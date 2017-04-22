from django.conf.urls import url

from .view import article_list
from .view import publish_article
from .view import ArticleCreate
from .view import article_detail

urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
    #url(r'^(?P<b_id>\d+)/publish_article',publish_article),
    url(r'^(?P<block_id>\d+)/publish_article',ArticleCreate.as_view()),
    url(r'^(?P<block_id>\d+)/article_detail/(?P<aid>\d+)',article_detail),
]




