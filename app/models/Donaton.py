
donationId = 1

class Donation:
  def __init__(self, amount, method):
    global donationId
    self.amount = amount
    self.method = method
    self.id = donationId
    donationId = donationId + 1
