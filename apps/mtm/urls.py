from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_form$', views.add_form),
    url(r'^add$', views.add),
    url(r'^show/(?P<id>\d+)$', views.show)
]
