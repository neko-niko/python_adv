from django.conf.urls import url
from test1 import views

urlpatterns = [
    url(r'^lgzp/(?P<id1>[0-9]+)$', views.lgzp, name='lgzp'),
    
]