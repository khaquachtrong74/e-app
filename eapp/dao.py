from eapp.models import Category, Product

def get_categories():
    return Category.query.all()
def get_products(kw=None, category_id=None):
    products = Product.query
    if kw:
        products = products.filter(Product.name==kw)
    if category_id:
        products = products.filter(Product.category_id.contains(category_id))
    return products.all()