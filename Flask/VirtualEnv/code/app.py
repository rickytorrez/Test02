from flask import Flask, request
from flask_restful import Resource, Api

# Resource is an entity our API can create and return
# Resources are usually mapped into database tables

app = Flask(__name__)
app.secret_key = 'eduardo'
api = Api(app)

items = []

class Item(Resource):                           
################################# ENDPOINT TO GET A SINGLE ITEM IN THE LIST OF ITEMS #################################
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
        data = request.get_json()
        item = {'name':name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
##################################### ENDPOINT TO GET THE LIST OF ALL THE ITEMS ######################################
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')  
api.add_resource(ItemList, '/items')             

app.run(port=5000, debug=True)