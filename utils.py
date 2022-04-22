import json
import pytest

def load_posts_json():
    with open('./data/data.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)
    return data_json


def load_comment_json():
    with open('./data/comments.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)
    return data_json


def get_posts_all():
    data = load_posts_json()
    return data


def get_posts_by_user(user_name):
    data = load_posts_json()
    user_posts = []
    for index in data:
        if index['poster_name'].lower() == user_name.lower():
            user_posts.append(index)
    return user_posts


def get_comments_by_post_id(post_id):
    data = load_comment_json()
    comments_id = []
    for index in data:
        if index['post_id'] == post_id:
            comments_id.append(index)
    return comments_id


def remove_from_string(string, *symbol):
    for symb in symbol:
        string = string.replace(symb , '')
    return string


def search_for_posts(query):
    data = load_posts_json()
    list_contents = []
    for index in data:
        if query.lower() in remove_from_string(index['content'].lower(), '!',".",',','-',':').split(' '):
            list_contents.append(index)
    return list_contents[:10]


def get_post_by_pk(pk):
    data = load_posts_json()
    post = None
    for index in data:
        if int(pk) == index['pk']:
            post = index
    return post

