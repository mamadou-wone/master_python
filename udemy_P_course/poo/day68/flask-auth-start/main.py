from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Mamadou Amir Ibn Boss WONE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

password = False
@app.route('/')
def home():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        db.create_all()
        password = generate_password_hash(password=request.form['password'],
                                          method='pbkdf2:sha256', salt_length=8)
        user = User(email=request.form['email'], password=password, name=request.form['name'])
        print(user)
        db.session.add(user)
        db.session.commit()
        return render_template("secrets.html", name=user.name)
    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    global password
    error = None
    user = None
    if request.method == "POST":
        email = request.form.get('email')
        db.create_all()
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            password = check_password_hash(pwhash=user.password, password=request.form.get('password'))
            if password:
                login_user(user)
                return render_template("secrets.html", name=current_user.name)
            else:
                return render_template("login.html")
        else:
            print("error")

@app.route('/secrets')
@login_required
def secrets():
    if password:
        return render_template("secrets.html")
    else:
        return "No cant access to this page"


@app.route('/logout')
def logout():
    pass


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
