from flask import Blueprint

accounts = Blueprint('accounts', __name__)
donate   = Blueprint('donate', __name__)

from . import Accounts
from . import DonationController