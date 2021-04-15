from flask import Flask, render_template, request
from post import Post
import requests
from smtplib import SMTP

API_ENDPOINT = 'https://api.npoint.io/43644ec4f0013682fc0d'

app = Flask(__name__)

def fetch_post(url):
    post_list = []
    response = requests.get(url).json()
    for item in response:
        post = Post(item['id'], item['body'], item['date'], item['title'],
                    item['author'], item['subtitle'], item['image_url'])
        post_list.append(post)
    return post_list

def send_email(name, email, phone, message):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="megawone735@gmail.com", password="775596731")
        connection.sendmail(from_addr="megawone735@gmail.com", to_addrs="mamadouwone12345@gmail.com",
                            msg="Subject:Want to Contact You\n\n"
                                f"Name: {name}\n Email: {email} \n Phone: {phone}\n Message: {message}"
                            )

@app.route('/')
def home():
    post_list = fetch_post(API_ENDPOINT)
    return render_template('index.html', all_post=post_list)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    msg_send = "Contact me!"
    return render_template('contact.html', msg_send=msg_send)

@app.route('/post/<post_id>')
def post(post_id):
    post_list = fetch_post(API_ENDPOINT)
    return render_template('post.html', post_id=int(post_id), all_post=post_list)


@app.route('/form-entry', methods=['POST', 'GET'])
def receive_data():
    error = None
    msg_send = None
    if request.method == 'POST':
        send_email(request.form["name"], request.form["email"], request.form["phone"], request.form["message"])
        msg_send = "Message Send SuccessFull"
        return render_template('contact.html', msg_send=msg_send)
    msg_send = "Error"
    return render_template('contact.html', msg_send=msg_send)

if __name__ == '__main__':
    app.run(debug=True)