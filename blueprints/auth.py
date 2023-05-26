from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('login')
def login():
    pass
