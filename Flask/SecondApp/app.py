from flask import Flask, jsonify                   

app = Flask(__name__)  

# List of Stores
stores = [                          
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data back only


# POST /store data: {name}                                  - Creates a new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET  /store/<string:name>                                 - Get a store for a given name
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET  /store                                               - Returns a list of all the stores
@app.route('/store')
def get_stores():
    # Converts the stores variable into JSON
    # Turns List of stores into a dictionary
    return jsonify({'stores':stores})          

# POST /store/<string:name>/item                            - Creates an item inside a specific store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET  /store/<string:name>/item                            - Gets all the items inside a specific store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass



app.run(port=5000)