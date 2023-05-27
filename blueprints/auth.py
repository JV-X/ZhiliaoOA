import random
import string

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel, UserModel
from .form import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print('邮箱不存在！')
                return redirect(url_for('auth.login'))
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect('/')
            else:
                print('密码错误')
                return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.register'))


@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = ''.join(captcha)
    # 应该用celery来发送
    message = Message(subject='ZhiliaoOA验证码', recipients=[email], body=f'您的验证码是{captcha}')
    mail.send(message)

    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({'code': 200, 'message': '', 'data': None})
