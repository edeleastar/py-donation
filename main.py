from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
from sqlite3 import dbapi2 as sqlite3

from app.models.db import init_db

from app.controllers.Accounts import Accounts
from app.controllers.DonationController import DonationController

# configuration
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)


@app.teardown_appcontext
def close_db_connection(exception):
  top = _app_ctx_stack.top
  if hasattr(top, 'sqlite_db'):
    top.sqlite_db.close()

@app.route('/')
def index():
  return Accounts.index()

@app.route('/login')
def login():
  return Accounts.login()

@app.route('/signup')
def signup():
  return Accounts.signup()

@app.route('/register', methods=['POST'])
def register():
  return Accounts.register()

@app.route('/logout')
def logout():
  return Accounts.logout()

@app.route('/authenticate', methods=['POST'])
def authenticate():
  return Accounts.authenticate()

@app.route('/donation')
def donation():
  return DonationController.index()

@app.route('/donation/donate', methods=['POST'])
def donate():
  return DonationController.donate()

@app.route('/donation/report')
def report():
  return DonationController.report()

if __name__ == '__main__':
  init_db(app)
  app.run(debug=True)