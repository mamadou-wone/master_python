from flask import Flask, render_template
from post import Post
import requests

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


@app.route('/')
def home():
    post_list = fetch_post(API_ENDPOINT)
    return render_template('index.html', all_post=post_list)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<post_id>')
def post(post_id):
    post_list = fetch_post(API_ENDPOINT)
    return render_template('post.html', post_id=int(post_id), all_post=post_list)



if __name__ == '__main__':
    app.run(debug=True)