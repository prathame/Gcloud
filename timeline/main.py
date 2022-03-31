import datetime

from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
import webapp2
import jinja2
import os
import json
from datetime import date


class Details(ndb.Model):
    from_date = ndb.DateProperty()
    to_date = ndb.DateProperty()
    profile = ndb.StringProperty()

class User(ndb.Model):
    user_name = ndb.StringProperty()
    details = ndb.StructuredProperty(Details, repeated=True)


class MainPage(webapp2.RequestHandler):
    def post(self):
        p1=User(user_name="xyz@gmail.com",
                details=[
                    Details(
                        from_date=datetime.date(2000,11,30),
                        to_date=datetime.date(2001,11,30),
                        profile="happier",
                    )
                ])
    p1.put()


app = webapp2.WSGIApplication([
    ("/", MainPage)], debug=True)
