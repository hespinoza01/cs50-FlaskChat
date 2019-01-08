from flask import render_template as render
from . import routes


@routes.route('/')
def index():
    return render('index.html')
