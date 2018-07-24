from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister                                                                     # Import from the correct file
from resources.item import Item, ItemList                                                                   # Import from the correct file
from resources.store import Store, StoreList                                                                # Import the Store Resource and StoreList Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'                                                 # Tell SQLAlchemy where the db is
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                                                        # SQLAlchemy has its own mod tracker
app.secret_key = 'eduardo'
api = Api(app)

@app.before_first_request                                                                                   # It runs the method below it before anything else
def create_tables():
    db.create_all()                                                                                         # Creates the schema and tables according to import of resources and the imports of models inside resources

jwt = JWT(app, authenticate, identity)                                                                      # Creates a new endpoint /auth

api.add_resource(Store, '/store/<string:name>')                                                             # API endpoint to get, post, put, delete a store
api.add_resource(Item, '/item/<string:name>')                                                               # API endpoint to get, post, put, delete an item
api.add_resource(ItemList, '/items')                                                                        # API endpoint to get all items
api.add_resource(StoreList, '/stores')                                                                      # API endpoint to get all stores
api.add_resource(UserRegister, '/register')                                                                 # API endpoint for registering a user

if __name__ == '__main__':
    from db import db                                                                                       # Circular imports
    db.init_app(app)
    app.run(port=5000, debug=True)
