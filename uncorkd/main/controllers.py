__author__ = 'poojm'

from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    """Renders the about page."""
    return "Hello!"
