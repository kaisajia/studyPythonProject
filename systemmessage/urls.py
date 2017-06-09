from django.conf.urls import url
from .view import message_list
from .view import message_read

urlpatterns=[
    url(r'^list',message_list),
    url(r'^read',message_read), 
]


