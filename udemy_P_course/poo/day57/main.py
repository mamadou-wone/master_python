from flask import Flask, render_template
import random
from datetime import datetime
import requests
app = Flask(__name__)




@app.route('/')
def hello():
    date = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=date)


@app.route('/guess/<name>')
def guess(name):
    gender_api = "https://api.genderize.io/"
    age_api = "https://api.agify.io/"
    param = {
        'name': f"{name}"
    }
    gender_response = requests.get(gender_api, params=param).json()['gender']
    age_response = requests.get(age_api, params=param).json()['age']
    return render_template("guess.html", name=name, gender=gender_response, age=age_response)


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url).json()
    return render_template("blog.html", posts=response)

if __name__ == '__main__':
    app.run(debug=True)
