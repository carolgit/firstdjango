
from django.conf.urls import url
from .views import post_list

urlpatterns = [
    url('list/', post_list)
]