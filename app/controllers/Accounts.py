from flask import Flask
from flask import render_template, url_for, redirect

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
    return redirect('/')

  @staticmethod
  def authenticate():
    return redirect('/donation')