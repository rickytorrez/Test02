import sqlite3

connection = sqlite3.connect('data.db')                                             # Connects to sqlite and creates schema named data.db

cursor = connection.cursor()                                                        # Cursor runs the query and stores the result

create_table = "CREATE TABLE users(id int, username text, password text)"           # Creates a new table with the attributes
cursor.execute(create_table)                                                        # Runs the query

user = (1, 'ricardo', 'asdf')                                                       # Create a new user
insert_query = "INSERT INTO users VALUES (?, ?, ?)"                                 # Query for values to be inserted
cursor.execute(insert_query, user)                                                  # Execute the query

users = [
    (2, 'palolo', 'asdf'),
    (3, 'felipe', 'xyz')
]

cursor.executemany(insert_query, users)                                             # Inserts users list 

select_query = "SELECT * FROM users"                                                # Retrieves items from the database
for row in cursor.execute(select_query):                                            # Iterates through the query
    print(row)                                                                      # Prints each user

connection.commit()                                                                 # Commit Changes
connection.close()                                                                  # Close connection so it won't be wasting resources
