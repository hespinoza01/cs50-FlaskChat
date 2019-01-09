from flask import Blueprint, session, url_for, redirect, request


routes = Blueprint('routes', __name__, template_folder='views')


def before_request():
    if 'nickname' not in session and request.endpoint in ['routes.index']:
        return redirect(url_for('routes.login'))
    elif 'nickname'in session and request.endpoint in ['routes.login']:
        return redirect(url_for('routes.index'))


routes.before_request(before_request)


nicknames = []


from . import index
from . import login
