from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.sign_in, name='login'),
    url(r'^logout/$',views.log_out, name='logout'),
    url(r'^create_user/$', views.RegisterNewUser, name='registration'),
]
