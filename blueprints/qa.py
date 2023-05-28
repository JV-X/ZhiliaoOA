from flask import Blueprint,request,render_template

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'Hello World!'


@bp.route('qa/public', methods=['GET', "POST"])
def public_qa():
    if request.method == 'GET':
        return render_template('public_question.html')
