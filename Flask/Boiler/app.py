from flask import Flask                     # Import Flask

app = Flask(__name__)                       # Create an object of a unique name

@app.route('/')                             # create a route to the home page of our app
def home():                                 # all routes need a method
    return "Hello, world!"

app.run(port=5000)