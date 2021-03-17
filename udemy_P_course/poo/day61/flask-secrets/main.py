from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from email_validator import validate_email, EmailNotValidError
from flask_bootstrap import Bootstrap

EMAIL = 'admin@email.com'
PASSWORD = '12345678'
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             validators.Email(message="Enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=8)])

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "Maimouna WONE"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        if form.email.data == EMAIL and form.password.data == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)