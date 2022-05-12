import json

POST_PATH = 'data/posts.json'
COMM_PATH = 'data/comments.json'


def get_posts_all():
    """ Возвращает посты"""
    with open(POST_PATH, 'r', encoding='utf8') as f:
        posts = json.load(f)
        return posts


def get_posts_by_user(username):
    """ Возвращает посты определенного пользователя"""
    with open(POST_PATH, 'r', encoding='utf8') as f:
        user_data = json.load(f)
    return [posts for posts in user_data if username.lower() in posts['poster_name'].lower()]


def get_comments_by_post_id(post_id):
    """ Возвращает комментарии определенного поста"""
    with open(COMM_PATH, 'r', encoding='utf8') as f:
        comments = json.load(f)
        comments_by_id = []
        for comment in comments:
            if post_id == comment['post_id']:
                comments_by_id.append(comment)
    return comments_by_id


def search_for_posts(query):
    """ Возвращает список постов по ключевому слову"""
    post_list = get_posts_all()
    posts_list = []
    for post in post_list:
        if query.lower() in post['content'].lower():
            posts_list.append(post)
    return posts_list


def get_post_by_pk(pk):
    """ Возвращает пост по его идентификатору"""
    user_data = get_posts_all()
    for poster in user_data:
        if poster['pk'] == pk:
            return poster
