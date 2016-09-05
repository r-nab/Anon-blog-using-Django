from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^blog/post_(?P<post_id>[0-9]+)/$', views.details, name='details'),
    url(r'^blog/$', views.all_posts, name='all_post'),
    url(r'^blog/create/$', views.create_post, name='create_post'),
]
