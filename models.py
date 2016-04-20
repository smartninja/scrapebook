from google.appengine.ext import ndb


class Person(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    gender = ndb.StringProperty()
    city = ndb.StringProperty()
    age = ndb.IntegerProperty()

    @property
    def get_id(self):
        return self.key.id()

    @property
    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @classmethod
    def create(cls, first_name, last_name, email, gender, city, age):
        person = cls(first_name=first_name, last_name=last_name, email=email, gender=gender, city=city, age=age)
        person.put()
        return person
