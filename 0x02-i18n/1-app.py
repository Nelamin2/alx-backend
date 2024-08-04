#! /usr/bin/env python3

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)

class config:
    """Configures the app."""
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'
    LANGUAGES = ['en', 'fr']
    
    

