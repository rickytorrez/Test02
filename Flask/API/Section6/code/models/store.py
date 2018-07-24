from db import db

class StoreModel(db.Model):                                                                                 # db.Model tells SQLAlchemy that Item model is a thing that we
                                                                                                            # will save and retrieve from the database
    __tablename__ = 'stores'                                                                                # Create the items DATABASE

    id = db.Column(db.Integer, primary_key=True)                                                            # Create the id Colummn
    name = db.Column(db.String(80))                                                                         # Create the name column

    items = db.relationship('ItemModel', lazy='dynamic')                                                    # Retrieve all the items that belong to a store

    def __init__(self, name):
        self.name = name

################################## JSON METHOD TO RETURN A DICTIONARY OF THE MODEL  ##################################
    def json(self):                                                                                         # JSON method
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}                     # Return a JSON representation of the model, store name and its items


#################### @CLASSMETHOD TO FIND A SINGLE ITEM IN THE LIST OF ITEMS NO JWT AUTH REQUIRED ####################
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()                                                       # Return the cls (StoreModel), use query which is a SQLAlchemy built in function
                                                                                                            # to create a query and filter by name and return the first row only
                                                                                                            # SELECT * FROM -(__tablename__)- stores WHERE name = name LIMIT 1

#################### @CLASSMETHOD TO INSERT AN ITEM INTO THE DATABASE - USED IN POST & PUT METHODS ###################
    def save_to_db(self):                                                                                   # Updating/Upserting to the DB
        db.session.add(self)                                                                                # Tell SQLAlchemy to insert this object(self) into the database
        db.session.commit()                                                                                 # Save to the database

######################## @CLASSMETHOD TO DELETE AN ITEM IN THE DATABASE - USED IN PUT METHOD #########################
    def delete_from_db(self):
        db.session.delete(self)                                                                             # Delete the object from the db
        db.session.commit()                                                                                 # Save changes
