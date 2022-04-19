from flask import Blueprint, render_template, request
from utils import search_for_posts, get_posts_by_user

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search')
def search_post():
    s = request.args.get('s')
    if s:
        search_posts = search_for_posts(s)
        return render_template('search.html', searches=search_posts)

    return render_template('search.html')


@search_blueprint.route('/users/<user_name>')
def search_user(user_name):
    users = get_posts_by_user(user_name)
    return render_template('user-feed.html', users=users)
