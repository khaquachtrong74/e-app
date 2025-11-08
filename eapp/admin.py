import typing as t

from flask import session
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from werkzeug.utils import redirect

from eapp.models import Category, Product, USER_ROLE
from eapp import app, db
from flask_admin import Admin, BaseView, expose

class AuthenticatedView(ModelView):
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role == USER_ROLE.ADMIN
class ProductView(AuthenticatedView):
    page_size = 3
    can_export = True
    column_list = ['id', 'name', 'description', 'price', 'category_id']
    column_filters = ['id', 'name', 'price']
    edit_template = ['name']
    column_editable_list = ['name']
    column_searchable_list = ['name', 'id', 'category_id']
    edit_modal = True
class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self) -> bool:
        return current_user.is_authenticated
class AboutUs(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/about_us.html')

admin = Admin(app=app, name='e-app_ADMIN')
admin.add_view(AuthenticatedView(Category, session= db.session))
admin.add_view(ProductView(model=Product, session=db.session))
# admin.add_view(AboutUs(name='Giowis thieu'))
admin.add_view(LogoutView(name='Đăng xuất'))