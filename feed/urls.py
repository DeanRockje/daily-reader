from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category_index, name='category_index'),
    url(r'^category/(?P<pk>\d+)/$', views.feed_list, name='feed_list'),
    url(r'^feed_items/(?P<pk>\d+)/$', views.entry_list, name='entry_list'),
    url(r'^new/$', views.add_feed, name='add_feed'),
    url(r'^new/category/$',views.create_category, name='add_category'),
]
