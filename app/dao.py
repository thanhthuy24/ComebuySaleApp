from app.models import Category, Product
# #
# #
def get_categories():
    return Category.query.all()
def get_products(kw=None): #, cate_id, page=None
    products = Product.query
    if kw:
        # products = [p for p in products if p['name'].find(kw) >= 0]
        products = products.filter(Product.name.contains(kw))

    # if cate_id:
    #     products = products.filter(Product.category_id.__eq__(cate_id))

    return products.all()