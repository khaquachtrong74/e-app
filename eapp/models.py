from eapp import db, app
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as UserEnum
from flask_login import UserMixin
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class USER_ROLE(UserEnum):
    USER = 1
    ADMIN = 2
class User(BaseModel, UserMixin):
    name = Column(String(100), nullable=False)
    avatar = Column(String(100))
    user_name = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    user_role = Column(Enum(USER_ROLE), default=USER_ROLE.USER)
    def __str__(self):
        return self.name

class Category(BaseModel):
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(BaseModel):
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg')
    category_id= Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name
if __name__ == '__main__':
    import hashlib
    with app.app_context():
        categories = ['Máy tính bảng', 'Điện thoại', 'Robot']
        products = [{
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        },
            {
                "name": "iPhone 7 Plus",
                "description": "Apple, 32GB, RAM: 3GB, iOS13",
                "price": 17000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
                "category_id": 1
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            },
            {
                "name": "iPhone 7 Plus",
                "description": "Apple, 32GB, RAM: 3GB, iOS13",
                "price": 17000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
                "category_id": 1
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }
        ]
        db.create_all()
        # for cate in categories:
        #     c = Category(name=cate)
        #     db.session.add(c)

        # for p in products:
        #     o = Product(**p)
        #     db.session.add(o)

        # user = User(name='admin',
        #             avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
        #             user_name='admin',
        #             password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #             user_role = USER_ROLE.ADMIN)
        # db.session.add(user)
        db.session.commit()