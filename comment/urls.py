from django.conf.urls import url
from .view import create_comment

urlpatterns=[
    url(r'^create/',create_comment), 
]
