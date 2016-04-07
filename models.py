from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class State(db.Model):
    __tablename__ = 'state'

    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(120), nullable=False, unique=True)
    tax_percent = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))

    def __init__(self, state_name, tax_percent):
        self.state_name = state_name
        self.tax_percent = tax_percent


class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))

    def __init__(self, product_name):
        self.product_name = product_name


class Seller(db.Model):
    __tablename__ = 'seller'

    seller_id = db.Column(db.Integer, primary_key=True)
    seller_name = db.Column(db.String(120), nullable=False, unique=True)
    state_id = db.Column(db.ForeignKey(u'state.state_id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))

    state = db.relationship(u'State')

    def __init__(self, seller_name, state_id):
        self.seller_name = seller_name
        self.state_id = state_id


class Buyer(db.Model):
    __tablename__ = 'buyer'

    buyer_id = db.Column(db.Integer, primary_key=True)
    buyer_name = db.Column(db.String(120), nullable=False, unique=True)
    state_id = db.Column(db.ForeignKey(u'state.state_id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))

    state = db.relationship(u'State')

    def __init__(self, buyer_name, state_id):
        self.buyer_name = buyer_name
        self.state_id = state_id


class Selling(db.Model):
    __tablename__ = 'selling'

    selling_id = db.Column(db.Integer, primary_key=True, nullable=False)
    seller_id = db.Column(db.ForeignKey(u'seller.seller_id'), nullable=False, index=True)
    product_id = db.Column(db.ForeignKey(u'product.product_id'), nullable=False, index=True)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))

    seller = db.relationship(u'Seller')
    product = db.relationship(u'Product')

    def __init__(self, seller_id, product_id, price):
        self.seller_id = seller_id
        self.product_id = product_id
        self.price = price
