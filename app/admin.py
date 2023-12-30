from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product, UserRoleEnum
from app import app, db
from flask_login import current_user, logout_user
from flask import redirect

admin = Admin(app=app, name='QUẢN LÝ BÁN HÀNG', template_mode='bootstrap4')

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyProductView(AuthenticatedAdmin):
    column_list = ['id','name','price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price','name']
    column_editable_list = ['name', 'price']
    edit_modal = True

class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name','products']

class MyStatsView(BaseView):
    @expose('/') #nạp domain nối đuôi tiếp
    def index(self):
        return self.render('admin/stats.html')

class MyLogoutView(AuthenticatedUser):
    @expose("/") #nạp domain nối đuôi tiếp
    def index(self):
        logout_user()
        return redirect('/')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
admin.add_view(MyLogoutView(name='Đăng xuất'))