from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^add$', views.add),
url(r'^add_this$', views.add_this),
url(r'^logout$', views.logout),
url(r'^(?P<id>\d+)$', views.book),
url(r'/users/(?P<id>\d+)$', views.users),
url(r'/add_review$', views.add_review)
]