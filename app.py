from flask import Flask, jsonify, g
from flask_cors import CORS
#Calling the modles here
from resources.songs import song 
import models

DEBUG = True
PORT = 8000

# We are initilalizing 
app = Flask(__name__)

#The defaul

@app.route('/')
def index():
    return 'The apps is working!!!'

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

CORS(song, origins=['http://localhost:3000'], supports_credentials=True) 
app.register_blueprint(song, url_prefix='/api/v1/songs') # adding this line


#run the app when the program starts!!!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)