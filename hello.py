#!/usr/bin/env python

import flask
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing


DATABASE = '/tmp/whack_2016.db'
DEBUG = True

# Create the application.
APP = flask.Flask(__name__)
APP.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with APP.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(APP.config['DATABASE'])




@APP.before_request
def before_request():
    g.db = connect_db()

@APP.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@APP.route('/show_entries')
def show_seats():
    cur = g.db.execute('select * from seats')
    entries = [dict(row_num = row[0], seat_num = row[1], status = row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries = entries)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

#returns nested list of movie seat statuses
@APP.route('/test')
def get_seats():
    cur = g.db.execute('select * from seats where row_num=0')
    seat_list = []
    seat_list.append([row[2] for row in cur.fetchall()])
    
    cur = g.db.execute('select * from seats where row_num=1')
    seat_list.append([row[2] for row in cur.fetchall()])
    
    cur = g.db.execute('select * from seats where row_num=2')
    seat_list.append([row[2] for row in cur.fetchall()])

    cur = g.db.execute('select * from seats where row_num=3')
    seat_list.append([row[2] for row in cur.fetchall()])

    cur = g.db.execute('select * from seats where row_num=4')
    seat_list.append([row[2] for row in cur.fetchall()])
    
    return str(seat_list)

if __name__ == '__main__':
    init_db()
    APP.debug=True
    APP.run()
