from django.urls import path
from . import views

urlpatterns = [
    path('post/<str:pk>', views.post, name='post'),
    path('', views.counter, name='counter')
]