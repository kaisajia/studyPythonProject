import views
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import urls

 

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^accounts/',include('django.contrib.auth.urls')), 
    url(r'^article/',include('article.urls')),
    url(r'^register/',include('user.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^comment/',include('comment.urls')),
    url(r'^$',views.index),
]
