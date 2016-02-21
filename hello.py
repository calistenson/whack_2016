#!/usr/bin/env python

import flask
 

# Create the application.
APP = flask.Flask(__name__)


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
    return flask.render_template('available.html')

@APP.route('/', methods = ['POST'])
def seats():
    num_seats = flask.request.form['num_seats']
    print("The number of seats is '" + num_seats + "'")
    return flask.redirect('/available')


if __name__ == '__main__':
    APP.debug=True
    APP.run()
