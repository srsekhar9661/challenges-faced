from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('mapping', views.view1, name='view1'),
    path('1/', views.view2, name='view2'),
    path('new/', views.new, name='new'),
    path('narrative/', views.NarrativeView.as_view(), name='narrative-crud'),
    path('narrative/<int:pk>/', views.NarrativeView.as_view(), name='narrative-crud-with-pk'),
    path('upload-file/', FileUploadView.as_view(), name='upload-file'),
]   