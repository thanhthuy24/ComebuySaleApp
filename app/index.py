from flask import render_template, request
from app import app
import dao
@app.route('/') #can co cau lenh from App import app moi su dung duoc
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    pros = dao.get_products(kw)
    return render_template('index.html', categories = cates, products = pros)


if __name__ == '__main__':
    app.run(debug=True) #khai bao debug=True de chay kiem tra loi debug duoc