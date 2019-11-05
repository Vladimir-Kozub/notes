from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^del/(?P<del_id>[-\w]+)$', views.del_entry, name='del_entry'),
]