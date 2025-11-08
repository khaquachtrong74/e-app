from eapp.models import Category, Product, User, USER_ROLE
import hashlib
def get_categories():
    return Category.query.all()
def get_products(kw=None, category_id=None):
    products = Product.query
    if kw:
        products = products.filter(Product.name==kw)
    if category_id:
        products = products.filter(Product.category_id.contains(category_id))
    return products.all()

def get_user_by_id(id):
    return User.query.get(id)

def get_user_authenticated(username, password : str):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.user_name == username.strip(),
                             User.password == password).first()