"""Contains basic app definition"""
__author__ = 'poojm'

from flask import Flask
from uncorkd.main.controllers import main

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/')
