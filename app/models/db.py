from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
from sqlite3 import dbapi2 as sqlite3

DATABASE = 'donation.db'
app = None

def init_db(theApp):
  app = theApp
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()


def get_db():
  top = _app_ctx_stack.top
  if not hasattr(top, 'sqlite_db'):
    sqlite_db = sqlite3.connect(DATABASE)
    sqlite_db.row_factory = sqlite3.Row
    top.sqlite_db = sqlite_db

  return top.sqlite_db