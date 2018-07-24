from app import app
from db import db
db.init_app(app)                                                                                            # run.py creates the database for the API to work

@app.before_first_request                                                                                   # It runs the method below it before anything else
def create_tables():
    db.create_all()                                                                                         # Creates the schema and tables according to import of resources and the imports of models inside resources
