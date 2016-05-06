from uncorkd.data.models import Winery, Wine
from uncorkd.data.dbsession import session

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

wines = [{'id': 0,
          'winery_id': 1,
          'name': "Estate Cabernet Sauvignon"},
         {'id': 1,
          'winery_id': 1,
          'name': "Estate Malbec"},
         {'id': 2,
          'winery_id': 1,
          'name': "Estate Merlot"},
         {'id': 3,
          'winery_id': 2,
          'name': "2013 Horse Heaven Hills Nebbiolo"},
         {'id': 4,
          'winery_id': 3,
          'name': "2013 DUTCHMAN VINEYARD SYRAH"},
         {'id': 5,
          'winery_id': 4,
          'name': "2008 KENNEDY SHAH RESERVE LA VIE EN ROUGE"},
        ]


for winery in wineries:
    winery_to_add = Winery(name=winery['name'],
                           website=winery['website'],
                           address=winery['address'])
    session.add(winery_to_add)
    session.commit()

for wine in wines:
    wine_to_add = Wine(name=wine['name'],
                    winery_id=wine['winery_id'])
    session.add(wine_to_add)
    session.commit()

test = session.query(Wine).all()
for item in test:
    print(item.name)