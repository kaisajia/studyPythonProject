from django.conf.urls import url

from .view import article_list
from .view import publish_article
from .view import ArticleCreate
from .view import article_detail
from .view import ArticleDetailView
from django.contrib.auth.decorators import login_required



urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
    #url(r'^(?P<b_id>\d+)/publish_article',publish_article),
    #url(r'^(?P<block_id>\d+)/publish_article',ArticleCreate.as_view()),
    url(r'^(?P<block_id>\d+)/publish_article',login_required(ArticleCreate.as_view())),
    url(r'^(?P<block_id>\d+)/article_detail/(?P<aid>\d+)',article_detail),
    #url(r'^(?P<block_id>\d+)/article_detail/(?P<aid>\d+)',login_required(ArticleDetailView.as_view())),
]




