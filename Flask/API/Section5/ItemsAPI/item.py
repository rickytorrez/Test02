import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

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
        item = self.find_by_name(name)                                                                      # Uses classmethod bellow to connect to db and find item
        if item:
            return item
        return {'message': 'Item not found'}, 404                                                           # Else, return an error message

#################### @CLASSMETHOD TO FIND A SINGLE ITEM IN THE LIST OF ITEMS NO JWT AUTH REQUIRED ####################
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "SELECT * FROM items WHERE name=?"                                                          # Query to look for the particular item
        result = cursor.execute(query, (name,))                                                             # Put the result in a variable, the name must be a tuple
        row = result.fetchone()                                                                             # Fetch one row, no duplicates
        connection.close()                                                                                  # Close connection

        if row:                                                                                             # If the row of data exists
            return {'item': {'name':row[0], 'price':row[1]}}                                                # Return it with the name and price

################################## ENDPOINT TO POST A NEW ITEM IN THE LIST OF ITEMS ##################################
    def post(self, name):
        if self.find_by_name(name):                                                                         # Uses the class method above to look for the item
            return {'message': "An item with the name of '{}' already exists.".format(name)}, 400           # throw error telling it that it already exists and send
                                                                                                            # a 400 code for bad request

        data = Item.parser.parse_args()                                                                     # Parse the arguments that come through the JSON payload and it will put the
                                                                                                            # valid ones in data
        item = {'name':name, 'price': data['price']}

        try:
            self.insert(item)                                                                               # Uses the class method bellow to insert values into the database
        except:
            return {'message': 'An error occurred while inserting the item'}, 500                           # 500 Internal server error
        return item, 201                                                                                    # Return the item

#################### @CLASSMETHOD TO INSERT AN ITEM INTO THE DATABASE - USED IN POST & PUT METHODS ###################
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "INSERT INTO items VALUES(?,?)"                                                             # Query to insert the item into DB
        cursor.execute(query, (item['name'],item['price']))                                                 # Use cursor to execute query

        connection.commit()                                                                                 # Save changes
        connection.close()                                                                                  # Close connection

################################# ENDPOINT TO DELETE A NEW ITEM IN THE LIST OF ITEMS #################################
    def delete(self, name):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "DELETE FROM items WHERE name=?"                                                            # Query to delete the item from the DB where the name matches
        cursor.execute(query, (name,))                                                                      # Use cursor to execute query

        connection.commit()                                                                                 # Save changes
        connection.close()                                                                                  # Close connection

        return {'message': 'Item deleted'}                                                                  # Return a message

################################# ENDPOINT TO UPDATE A NEW ITEM IN THE LIST OF ITEMS #################################
    def put(self, name):
        data = Item.parser.parse_args()                                                                     # Parse the arguments that come through the JSON payload and it will put the
                                                                                                            # valid ones in data
        item = self.find_by_name(name)                                                                      # Uses the classmethod find_by_name to look for the specific item
        updated_item = {'name':name, 'price': data['price']}

        if item is None:                                                                                    # If item doesn't exist
            try:
                self.insert(updated_item)                                                                   # Add updated_item to the list of items as a new item using the class method above
            except:
                return {'message': 'An error occurred while inserting the item'}, 500                       # 500 Internal server error
        else:                                                                                               # If item exists
            try:
                self.update(updated_item)                                                                   # Update the item
            except:
                return {'message': 'An error occurred while updating the item'}, 500                        # 500 Internal server error
        return updated_item                                                                                 # Return the item

######################## @CLASSMETHOD TO UPDATE AN ITEM IN THE DATABASE - USED IN PUT METHOD #########################
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "UPDATE items SET price=? WHERE name=?"                                                     # Query to update the price of a particular item name in the DB
        cursor.execute(query, (item['price'], item['name']))                                                # Use cursor to execute query, make sure arguments are in the correct order

        connection.commit()                                                                                 # Save changes
        connection.close()                                                                                  # Close connection

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
