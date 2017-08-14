from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^addwords$', views.addwords),
url(r'^clear$', views.clear)
]