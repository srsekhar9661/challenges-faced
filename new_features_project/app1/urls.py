from django.urls import path
from . import views

urlpatterns = [
    path('', views.view1, name='view1'),
    path('1/', views.view2, name='view2'),
]