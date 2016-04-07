from models import db, State,Product, Seller, Buyer, Selling


class StateOperations:
    @classmethod
    def create(self, state_name, tax_percent):
        state = State(state_name=state_name, tax_percent=tax_percent)
        db.session.add(state)
        db.session.commit()

    @classmethod
    def find(self, state_id):
        state = State.query.filter_by(state_id=state_id).first()
        state_dict = {
            'state_id': state.state_id,
            'state_name': state.state_name,
            'tax_percent': state.tax_percent
        }
        return state_dict

    @classmethod
    def find_all(self):
        states = State.query.all()
        states_dict = {}
        for state in states:
            states_dict[state.state_id] = state.state_name
        return states_dict


class ProductOperations:
    @classmethod
    def create(self, product_name):
        product = Product(product_name=product_name)
        db.session.add(product)
        db.session.commit()

    @classmethod
    def find(self, product_id):
        product = Product.query.filter_by(product_id=product_id).first()
        product_dict = {
            'product_id': product.product_id,
            'product_name': product.product_name
        }
        return product_dict

    @classmethod
    def find_all(self):
        products = Product.query.all()
        products_dict = {}
        for product in products:
            products_dict[product.product_id] = product.product_name
        return products_dict


class SellerOperations:
    @classmethod
    def create(self, seller_name, state_id):
        seller = Seller(seller_name=seller_name, state_id=state_id)
        db.session.add(seller)
        db.session.commit()

    @classmethod
    def find(self, seller_id):
        seller = Seller.query.filter_by(seller_id=seller_id).first()
        seller_dict = {
            'seller_id': seller.seller_id,
            'seller_name': seller.seller_name,
            'state_id': seller.state_id
        }
        return seller_dict

    @classmethod
    def find_all(self):
        sellers = Seller.query.all()
        sellers_dict = {}
        for seller in sellers:
            sellers_dict[seller.seller_id] = seller.seller_name
        return sellers_dict


class BuyerOperations:
    @classmethod
    def create(self, buyer_name, state_id):
        buyer = Buyer(buyer_name=buyer_name, state_id=state_id)
        db.session.add(buyer)
        db.session.commit()

    @classmethod
    def find(self, buyer_id):
        buyer = Buyer.query.filter_by(buyer_id=buyer_id).first()
        buyer_dict = {
            'buyer_id': buyer.buyer_id,
            'buyer_name': buyer.buyer_name,
            'state_id': buyer.state_id
        }
        return buyer_dict

    @classmethod
    def find_all(self):
        buyers = Buyer.query.all()
        buyers_dict = {}
        for buyer in buyers:
            buyers_dict[buyer.buyer_id] = buyer.buyer_name
        return buyers_dict


class SellingOperations:
    @classmethod
    def create(self, seller_id, product_id, price):
        selling = Selling(seller_id=seller_id, product_id=product_id, price=price)
        db.session.add(selling)
        db.session.commit()

    @classmethod
    def find(self, selling_id):
        selling = Selling.query.filter_by(selling_id=selling_id).first()
        selling_dict = {
            'selling_id': selling.selling_id,
            'seller_id': selling.seller_id,
            'product_id': selling.product_id,
            'price': selling.price
        }
        return selling_dict
