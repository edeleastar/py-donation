from flask import render_template, url_for, redirect, request
from app.models import donations
from app.models.Donaton import Donation

from . import donate

@donate.route('/donation')
def index():
  return render_template('views/DonationController/index.html')

@donate.route('/donation/donate', methods=['POST'])
def donateAmount():
  amount = request.form['amountDonated']
  method = request.form['methodDonated']
  donations.append(Donation(amount, method))
  return redirect('/donation')

@donate.route('/donation/report')
def report():
  return render_template('views/DonationController/report.html', donations=donations)