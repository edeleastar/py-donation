from flask import Flask, request, session, g, redirect, url_for, abort,  render_template, flash, _app_ctx_stack
from app.controllers.Accounts import Accounts
from app.controllers.DonationController import DonationController

SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

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
  app.run(debug=True)