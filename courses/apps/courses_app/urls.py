from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^add$', views.add),
url(r'^courses/(?P<id>\d+)/destroy$', views.confirm),
url(r'^courses/(?P<id>\d+)/destroy_confirm$', views.really_destroy)
]