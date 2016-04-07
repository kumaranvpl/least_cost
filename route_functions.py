import json
from flask import jsonify, request
from db_operations import StateOperations, ProductOperations, SellerOperations
from db_operations import BuyerOperations, SellingOperations

with open('config.json') as conf_file:
    config = json.load(conf_file)


def create_return_msg(status, msg, additional_msg=None):
    status_dict = {
        "status": status,
        "message": msg
    }
    if additional_msg is not None:
        status_dict.update(additional_msg)
    return status_dict


def add_state():
    state_name = request.values.get('state_name')
    tax_percent = request.values.get('tax_percent')
    try:
        state_ops = StateOperations()
        state_ops.create(state_name, tax_percent)
        return jsonify(create_return_msg("ok", "State created"))
    except Exception as e:
        return jsonify(create_return_msg("error", "State creation failed", {"exception": "Internal Server Error"}))


def find_all_states():
    try:
        state_ops = StateOperations()
        states_dict = state_ops.find_all()
        return states_dict
    except Exception as e:
        return jsonify(create_return_msg("error", "Finding all states failed", {"exception": "Internal Server Error"}))


def add_product():
    product_name = request.values.get('product_name')
    try:
        product_ops = ProductOperations()
        product_ops.create(product_name)
        return jsonify(create_return_msg("ok", "Product created"))
    except Exception as e:
        return jsonify(create_return_msg("error", "Product creation failed", {"exception": "Internal Server Error"}))


def find_all_products():
    try:
        product_ops = ProductOperations()
        products_dict = product_ops.find_all()
        return products_dict
    except Exception as e:
        return jsonify(
            create_return_msg("error", "Finding all products failed", {"exception": "Internal Server Error"})
        )


def add_seller():
    seller_name = request.values.get('seller_name')
    state_id = request.values.get('state_id')
    try:
        seller_ops = SellerOperations()
        seller_ops.create(seller_name, state_id)
        return jsonify(create_return_msg("ok", "Seller created"))
    except Exception as e:
        return jsonify(create_return_msg("error", "Seller creation failed", {"exception": "Internal Server Error"}))


def find_all_sellers():
    try:
        seller_ops = SellerOperations()
        sellers_dict = seller_ops.find_all()
        return sellers_dict
    except Exception as e:
        return jsonify(
            create_return_msg("error", "Finding all sellers failed", {"exception": "Internal Server Error"})
        )


def add_buyer():
    buyer_name = request.values.get('buyer_name')
    state_id = request.values.get('state_id')
    try:
        buyer_ops = BuyerOperations()
        buyer_ops.create(buyer_name, state_id)
        return jsonify(create_return_msg("ok", "Buyer created"))
    except Exception as e:
        return jsonify(create_return_msg("error", "Buyer creation failed", {"exception": "Internal Server Error"}))


def find_all_buyers():
    try:
        buyer_ops = BuyerOperations()
        buyers_dict = buyer_ops.find_all()
        return buyers_dict
    except Exception as e:
        return jsonify(
            create_return_msg("error", "Finding all buyers failed", {"exception": "Internal Server Error"})
        )


def add_selling():
    seller_id = request.values.get('seller_id')
    product_id = request.values.get('product_id')
    price = request.values.get('price')
    try:
        selling_ops = SellingOperations()
        selling_ops.create(seller_id, product_id, price)
        return jsonify(create_return_msg("ok", "Selling entry created"))
    except Exception as e:
        return jsonify(
            create_return_msg("error", "Selling entry creation failed", {"exception": "Internal Server Error"}))
