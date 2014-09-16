#!/usr/bin/env python
# coding=utf-8

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': "Добро пожаловать",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': "Про нас",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render(template_values))


class GalleryHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': "Наша маленькая галерея",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
        self.response.write(template.render(template_values))


class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': "Контакт",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/contacts.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/about', AboutHandler),
    ('/gallery', GalleryHandler),
    ('/contacts', ContactHandler),
], debug=True)
