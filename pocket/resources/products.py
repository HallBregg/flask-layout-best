from flask import request
from flask_restplus import Resource

from pocket import ma, db, api


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

    def save(self):
        db.session.add(self)
        db.session.commit()


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@api.route('/product')
class ProductView(Resource):
    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        new_product = Product(name, description, price, qty)
        return product_schema.jsonify(new_product)
