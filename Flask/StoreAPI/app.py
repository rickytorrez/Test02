from flask import Flask, jsonify, request, render_template                   

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

####################################### HTML FILE FOR TESTING OF OUR ENDPOINTS #######################################

@app.route('/')
def home():
    return render_template('index.html')

###################################### CREATES A NEW STORE WITH A SPECIFIC NAME ######################################

# POST /store data: {name}                                          
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()                               # Request made to the endpoint, browser will send JSON data which is the name of the store
    new_store = {                                                   # Create a new store
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)                                        # Add the new store to the list of stores
    return jsonify(new_store)                                       # Return the new store in JSON format so we can view it

###################################### FINDS A STORE WITH A SPECIFIC GIVEN NAME ######################################

# GET  /store/<string:name>                                         
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:                                            # Iterate over stores
        if store['name'] == name:                                   # if the store exists
            return jsonify(store)                                   # return it in JSON format
    return jsonify({'message': 'store not found'})                  # if not, throw a message error


####################################### RETURNS THE LIST OF ALL CREATED STORES #######################################

# GET  /store                                                       
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})                               # Converts the stores variable into JSON & turns List of stores into a dictionary
              
###################################### CREATES AN ITEM INSIDE A SPECIFIC STORE #######################################

# POST /store/<string:name>/item                                    
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()                               # request data is used for post methods
    for store in stores:                                            # iterate through stores
        if store['name'] == name:                                   # if the store exists
            new_item = {                                            # create new item
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)                         # store the item in the list of the store's items
            return jsonify(new_item)                                # return the item
    return jsonify({'message': 'store not found'})                  # if not, throw a message error

###################################### FINDS ALL THE ITEMS INSIDE A GIVEN STORE ######################################

# GET  /store/<string:name>/item                                    
@app.route('/store/<string:name>/item')
def get_items_in_store(name):                                       
    for store in stores:                                            # Iterate over stores
        if store['name'] == name:                                   # if the store exists
            return jsonify({'items': store['items']})               # return the items inside the store
    return jsonify({'message': 'store not found'})                  # if not, throw a message error



app.run(port=5000)