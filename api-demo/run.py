from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    inventoryStatus = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f"<Product(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, "
                f"category='{self.category}', quantity={self.quantity}, inventoryStatus='{self.inventoryStatus}', "
                f"rating={self.rating})>")

# Get all products
@app.route('/get_all_details', methods=['GET'])
def get_all_details():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'code': product.code,
        'name': product.name,
        'description': product.description,
        'image': product.image,
        'price': product.price,
        'category': product.category,
        'quantity': product.quantity,
        'inventoryStatus': product.inventoryStatus,
        'rating': product.rating
    } for product in products]), 200

# Add a new product
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    if type(data) != list:
        new_product = Product(
        code=data['code'],
        name=data['name'],
        description=data['description'],
        image=data['image'],
        price=data['price'],
        category=data['category'],
        quantity=data['quantity'],
        inventoryStatus=data['inventoryStatus'],
        rating=data['rating']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({
            'message': 'Product added',
            'product': {
            'id': new_product.id,
            'code': new_product.code,
            'name': new_product.name,
            'description': new_product.description,
            'image': new_product.image,
            'price': new_product.price,
            'category': new_product.category,
            'quantity': new_product.quantity,
            'inventoryStatus': new_product.inventoryStatus,
            'rating': new_product.rating
        }
        }), 201
    else:
        for items in data:
            print('----->')
            new_product = Product(
            code=items['code'],
            name=items['name'],
            description=items['description'],
            image=items['image'],
            price=items['price'],
            category=items['category'],
            quantity=items['quantity'],
            inventoryStatus=items['inventoryStatus'],
            rating=items['rating']
            )
            db.session.add(new_product)
            db.session.commit()
        return jsonify({
                'message': 'Product added',
                'product': {
                'id': new_product.id,
                'code': new_product.code,
                'name': new_product.name,
                'description': new_product.description,
                'image': new_product.image,
                'price': new_product.price,
                'category': new_product.category,
                'quantity': new_product.quantity,
                'inventoryStatus': new_product.inventoryStatus,
                'rating': new_product.rating
            }
            }), 201


@app.route('/update_product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    
    product.code = data.get('code', product.code)
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.image = data.get('image', product.image)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)
    product.quantity = data.get('quantity', product.quantity)
    product.inventoryStatus = data.get('inventoryStatus', product.inventoryStatus)
    product.rating = data.get('rating', product.rating)
    
    db.session.commit()
    return jsonify({
        'message': 'Product updated',
        'product': {
            'id': product.id,
            'code': product.code,
            'name': product.name,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'category': product.category,
            'quantity': product.quantity,
            'inventoryStatus': product.inventoryStatus,
            'rating': product.rating
        }
    }), 200

# Delete a product
@app.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
