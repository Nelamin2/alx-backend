#! /usr/bin/env python3

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Returns the index.html page."""
    return render_template('0-index.html')

    
if __name__ == '__main__':
    app.run(debug=True)