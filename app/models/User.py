users = {}
userId = 1

class User:
  def __init__(self, firstname, lastname, email, password):
    global userId

    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.password = password
    self.id = userId
    userId += 1

  def toJson(self):
    json_user = \
    {
      'firstname' : self.firstname,
      'lastname'  : self.lastname,
      'email'     : self.email,
      'password'  : self.password
    }
    return json_user

  @staticmethod
  def findById(id):
    global users
    for user in users.values():
      if user.id == id:
        return user
    return None


