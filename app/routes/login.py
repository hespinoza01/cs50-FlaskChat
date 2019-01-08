from . import routes


@routes.route('/login')
def login():
    return "Vista del login"
