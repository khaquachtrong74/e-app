from flask import render_template, request, redirect

from eapp import app, login, dao


@app.route('/')
def index():
    return render_template('index.html',
                           categories=dao.get_categories(),
                           products=dao.get_products(kw=request.args.get('kw'), category_id=request.args.get('category_id')))
from flask_login import login_user
@app.route("/login-admin", methods=['post'])
def login_admin():
    username = request.form.get('username')
    password = request.form.get('password')
    u = dao.get_user_authenticated(username, password)
    if u:
        login_user(user=u)
    return redirect('/admin')

@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

if __name__ == '__main__':
    from admin import admin
    app.run(debug=True)
