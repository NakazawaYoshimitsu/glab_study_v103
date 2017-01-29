from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myadmin/$', views.myadmin, name='myadmin'),
    url(r'^redilect/$', views.redilect, name='redilect'),
]


