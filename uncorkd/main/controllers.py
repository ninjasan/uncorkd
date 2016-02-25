__author__ = 'poojm'

from flask import Blueprint, render_template, url_for
#from uncorkd.data.models import City, Activity
#from uncorkd.data.dbsession import session

main = Blueprint('main', __name__, template_folder='templates')

wineries = [{'id': 0,
             'name': "Basel Cellars",
             'website': "http://baselcellars.com",
             'address': "15029 Woodinville-Redmond Rd NE #400, Woodinville, WA 98072"},
            {'id': 1,
             'name': "Cascade Cliffs Winery",
             'website': "http://www.cascadecliffs.com",
             'address': "15029 Woodinville-Redmond Rd NE # 300, Woodinville, WA 98072"},
            {'id': 2,
             'name': "Isenhower Cellars",
             'website': "http://www.isenhowercellars.com",
             'address': "15007 Woodinville-Redmond Rd NE, Woodinville, WA 98072"},
            {'id': 3,
             'name': "The Woodhouse Wine Estates",
             'website': "http://www.thewoodhousewineestates.com",
             'address': "15500 Woodinville-Redmond Rd NE, Woodinville, WA"}]

all_wines = [{'id': 0,
          'winery_id': 0,
          'name': "Estate Cabernet Sauvignon"},
         {'id': 1,
          'winery_id': 0,
          'name': "Estate Malbec"},
         {'id': 2,
          'winery_id': 0,
          'name': "Estate Merlot"},
         {'id': 3,
          'winery_id': 1,
          'name': "2013 Horse Heaven Hills Nebbiolo"},
         {'id': 4,
          'winery_id': 2,
          'name': "2013 DUTCHMAN VINEYARD SYRAH"},
         {'id': 5,
          'winery_id': 3,
          'name': "2008 KENNEDY SHAH RESERVE LA VIE EN ROUGE"},
        ]

@main.route('/')
def home():
    """Renders the about page."""
    return "Hello!"


@main.route('wineries/')
def get_wineries():
    """Renders the page about wineries"""
    #TODO: query wineries
    return render_template("wineries.html", wineries=wineries)


@main.route('wineries/<int:winery_id>/')
def get_wines(winery_id):
    #TODO: query on wines for this winery_id
    return render_template("wines.html", wines=all_wines)
