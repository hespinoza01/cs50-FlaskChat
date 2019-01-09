from flask import render_template as render
from . import routes, session


@routes.route('/', methods=('GET', 'POST'))
def index():
    return render('index.html', nickname=session.get('nickname'))
