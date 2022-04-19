from run import app


keys = keys_posts = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_all_data_json():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, 'Ошибка типа данных'
    assert set(response.json[0].keys()) == keys, 'Ошибка ключей'


def test_api_by_id():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict, 'Ошибка типа данных'
    assert set(response.json.keys()) == keys, 'Ошибка ключей'