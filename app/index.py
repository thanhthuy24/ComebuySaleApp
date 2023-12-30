import math

from flask import render_template, request, redirect, jsonify, session
from app import app, login
import dao, utils
from flask_login import login_user, logout_user

@app.route('/') #can co cau lenh from App import app moi su dung duoc
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    num = dao.count_product()

    cates = dao.get_categories()
    pros = dao.get_products(kw, cate_id, page)
    return render_template('index.html', categories=cates, products=pros,
                           pages=math.ceil(num/app.config['PAGE_SIZE']))

@app.route('/admin/login', methods=['post'])
def admin_login():
    usename = request.form.get('username')
    password =  request.form.get('password')

    user = dao.authe_user(username=usename, password=password)

    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route("/api/cart", methods=['post'])
def add_to_cart():
    '''
    {
        "cart":{
            "1": {
                "id": 1,
                "name":"abc",
                "price":123,
                "quantity":2
            },
            "2": {
                "id": 2,
                "name":"abc",
                "price":123,
                "quantity":1
                }
        }
    }

    :return:
    '''

    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get('id'))
    if id in cart: #sp co trong gio roi
        cart[id]['quantity'] += 1
    else: #sp chua co trong gio
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart
    print(cart)

    return jsonify(utils.count_cart(cart))

@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart: #kiem tra key product_id co trong cart khong
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart: #kiem tra key product_id co trong cart khong
        del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route("/login", methods=['get', 'post'])
def process_user_login():
    if request.method.__eq__('POST'):
        usename = request.form.get('username')
        password = request.form.get('password')

        user = dao.authe_user(username=usename, password=password)

        if user:
            login_user(user=user)
            #lay tren duong dan ve thi dung => .args
            next = request.args.get('next')

            return redirect('/' if next is None else next)

    return render_template('login.html')


@app.route('/logout')
def process_user_logout():
    logout_user()
    return redirect('/login')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.context_processor
def common_responese():
    return {
        'categories':dao.get_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


if __name__ == '__main__':
    from app import admin
    app.run(debug=True) #khai bao debug=True de chay kiem tra loi debug duoc