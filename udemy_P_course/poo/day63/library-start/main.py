from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Books %r>' % self.title


all_books = []


@app.route('/')
def home():
    global all_books
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    # global all_books
    if request.method == "POST":
        new_book = {
            "title": request.form['title'],
            "author": request.form['author'],
            "rating":  request.form['rating']
        }
        db.create_all()
        # book = Books(title=new_book['title'], author=new_book['author'], rating=new_book['rating'])
        # db.session.add(book)
        # db.session.add(book2)
        db.session.commit()
        query = Books.query.all()
        # print(query)
        # print(type(query))
        for item in query:
            all_books.append(item)
        print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

