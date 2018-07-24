from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

################################ ENDPOINT TO GET A SINGLE STORE IN THE LIST OF ITEMS #################################
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

############################## ENDPOINT TO CREATE A SINGLE STORE IN THE LIST OF ITEMS ################################
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store =  StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occurred while creating the store.'}, 500

        return store.json(), 201

############################## ENDPOINT TO DELETE A SINGLE STORE IN THE LIST OF ITEMS ################################
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

##################################### ENDPOINT TO GET A LIST OF ALL THE STORES #######################################
class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
