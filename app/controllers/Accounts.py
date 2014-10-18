from flask import render_template, url_for, redirect, request, session
from app.models.User import User
from app.models import users

class Accounts:

  @staticmethod
  def index():
    return render_template('views/Accounts/index.html')

  @staticmethod
  def login():
    return render_template('views/Accounts/login.html')

  @staticmethod
  def logout():
    return render_template('views/Accounts/index.html')

  @staticmethod
  def signup():
    return render_template('views/Accounts/signup.html')

  @staticmethod
  def register():
    firstname = request.form['firstName']
    lastname  = request.form['lastName']
    email     = request.form['email']
    password  = request.form['password']
    users[email] = (User (firstname, lastname, email, password))
    return redirect('/')

  @staticmethod
  def authenticate():
    email     = request.form['email']
    password  = request.form['password']
    if email in users and password == users[email].password:
      session['logged_in'] = True
      return redirect('/donation')
    else:
      return redirect('/')