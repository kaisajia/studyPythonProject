from django.conf.urls import url

from .view import article_list

urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
]




