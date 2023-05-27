from flask import Blueprint,render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('login')
def login():
    pass

@bp.route('register')
def register():
    return render_template('register.html')