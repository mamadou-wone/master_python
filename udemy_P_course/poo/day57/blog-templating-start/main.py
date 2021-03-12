from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
response = requests.get(url=blog_url).json()
post_list = []
for item in response:
    post = Post(item['id'], item['title'], item['subtitle'], item['body'])
    post_list.append(post)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_list)

@app.route("/post/<post_id>")
def read_post(post_id):
    return render_template("post.html", post_id=int(post_id), all_posts=post_list)




if __name__ == "__main__":
    app.run(debug=True)
