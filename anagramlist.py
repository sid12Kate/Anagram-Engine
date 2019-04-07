from google.appengine.ext import ndb

class AnagramList(ndb.Model):
    list = ndb.StringProperty(repeated=True)
    wordcount = ndb.IntegerProperty()
    lettercount = ndb.IntegerProperty()
