import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

################################## JSON METHOD TO RETURN A DICTIONARY OF THE MODEL  ##################################
    def json(self):                                                                         # JSON method
        return {'name': self.name, 'price': self.price}                                     # Return a JSON representation of the model


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
            return cls(*row)                                                                                # cls calls the ItemModel __init__ method and fills in the
                                                                                                            # parameters with the keyword *row

#################### @CLASSMETHOD TO INSERT AN ITEM INTO THE DATABASE - USED IN POST & PUT METHODS ###################
    def insert(self):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "INSERT INTO items VALUES(?,?)"                                                             # Query to insert the item into DB
        cursor.execute(query, (self.name, self.price))                                                      # Use cursor to execute query

        connection.commit()                                                                                 # Save changes
        connection.close()                                                                                  # Close connection

######################## @CLASSMETHOD TO UPDATE AN ITEM IN THE DATABASE - USED IN PUT METHOD #########################
    def update(self):
        connection = sqlite3.connect('data.db')                                                             # Connect to the database
        cursor = connection.cursor()                                                                        # Start cursor

        query = "UPDATE items SET price=? WHERE name=?"                                                     # Query to update the price of a particular item name in the DB
        cursor.execute(query, (self.price, self.name))                                                      # Use cursor to execute query, make sure arguments are in the correct order

        connection.commit()                                                                                 # Save changes
        connection.close()                                                                                  # Close connection
