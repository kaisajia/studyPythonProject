import views
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^article/',include('article.urls')),
    url(r'^$',views.index),
]
