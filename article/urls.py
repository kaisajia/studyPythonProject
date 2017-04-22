from django.conf.urls import url

from .view import article_list
from .view import publish_article


urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
    url(r'^(?P<b_id>\d+)/publish_article',publish_article),
]




