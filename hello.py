#!/usr/bin/env python

import flask
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from Arduino import hello


DATABASE = '/tmp/whack_2016.db'
DEBUG = True

# Create the application.
APP = flask.Flask(__name__)
APP.config.from_object(__name__)


seat_dict = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): 4, (0, 4): 5, (1, 0): 6, (1, 1): 7, (1, 2): 8, (1, 3): 9, (1, 4): 10, (2, 0): 11, 
(2, 1): 12, (2 ,2): 13, (2, 3): 14, (2, 4): 15, (3, 0): 16, (3, 1): 17, (3, 2): 18, (3, 3): 19, (3, 4): 20, (4, 0): 21, (4, 1): 22, (4, 2): 23, (4, 3): 24, (4, 4): 25}

def find_Seats(theater, num):
	if num > 5: return 
	seats = []
	for (i, row) in enumerate(theater): #for each row in the theater
		for (j, seat) in enumerate(row): #for each seat in the row
			need = num
			curr_seats = []
			while (need > 0) and (j < 5):
				if theater[i][j] == 0:
					curr_seats.append((i, j))
					need -= 1
					j += 1
				else: 
					curr_seats = []
					need = num
					j += 2
				if len(curr_seats) ==  num:
					if curr_seats not in seats:
						seats.append(curr_seats)
						curr_seats = []
						need = 0
	return seats 

def availableSeats(theater):
	#return the first seat in a sequence of n available seats
	seats = []
	for (i, row) in enumerate(theater): 
		for (j, seat) in enumerate(row):
			if theater[i][j] == 0:
				seats.append((i, j))
	return seats

def seatStatus(theater, row, col): 
	return  theater[row][col] #theater is a 2d array; return 0 if empty, 1 if seat is full

# # Changes status of seat from empty to full and vice versa, when the sensor status changes
def changeStatus(theater, row, col): 
	current = seatStatus(theater, row, col) #when we actually have a database running, we'll need to access the value from there
	theater[row][col] = 1 if current == 0 else 0 #but make sure to actually change the value in the database


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

@APP.route('/about')
def about():
    """ Displays the about page accessible at '/about'
    """
    return flask.render_template('about.html')

@APP.route('/available')
def available():
    """ Displays the about page accessible at '/available'
    """
    #return str(findSeats.findSeats(2))
    num_seats = request.args['messages']
    
    status = hello()
    script = 'update seats set status =' + str(status) + ' where row_num=1 and seat_num=1'
    cur = g.db.execute(script)
     
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
    
    #cur = g.db.execute('update seats set status= 23 where row_num=2 and seat_num=2')
    #return str(find_Seats(seat_list,int(num_seats)))
    return flask.render_template('available.html', entries=find_Seats(seat_list,int(num_seats)))
    #return str(seat_list)
    #return str(status)

@APP.route('/', methods = ['POST'])
def seats():
    num_seats = flask.request.form['num_seats']
    print("The number of seats is '" + num_seats + "'")
    return flask.redirect(url_for('.available',messages = num_seats))

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
    #return str(find_Seats(seat_list,5))





if __name__ == '__main__':
    init_db()
    APP.debug=True
    APP.run()
