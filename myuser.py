from google.appengine.ext import ndb

class MyUser(ndb.Model):
    email_address = ndb.StringProperty()
    anagramcount = ndb.IntegerProperty(default=0)
    wordcount = ndb.IntegerProperty(default=0)
