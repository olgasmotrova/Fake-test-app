
from app import app


def tests_api_posts(posts_keys):
    """Проверяем что
    - возвращается список
    - у элементов есть нужные ключи"""
    response = app.test_client().get('api/posts')
    posts = response.json
    assert isinstance(posts, list), "Есть ошибка получения поста: выгружается не список"
    assert set(posts[0].keys()) == posts_keys, "Ошибка получения ключей"


def test_api_posts_by_id(posts_keys):
    """Проверяем что
    - возвращается словарь
    - у элемента есть нужные ключи"""
    response = app.test_client().get('api/posts/1')
    post = response.json
    assert isinstance(post, dict), "Есть ошибка получения поста по ID: выгружается не словарь"
    assert set(post.keys()) == posts_keys, "Ошибка получения ключей при загрузке ID"


