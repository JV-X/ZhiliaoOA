import random
import string

from flask import Blueprint, render_template, request, jsonify
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def login():
    pass


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = ''.join(captcha)
    message = Message(subject='ZhiliaoOA验证码', recipients=[email], body=f'您的验证码是{captcha}')
    mail.send(message)

    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({'code': 200, 'message': '', 'data': None})
