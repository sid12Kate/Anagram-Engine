import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from myuser import MyUser
from wordlist import WordList
from anagramlist import AnagramList

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''
        welcome = 'Welcome back'
        myuser = None
        user = users.get_current_user()
        list = ''
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'
            anagramlist = AnagramList()
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            if myuser == None:
                welcome = 'Welcome to the application'
                myuser = MyUser(id=user.user_id())
                myuser.email_address = user.email()
                myuser.anagramcount = 0
                myuser.put()


        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'

        action = self.request.get('button')
        if action == 'Search':
            string = self.request.get('value_2')
            word = sorted(string)
            order = ''.join(word)
            key = ndb.Key('AnagramList', user.user_id()+order)
            anagramlist = key.get()
            list = anagramlist.list
            if list == None:
                self.redirect('/')

        template_values = {
            'url' : url,
            'url_string' : url_string,
            'user' : user,
            'welcome' : welcome,
            'anagramlist' : list
        }

        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))






app = webapp2.WSGIApplication([
     ('/', MainPage),
     ('/wordlist', WordList)
], debug=True)
