from flask import Blueprint, render_template
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id
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