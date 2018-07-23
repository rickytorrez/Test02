import sqlite3

connection = sqlite3.connect('data.db')                                                                             # Connect to DB
cursor = connection.cursor()                                                                                        # Start Cursor

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"            # Create users table query
cursor.execute(create_table)                                                                                        # Use cursor to execute the query

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"                   # Create items table query, (real is number with a decimal point)
cursor.execute(create_table)                                                                                        # Use cursor to execute the query

connection.commit()                                                                                                 # Commit(save) changes

connection.close()                                                                                                  # Close connection
