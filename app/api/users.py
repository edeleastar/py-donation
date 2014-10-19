from .. import app
from app.models.User import User, users
from flask import jsonify

@app.route('/users/<int:id>')
def get_user(id):
  user = User.findById(id)
  if user != None:
    return jsonify(user.toJson())
  else:
    return "not found"

@app.route('/users')
def get_users():
  return jsonify \
  (
    {
      "users": [user.toJson() for user in users.values()]
    }
  )
