from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissuperinsecure'
from simple import server
