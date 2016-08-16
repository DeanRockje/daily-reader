from django.conf.urls import url
from .views import (FeedAPI,CategoryAPI, FeedAPIdetailed,
                    EntryAPIdetailed, CategoryAPIdetailed, UserAPI)

urlpatterns = [
    url(r'^feeds/$', FeedAPI.as_view()),
    url(r'^feeds/(?P<pk>\d+)/$', FeedAPIdetailed.as_view()),
    url(r'^category/$',CategoryAPI.as_view()),
    url(r'^category/(?P<pk>\d+)/$', CategoryAPIdetailed.as_view()),
    url(r'^feeds/entry/(?P<pk>\d+)/$', EntryAPIdetailed.as_view()),
    url(r'^users/$', UserAPI.as_view()),
]
