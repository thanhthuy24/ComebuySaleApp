from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app import db, app


#tạo class trong gói enum
# class UserRoleEnum(enum.Enum):
#     ADMIN = 1,
#     USER = 2

# class User(db.Model, UserMixin):
#     id = Column(Integer, primary_key=True, autoincrement=True),
#     name = Column(String(100), nullable=False, unique=True),
#     username = Column(String(100), nullable=False, unique=True),
#     password = Column(String(100), nullable=False)
#
#     #user thường đăng kí
#     user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
#
#     #ghi đè
#     def __str__(self):
#         return self.name
class Category(db.Model): #db.Model là kế thừa
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    # tạo mối quan hệ vs product => đặt product trong nháy để khi máy dịch,
    # chạy qua product bên dưới rồi mới nhận biết product bên trong relationship'product'
    # products = relationship('Product', backref='category', lazy=True)

    # def __str__(self):
    #     return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Float, default=8)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    image = Column(String(200))


    # def __str__(self):
    #     return self.name

if __name__ == '__main__':
    with app.app_context():

        db.create_all()

        # c1 = Category(name='Trà Sữa')
        # c2 = Category(name='Trà Tươi')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        #
        p1 = Product(name='Trà sữa Signature', price='53000', category_id=1,
                     image="https://product.hstatic.net/200000421745/product/ts_signature_da473adc7fcc4d1d8c4d6378adc1f114_large.png")

        p2 = Product(name='Lục trà hoàng kim', price='53000', category_id=1,
                     image="https://product.hstatic.net/200000421745/product/luc_tra_hoang_kim_4b2ef28d7cc04db0a47c0587e05f8963_large.png")

        p3 = Product(name='Trà sữa hải thần', price='59000', category_id=1,
                     image="https://product.hstatic.net/200000421745/product/ts_hai_than_66599a9e451c47a9a637b41d0289d21c_large.png")

        p4 = Product(name='Trà hải thần', price='55000', category_id=2,
                     image="https://product.hstatic.net/200000421745/product/tra_hai_than_6c17ef2fee4d4472ac5c8f082654d9f1_large.png")

        p5 = Product(name='Trà Hoa Hồng Pu’re', price='59000', category_id=2,
                     image="https://product.hstatic.net/200000421745/product/tra_hoa_hong_b8ff8585af4d4ee0b2e932ef5ce29704_large.png")

        p6 = Product(name='Trà Oolong Đào Mật Ong', price='55000', category_id=2,
                     image="https://product.hstatic.net/200000421745/product/tra_oolong_dao_mat_ong_6c76ab8ce2714626aebd4c4ba6083414_large.png")

        p7 = Product(name='Trà Hoa Quế Tứ Quý Xuân', price='62000', category_id=2,
                     image="https://product.hstatic.net/200000421745/product/tra_hoa_que_tu_quy_xuan_1680a739763141fb854e63cb44bf1076_large.png")

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7])
        db.session.commit()

