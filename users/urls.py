from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',RedirectView.as_view(url='login'), name = 'redirect'),
    url(r'^login/$',views.sign_in, name='login'),
    url(r'^logout/$',views.log_out, name='logout'),
    url(r'^create_user/$', views.RegisterNewUser, name='registration'),
]
