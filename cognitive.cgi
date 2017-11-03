#!/usr/bin/python

from wsgiref.handlers import CGIHandler
#from myapp import app
from cognitiveapp.cognitive import app


CGIHandler().run(app)
