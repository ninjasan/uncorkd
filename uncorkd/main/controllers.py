__author__ = 'poojm'

from flask import Blueprint, render_template, url_for, redirect, request
from datetime import date, time
from uncorkd.data.models import Winery, Wine, User, Visit, Tasting, Purchase
from uncorkd.data.dbsession import session

main = Blueprint('main', __name__, template_folder='templates')

"""wineries = [{'id': 0,
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
        ]"""

@main.route('/')
def home():
    """Renders the about page."""
    return "Hello!"


@main.route('home/')
@main.route('wineries/')
def get_wineries():
    """Renders the page about wineries"""
    wineries = session.query(Winery).all()
    return render_template("wineries.html", wineries=wineries)


@main.route('wineries/add', methods=['GET', 'POST'])
def add_winery():
    if request.method == 'POST':
        '''Add the winery'''
        winery_to_add = Winery(name=request.form['name'],
                               address=request.form['address'],
                               website=request.form['website'])
        session.add(winery_to_add)
        session.commit()
        #TODO: flash message
        return redirect(url_for('.get_wineries'))
    else:
        return render_template("add_winery.html")


@main.route('wineries/<int:winery_id>/')
@main.route('wineries/<int:winery_id>/wines/')
def get_wines(winery_id):
    winery = session.query(Winery).filter(Winery.id == winery_id).one()
    wines = session.query(Wine).filter(Wine.winery_id == winery_id).all()
    #todo: get signed in user
    user_Id = 1
    last_visit = session.query(Visit).\
                    filter(Visit.user_id == user_Id,
                           Visit.winery_id == winery_id).\
                    order_by(Visit.date.desc()).first()
    print(last_visit)
    return render_template("wines.html", winery=winery,
                                         wines=wines,
                                         last_visit=last_visit)


@main.route('wineries/<int:winery_id>/checkin/', methods=['POST'])
def winery_visit(winery_id):
    if request.method == 'POST':
        #todo: change userId to actual userId
        check_in = Visit(user_id=1,
                         winery_id=winery_id,
                         date=date.today())
        session.add(check_in)
        session.commit()
        #todo: flash message
        return redirect(url_for('.get_wines', winery_id=winery_id))


@main.route('wineries/<int:winery_id>/wines/<int:wine_id>/')
def get_wine(winery_id, wine_id):
    wines = session.query(Wine).filter(Wine.id == wine_id).all()
    return render_template("wine.html", wine=wines)
