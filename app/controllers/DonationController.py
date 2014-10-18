from flask import render_template, url_for, redirect, request
from app.models import donations
from app.models.Donaton import Donation

class DonationController:

  @staticmethod
  def index():
    return render_template('views/DonationController/index.html')

  @staticmethod
  def donate():
    amount = request.form['amountDonated']
    method = request.form['methodDonated']
    donations.append(Donation(amount, method))
    return redirect('/donation')

  @staticmethod
  def report():
    return render_template('views/DonationController/report.html', donations=donations)