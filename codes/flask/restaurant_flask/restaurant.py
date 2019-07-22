#!/usr/bin/env python3.6

# flask
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)

# importar librerias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_setup import Base, Restaurant, MenuItem


# Create session and connect
engine = create_engine("postgres://vagrant:losguachos@/restaurant")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurant-<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)

    return render_template('restaurant_menu.html', restaurant=restaurant, items=items)


@app.route('/restaurant-<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenu(restaurant_id):
    if request.method == 'POST':
        new_menu = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(new_menu)
        session.commit()
        flash("Menu created successfully")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('menu_new.html', restaurant_id=restaurant_id)


@app.route('/restaurant-<int:restaurant_id>/menu-<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenu(restaurant_id, menu_id):

    editedMenu = session.query(MenuItem).filter_by(id=menu_id).one()
    
    if request.method == 'POST':
        editedMenu.name = request.form['name']
        session.add(editedMenu)
        session.commit()
        flash("Menu edited successfully")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('menu_edit.html', restaurant_id=restaurant_id, menu=editedMenu)


@app.route('/restaurant-<int:restaurant_id>/menu-<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):

    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()

    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu deleted successfully")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('menu_delete.html', item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'SUPER_SECRET_KEY'
    app.debug = True
    app.run (host='0.0.0.0', port=8000)
