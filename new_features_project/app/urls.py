from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.template_list, name='template_list'),
    path('templates/<int:pk>/', views.template_detail, name='template_detail'),
    path('templates/create/', views.create_template, name='create_template'),
    path('templates/<int:pk>/edit/', views.update_template, name='update_template'),
]
