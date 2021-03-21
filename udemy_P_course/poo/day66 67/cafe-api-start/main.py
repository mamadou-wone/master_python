from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_choice = random.choice(cafes)
    return jsonify(
        cafes={
            "can_lake_call":random_choice.can_take_calls,
            "coffee_price":random_choice.coffee_price,
            "has_sockets":random_choice.has_sockets,
            "has_wifi":random_choice.has_wifi,
            "id": random_choice.id,
            "Img_url": random_choice.img_url,
            "Location": random_choice.location,
            "map_url": random_choice.map_url,
            "name": random_choice.name,
            "seats":random_choice.seats
        }
    )

@app.route('/all')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_dict = {
                "can_lake_call": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
                "has_sockets": cafe.has_sockets,
                "has_wifi": cafe.has_wifi,
                "id": cafe.id,
                "Img_url": cafe.img_url,
                "Location": cafe.location,
                "map_url": cafe.map_url,
                "name": cafe.name,
                "seats": cafe.seats
            }
        cafe_list.append(cafe_dict)
    return jsonify(
        cafes=[item for item in cafe_list]
    )


@app.route('/search')
def search():
    # cafes = db.session.query(Cafe).all()
    location = None
    cafe = None

    location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=location).all()
    if cafes:
        # print(cafes)
        cafe_list = []
        for cafe in cafes:
            cafe_dict = {
                "can_lake_call": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
                "has_sockets": cafe.has_sockets,
                "has_wifi": cafe.has_wifi,
                "id": cafe.id,
                "Img_url": cafe.img_url,
                "Location": cafe.location,
                "map_url": cafe.map_url,
                "name": cafe.name,
                "seats": cafe.seats
            }
            cafe_list.append(cafe_dict)
        return jsonify(cafes=[cafe for cafe in cafe_list])
    else:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
