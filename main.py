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
            'greetings': u"Добро пожаловать",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': u"Про нас",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render(template_values))


class GalleryHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': u"Наша маленькая галерея",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
        self.response.write(template.render(template_values))


class ServicesHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': u"Наши услуги",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/services.html')
        self.response.write(template.render(template_values))



class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': u"Контакт",
        }

        template = JINJA_ENVIRONMENT.get_template('templates/contacts.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/about.html', AboutHandler),
    ('/gallery.html', GalleryHandler),
    ('/contacts.html', ContactHandler),
    ('/services.html', ServicesHandler),
], debug=True)
