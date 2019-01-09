from flask import render_template as render
from . import routes


@routes.route('/', methods=('GET', 'POST'))
def index():
    return render('index.html')
