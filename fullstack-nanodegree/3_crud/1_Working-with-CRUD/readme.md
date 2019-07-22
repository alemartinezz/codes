# CRUD

## Create database with SQLAlchemy

```python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant) 

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):

       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'course'         : self.course,
       }


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
```

## CRUD Review

## Operations with SQLAlchemy

In this lesson, we performed all of our CRUD operations with SQLAlchemy on an SQLite database. Before we perform any operations, we must first import the necessary libraries, connect to our restaurantMenu.db, and create a session to interface with the database:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
```

## CREATE

We created a new Restaurant and called it Pizza Palace:

```python
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
sesssion.commit()
```

We created a cheese pizza menu item and added it to the Pizza Palace Menu:

```python
cheesepizza = MenuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
```

## READ

We read out information in our database using the query method in SQLAlchemy:

```python
firstResult = session.query(Restaurant).first()
firstResult.name
items = session.query(MenuItem).all()
for item in items:
    print item.name
```

## UPDATE

In order to update and existing entry in our database, we must execute the following commands:

   1. Find Entry
   2. Reset value(s)
   3. Add to session
   4. Execute session.commit()

We found the veggie burger that belonged to the Urban Burger restaurant by executing the following query:

```python
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
```

Then we updated the price of the veggie burger to $2.99:

```python
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
```

## DELETE

To delete an item from our database we must follow the following steps:

    1. Find the entry
    2. Session.delete(Entry)
    3. Session.commit()

We deleted spinach Ice Cream from our Menu Items database with the following operations:

```python
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit()
```