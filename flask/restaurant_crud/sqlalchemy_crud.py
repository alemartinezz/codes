
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant_setup import Base, Restaurant, MenuItem

engine = create_engine("postgres://vagrant:laCumbre1@/restaurant")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create 
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

# Read
items = session.query(Restaurant).all()
for item in items:  
    print(item.name)

# Update
doctor_strange.title = "Some2016Film"  
session.commit()

# Delete
session.delete(doctor_strange)  
session.commit()