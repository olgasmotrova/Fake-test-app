from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, search_for_posts, get_posts_by_user, get_comments_by_post_id, get_post_by_pk

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:uid>")
def post_page(uid):
    comments = get_comments_by_post_id(uid)
    post = get_post_by_pk(uid)
    return render_template('post.html', comments=comments, post=post)


@app.route("/search/")
def search_page():
    search_by = request.args['s']
    if search_by:
        posts = search_for_posts(search_by)[0:10]
        if posts:
            return render_template('search.html', search_by=search_by, posts=posts)


@app.route("/users/<username>/")
def feed_page(username):
    user_feed = get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_feed)


@app.route("/api/posts")
def index_test():
    posts = get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = get_post_by_pk(uid)
    return jsonify(post)


if __name__ == "__main__":
    app.run(port=7030)
