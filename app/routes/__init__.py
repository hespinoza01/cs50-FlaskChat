from flask import Blueprint


routes = Blueprint('routes', __name__, template_folder='views')

from . import index
from . import login
