from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^registration$', views.registration),
    url(r'^dashboard$', views.dashboard),
    url(r'^quote$', views.quote),
    url(r'^editAccount$', views.editAccount),
    url(r'^edit$', views.edit),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^liked$', views.liked),
    url(r'^delete$', views.delete),
    url(r'^update$', views.update),
]