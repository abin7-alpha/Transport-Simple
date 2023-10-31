from django.urls import path

from bulletin.api.comment_to_post import create_comment
from bulletin.api.create_post import create_post
from bulletin.api.get_all_posts import get_all_the_posts
from bulletin.api.like_to_post import like_post

urlpatterns = [
    path('get-all-posts', get_all_the_posts, name='get_all_posts'),
    path('create-post', create_post, name='create_post'),
    path('like-post', like_post, name='like_post'),
    path('comment-to-post', create_comment, name='create_comment'),
]
