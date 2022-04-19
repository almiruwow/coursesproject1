import pytest
from utils import *


@pytest.fixture()
def json_for_test():
    return load_posts_json


keys_posts = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
keys_comment = {"post_id", "commenter_name", "comment", "pk"}


def test_get_all(json_for_test):
    assert type(get_posts_all()) == list, 'Ошибка типа данных'


def test_get_posts_by_user(json_for_test):
    user = get_posts_by_user('leo')
    assert type(user) == list, 'Ошибка типа данных'
    assert user[0]['poster_name'] == 'leo', 'Ошибка имени'
    assert set(user[0].keys()) == keys_posts, 'Ошибка ключей'


def test_comments(json_for_test):
    comment = get_comments_by_post_id(1)
    assert set(comment[0].keys()) == keys_comment, 'Ошибка ключей'


def test_search_for_posts(json_for_test):
    search_word = search_for_posts("еда")
    assert set(search_word[0].keys()) == keys_posts, ''
    assert 'еда' in search_word[0]['content'].lower(), ''


def test_get_post_by_pk(json_for_test):
    by_pk = get_post_by_pk(1)
    assert by_pk['pk'] == 1, ''
    assert type(by_pk) == dict, ''

