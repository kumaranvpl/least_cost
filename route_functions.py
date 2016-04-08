from __future__ import division
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


def calculate_price_with_tax(total, seller_state_id, buyer_state_id=None):
    seller_state_dict = find_state(seller_state_id)
    buyer_state_dict = {}
    if buyer_state_id is None:
        buyer_state_dict['tax_percent'] = 0
    else:
        buyer_state_dict = find_state(buyer_state_id)
    tot_percent = seller_state_dict['tax_percent'] + buyer_state_dict['tax_percent']
    final_price = ((total/100)*tot_percent) + total
    return final_price


def add_state():
    state_name = request.values.get('state_name')
    tax_percent = request.values.get('tax_percent')
    try:
        state_ops = StateOperations()
        state_ops.create(state_name, tax_percent)
        return jsonify(create_return_msg("ok", "State created"))
    except Exception as e:
        return jsonify(create_return_msg("error", "State creation failed", {"exception": "Internal Server Error"}))


def find_state(state_id):
    try:
        state_ops = StateOperations()
        state_dict = state_ops.find(state_id)
        return state_dict
    except Exception as e:
        return False


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


def find_product(product_id):
    try:
        product_ops = ProductOperations()
        product_dict = product_ops.find(product_id)
        return product_dict
    except Exception as e:
        return False


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


def find_seller(seller_id):
    try:
        seller_ops = SellerOperations()
        seller_dict = seller_ops.find(seller_id)
        return seller_dict
    except Exception as e:
        return False


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


def find_buyer(buyer_id):
    try:
        buyer_ops = BuyerOperations()
        buyer_dict = buyer_ops.find(buyer_id)
        return buyer_dict
    except Exception as e:
        return False


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
            create_return_msg("error", "Selling entry creation failed", {"exception": "Internal Server Error"})
        )


def calculate_least_cost():
    buyer_id = request.values.get('buyer_id')
    product_id = request.values.get('product_id')
    try:
        buyer_dict = find_buyer(buyer_id)
        if not buyer_dict:
            return jsonify(
                create_return_msg("ok", "Selected buyer not found", {"exception": "Internal Server Error"})
            )
        selling_ops = SellingOperations()
        sellings_lst = selling_ops.find_by_product(product_id)
        if not sellings_lst:
            return jsonify(
                create_return_msg("ok", "Selected Product is not available", {"exception": "Internal Server Error"})
            )
        min_price = None
        for selling in sellings_lst:
            seller_dict = find_seller(selling['seller_id'])
            if not seller_dict:
                continue
            if buyer_dict['state_id'] == seller_dict['state_id']:
                sel_price = calculate_price_with_tax(selling['price'], seller_dict['state_id'])
            else:
                sel_price = calculate_price_with_tax(selling['price'], seller_dict['state_id'], buyer_dict['state_id'])
            if min_price is None or sel_price < min_price:
                min_selling = selling
                min_seller_dict = seller_dict
                min_price = sel_price
        product_dict = find_product(min_selling['product_id'])
        seller_state_dict = find_state(min_seller_dict['state_id'])
        buyer_state_dict = find_state(buyer_dict['state_id'])
        if seller_state_dict['state_id'] == buyer_state_dict['state_id']:
            tot_percent = seller_state_dict['tax_percent']
        else:
            tot_percent = seller_state_dict['tax_percent'] + buyer_state_dict['tax_percent']
        least_cost_dict = {
            'least_cost_with_tax': min_price,
            'seller_id': min_seller_dict['seller_id'],
            'seller_name': min_seller_dict['seller_name'],
            'baseprice_without_tax': min_selling['price'],
            'product_id': product_dict['product_id'],
            'product_name': product_dict['product_name'],
            'seller_state_id': seller_state_dict['state_id'],
            'seller_state_name': seller_state_dict['state_name'],
            'seller_state_tax_percent': seller_state_dict['tax_percent'],
            'buyer_id': buyer_dict['buyer_id'],
            'buyer_name': buyer_dict['buyer_name'],
            'buyer_state_id': buyer_state_dict['state_id'],
            'buyer_state_name': buyer_state_dict['state_name'],
            'buyer_state_tax_percent': buyer_state_dict['tax_percent'],
            'total_tax_percent': tot_percent
        }
        return jsonify(create_return_msg("ok", "least cost found", least_cost_dict))
    except Exception as e:
        return jsonify(
            create_return_msg("error", "Calculating least cost failed", {"exception": "Internal Server Error"})
        )
