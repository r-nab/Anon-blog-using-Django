from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^blog/post=(?P<post_myurl>[0-9a-zA-Z-_]+)/$', views.details, name='details'),
    url(r'^blog/$', views.all_posts, name='all_posts'),
    url(r'^blog/create/$', views.create_post, name='create_post'),
]
