from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Book_db(ndb.Model):
    Book = ndb.StringProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        query = ndb.gql("SELECT Book FROM Book_db ")
        values = {'query': query}
        self.response.write(template.render(values))



class Add_Data(webapp2.RequestHandler):
    def post(self):
        new_book=Book_db(Book=self.request.get('book_input'))
        book_db.put()
        self.redirect('/')


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/add_data",Add_Data)], debug=True)
