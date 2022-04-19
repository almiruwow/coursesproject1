from flask import Blueprint, jsonify
from utils import load_posts_json, get_post_by_pk

json_blueprint = Blueprint('json_blueprint', __name__, url_prefix='/api')


@json_blueprint.route('/posts')
def json_posts():
    return jsonify(load_posts_json())


@json_blueprint.route('/posts/<int:post_id>')
def json_post(post_id):
    return jsonify(get_post_by_pk(post_id))