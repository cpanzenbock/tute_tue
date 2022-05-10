from flask import Blueprint, render_template, redirect, url_for, request
from .forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Successfully logged in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=form, heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Successfully registered')
        return redirect(url_for('auth.register'))
    return render_template('user.html', form=form)
