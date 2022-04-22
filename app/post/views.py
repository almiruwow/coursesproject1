from flask import Blueprint, render_template, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/')
def home_page():
    data = get_posts_all()
    return render_template('index.html', data=data)


@post_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    data = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=data, comments=comments)


@post_blueprint.route('/search/')
def search_post():
    s = request.args.get('s')
    if s:
        search_posts = search_for_posts(s)
        return render_template('search.html', searches=search_posts)

    return render_template('search.html')


@post_blueprint.route('/users/<user_name>')
def search_user(user_name):
    users = get_posts_by_user(user_name)
    return render_template('user-feed.html', users=users)