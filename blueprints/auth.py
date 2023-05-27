from flask import Blueprint,render_template
from exts import mail
from flask_mail import Message

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def login():
    pass

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/mail/test')
def mail_test():
    message = Message(subject='测试',recipients=['xjv1195275315@qq.com'],body='测试邮件')
    mail.send(message)
    return 'success'