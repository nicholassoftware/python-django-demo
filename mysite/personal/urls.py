from django.conf.urls import url, include
from . import views

#urlpatterns = [
 #   url(r'^$', views.index, name='index')
#]
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact')
    #url(r'^blog/$', views.blog, name='blog')
]
