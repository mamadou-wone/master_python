from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired, URL
import csv
import pandas

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    coffee_list = ["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    wifi_list = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    power_list = ["✘", '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    wifi = SelectField('Wifi', validators=[DataRequired()], choices=[(item, item) for item in wifi_list])
    coffee = SelectField('Cafe', validators=[DataRequired()], choices=[(item, item) for item in coffee_list])
    power = SelectField('Power', validators=[DataRequired()], choices=[(item, item) for item in power_list])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

def add_new_item(name, location, openH, close, coffee, wifi, power):
    new_item = f"{name},{location},{openH},{close},{coffee},{wifi},{power}"
    with open('test.csv', 'a', encoding='utf-8') as file:
        file.write(new_item+'\n')

@app.route('/add',  methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.is_submitted():
        add_new_item(form.cafe.data, form.location.data, form.open.data,
                     form.close.data, form.coffee.data, form.wifi.data, form.power.data)
        # print(form.cafe.data)
        # print(form.location.data)
        # print(form.open.data)
        # print(form.close.data)
        # print(form.wifi.data)
        # print(form.coffee.data)
        # print(form.power.data)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    content = pandas.read_csv("cafe-data.csv")
    data = content.to_dict()
    list = []
    for item in data:
        list.append(data[item])
    return render_template('cafes.html', cafes=data, dict_list=list)


if __name__ == '__main__':
    app.run(debug=True)
