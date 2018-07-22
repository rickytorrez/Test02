from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

# Resource is an entity our API can create and return
# Resources are usually mapped into database tables

app = Flask(__name__)
app.secret_key = 'eduardo'
api = Api(app)

jwt = JWT(app, authenticate, identity)                                                                      # Creates a new endpoint /auth

items = []

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
        item = next(filter(lambda x: x['name'] == name, items), None)                                       # We filter the list of items and only get the one that
                                                                                                            # matches the name by using a lambda function. It takes
                                                                                                            # two arguments, a filtering function "x['name'] == name"
                                                                                                            # and the list of items we're filtering "items"  
                                                                                                            # We put None in the end in case we don't find the specific
                                                                                                            # item, otherwise, python will throw an error if there are
                                                                                                            # not items in the list since we are using the next keyword 
                                                                                                                                                                                                                                                     
        return {'item': item}, 200 if item else 404                                                         # If the item exists, we return the item and a 200 status if
                                                                                                            # it doesn't exist, we throw a 404 


################################## ENDPOINT TO POST A NEW ITEM IN THE LIST OF ITEMS ##################################
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):                                          # If we find an item with the name of the POST new item
            return {'message': "An item with the name of '{}' already exists.".format(name)}, 400           # throw error telling it that it already exists and send 
                                                                                                            # a 400 code for bad request
                                                                                                            
        data = Item.parser.parse_args()                                                                     # Parse the arguments that come through the JSON payload and it will put the 
                                                                                                            # valid ones in data
        item = {'name':name, 'price': data['price']}
        items.append(item)
        return item, 201

################################# ENDPOINT TO DELETE A NEW ITEM IN THE LIST OF ITEMS #################################
    def delete(self, name):
        global items                                                                                        # We want to use the global variable, the items variable is the outer one
        items = list(filter(lambda x: x['name'] != name, items))                                            # We're looking for all the elements except one and passing those to the item variable
        return {'message': 'Item deleted'}                                                                  # Return a message  

################################# ENDPOINT TO UPDATE A NEW ITEM IN THE LIST OF ITEMS #################################
    def put(self, name):
        data = Item.parser.parse_args()                                                                     # Parse the arguments that come through the JSON payload and it will put the 
                                                                                                            # valid ones in data
        item = next(filter(lambda x: x['name'] == name, items), None)                                       # Iterates through the items list to find the specific item
        if item is None:                                                                                    # If item doesn't exist
            item = {'name':name, 'price': data['price']}                                                    # Created it 
            items.append(item)                                                                              # Add item to the list of items
        else:                                                                                               # If item exists
            item.update(data)                                                                               # Update the item
        return item                                                                                         # Return the item

class ItemList(Resource):
##################################### ENDPOINT TO GET THE LIST OF ALL THE ITEMS ######################################
    def get(self):
        return {'items':items}                                                                              # Returns the list of items

api.add_resource(Item, '/item/<string:name>')  
api.add_resource(ItemList, '/items')             

app.run(port=5000, debug=True)