from django.conf.urls import url
from . import views

urlpatterns = [
    url('check/', views.check, name='check'),
]