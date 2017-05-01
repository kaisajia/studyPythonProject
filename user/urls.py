 
from django.conf.urls import url
from django.contrib import admin
from .view import register
from .view import register_success
from .view import user_logout

urlpatterns = [
    url(r'^register_success',register_success),
    url(r'^user_logout',user_logout),
    url(r'^$',register),
]