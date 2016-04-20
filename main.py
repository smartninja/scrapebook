#!/usr/bin/env python
import os
import jinja2
import webapp2
from google.appengine.api import users
from models import Person
from utils import create_fake_persons

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        persons = Person.query().fetch()
        params = {"persons": persons}
        return self.render_template("main.html", params=params)


class PersonHandler(BaseHandler):
    def get(self, person_id):
        person = Person.get_by_id(int(person_id))
        params = {"person": person}
        return self.render_template("person.html", params=params)


class CreateNewUsersHandler(BaseHandler):
    def get(self):
        if users.is_current_user_admin():
            create_fake_persons(person_number=10)
        return self.redirect_to("main")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main"),
    webapp2.Route('/person/<person_id:\d+>', PersonHandler),
    webapp2.Route('/person/create-new', CreateNewUsersHandler),
], debug=True)
