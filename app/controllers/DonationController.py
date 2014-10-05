from flask import Flask
from flask import render_template, url_for, redirect, request
from app.models.db import get_db

class DonationController:

  @staticmethod
  def index():
    return render_template('views/DonationController/index.html')

  @staticmethod
  def donate():
    amount = request.form['amountDonated']
    method = request.form['methodDonated']
    db = get_db()
    db.execute('insert into donations (amount, method) values (?, ?)', [amount, method])
    db.commit()
    return redirect('/donation')

  @staticmethod
  def report():
    db = get_db()
    cur = db.execute('select amount, method from donations order by id desc')
    donations = cur.fetchall()
    return render_template('views/DonationController/report.html', donations=donations)