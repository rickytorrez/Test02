import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
################################# ENDPOINT TO GET A SINGLE ITEM IN THE LIST OF ITEMS #################################
    @jwt_required()                                                                                         # JWT-required forces us to authenticate before we can do anything
    def get(self, name):
        item = ItemModel.find_by_name(name)                                                                 # Uses classmethod bellow to connect to db and find item object
        if item:
            return item.json()                                                                              # Returns the item
        return {'message': 'Item not found'}, 404                                                           # Else, return an error message

################################## ENDPOINT TO POST A NEW ITEM IN THE LIST OF ITEMS ##################################
    def post(self, name):
        if ItemModel.find_by_name(name):                                                                    # Uses the class method above to look for the item
            return {'message': "An item with the name of '{}' already exists.".format(name)}, 400           # throw error telling it that it already exists and send
                                                                                                            # a 400 code for bad request

        data = Item.parser.parse_args()                                                                     # Parse the arguments that come through the JSON payload and it will put the
                                                                                                            # valid ones in data
        item = ItemModel(name, data['price'])                                                               # ItemModel object

        try:
            item.save_to_db()                                                                               # Save to DB the ItemModel object
        except:
            return {'message': 'An error occurred while inserting the item'}, 500                           # 500 Internal server error

        return item.json(), 201                                                                             # Return the item

################################# ENDPOINT TO DELETE A NEW ITEM IN THE LIST OF ITEMS #################################
    def delete(self, name):
        item = ItemModel.find_by_name(name)                                                                 # Find the item by name
        if item:                                                                                            # If the item exists
            item.delete_from_db()                                                                           # Use the method in the ItemModel to remove the item from the DB
        return {'message': 'Item deleted'}

################################# ENDPOINT TO UPDATE A NEW ITEM IN THE LIST OF ITEMS #################################
    def put(self, name):
        data = Item.parser.parse_args()                                                                     # Parse the arguments that come through the JSON payload and it will put the
                                                                                                            # valid ones in data
        item = ItemModel.find_by_name(name)                                                                 # Uses the Model find by name method and returns the ItemModel object

        if item is None:                                                                                    # If the item is not found
            item = ItemModel(name, data['price'])                                                           # We create a new instance ot the ItemModel
        else:                                                                                               # If item exists
            item.price = data['price']                                                                      # update the price

        item.save_to_db()                                                                                   # Whether the item exists or not, we save to the db
        return item.json()                                                                                  # Return the item in JSON format instead of an object


################################################# GET ALL THE ITEMS ##################################################
class ItemList(Resource):
##################################### ENDPOINT TO GET THE LIST OF ALL THE ITEMS ######################################
    def get(self):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "SELECT * FROM items"                                                                       # Query to select everything inside out items table
        result = cursor.execute(query)                                                                      # Use cursor to execute query

        items =[]                                                                                           # Create an empty list called items
        for row in result:                                                                                  # Iterate through the result variable
            items.append({'name':row[0], 'price': row[1]})                                                  # Append each item by using row[0] for name and row[1] for price

        connection.close()                                                                                  # Close the connection, there's nothing to commit since we're not changing anything
        return {'items': items}                                                                             # Return the list of items
