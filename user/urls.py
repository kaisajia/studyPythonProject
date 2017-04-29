 
from django.conf.urls import url
from django.contrib import admin
from .view import register
from .view import register_success 

urlpatterns = [
    url(r'^register_success',register_success),
    url(r'^$',register),
    
]