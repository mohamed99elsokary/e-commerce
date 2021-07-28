from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_mysqldb import MySQL
import datetime
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
socketio = SocketIO( app )

from config import *
mysql = MySQL(app)