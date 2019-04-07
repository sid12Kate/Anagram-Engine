import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from anagramlist import AnagramList
import os
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True
)

class WordList(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        my_list = AnagramList()

        template_values = {
         'my_list' : my_list
        }
        template =JINJA_ENVIRONMENT.get_template('wordlist.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        anagramlist = AnagramList()
        if action == 'Add':
            user = users.get_current_user()
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            string = self.request.get('value_1')
            word = sorted(string)
            order = ''.join(word)
            key = ndb.Key('AnagramList', user.user_id()+order)
            anagramlist = key.get()
            if anagramlist == None:
                anagramlist = AnagramList(id=user.user_id()+order)
                anagramlist.list.append(string)
                anagramlist.wordcount = 1
                myuser.anagramcount += 1
                myuser.wordcount += 1
                anagramlist.lettercount = len(order)
                anagramlist.put()
                myuser.put()
            else:
                length = len(anagramlist.list)
                anagramlist.wordcount = length + 1
                myuser.wordcount += 1
                anagramlist.list.append(string)
                anagramlist.put()
                myuser.put()
        if action == 'Upload':
            words = self.request.get('filename')
            content = words.split()
            for x in content:
                user = users.get_current_user()
                myuser_key = ndb.Key('MyUser', user.user_id())
                myuser = myuser_key.get()
                string = x
                word = sorted(string)
                order = ''.join(word)
                key = ndb.Key('AnagramList', user.user_id()+order)
                anagramlist = key.get()
                if anagramlist == None:
                    anagramlist = AnagramList(id=user.user_id()+order)
                    anagramlist.list.append(string)
                    anagramlist.wordcount = 1
                    myuser.anagramcount += 1
                    myuser.wordcount += 1
                    anagramlist.lettercount = len(order)
                    anagramlist.put()
                    myuser.put()
                else:
                    length = len(anagramlist.list)
                    anagramlist.wordcount = length + 1
                    myuser.wordcount += 1
                    anagramlist.list.append(string)
                    anagramlist.put()
                    myuser.put()

        self.redirect('/')
