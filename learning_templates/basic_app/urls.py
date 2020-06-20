from django.conf.urls import url
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^info/$', views.info, name='info'),
    url(r'^other/$', views.other, name='other'),
]
