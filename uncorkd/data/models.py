"""Contains schema definitions of database and tables"""
__author__ = 'poojm'
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Boolean, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    """Summary of User Class.

    Object that contains information about registered users

    Attributes:
        id: An integer representing a unique identifier for the user
        name: A string representing the name of the user, as it was specified
                on the 3rd party, that was used to sign-in for the first time
        email: A string representing the email address for the user, from the
                3rd party site that was used to sign-in, for the first time
        picture_url: A string representing the picture for the user, from the
                3rd party site that was used to sign-in, for the first time
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    picture_url = Column(String(250))

class Visit(Base):
    __tablename__ = 'visits'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    winery_id = Column(Integer, ForeignKey('wineries.id'))
    date = Column(Date)

class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    wine_id = Column(Integer, ForeignKey('wines.id'))
    price = Column(Numeric)
    quantity = Column(Integer)
    date = Column(Date)

class Tasting(Base):
    __tablename__ = 'tastings'
    id = Column(Integer, primary_key=True)
    notes = Column(String(1000))
    pairings = Column(String(1000))
    wine_id = Column(Integer, ForeignKey('wines.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    rating = Column(Numeric)

class Winery(Base):
    """Summary of City Class.

    Object that contains information about a City

    Attributes:
        id: An integer representing a unique identifier for the city
        user_id: An integer representing the id of the user who create it
        name: A string representing the name of the city
        state_provence: A string representing the state or provence in which
                this city exists
        country: A string representing the country in which this city exists
        description: A string written by the user that can be used to learn
                more about a location
        image: A string representing the url of an image for the city
    """
    __tablename__ = 'wineries'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    address = Column(String(100))
    website = Column(String(150))
    onStNicks = Column(Boolean, default=False)
    hours_mon_o = Column(Time)
    hours_mon_c = Column(Time)
    hours_tues_o = Column(Time)
    hours_tues_c = Column(Time)
    hours_wed_o = Column(Time)
    hours_wed_c = Column(Time)
    hours_thurs_o = Column(Time)
    hours_thurs_c = Column(Time)
    hours_fri_o = Column(Time)
    hours_fri_c = Column(Time)
    hours_sat_o = Column(Time)
    hours_sat_c = Column(Time)
    hours_sun_o = Column(Time)
    hours_sun_c = Column(Time)
    wines = relationship("Wine", cascade="all,delete")


class Wine(Base):
    """Summary of Activity Class.

    Object that contains information about a City

    Attributes:
        id: An integer representing a unique identifier for the activity
        city_id: An integer representing a unique identifier for the city
                that has this activity
        user_id: An integer representing the id of the user who create it
        name: A string representing the name of the activity
        category: A string representing the category that the activity
                falls in
        description: A string written by the user that can be used to learn
                more about the activity
        website: A string representing the url of the website for an activity
        address: A string representing the street address of the activity
        image: A string representing the url of an image for the activity
    """
    __tablename__ = 'wines'
    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    winery_id = Column(Integer, ForeignKey('wineries.id'))
    color = Column(String(30))
    grapes = Column(String(30))
    description = Column(String(1000))
    vintage = Column(String(150))
    image = Column(String(150))
    wineries = relationship(Winery)

engine = create_engine('sqlite:///uncorkd4.db')
Base.metadata.create_all(engine)
