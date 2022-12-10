from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('mypost/', views.MyPost.as_view(), name='mypost'),
    path('detail/<int:pk>', views.DetailPost.as_view(), name='detail'),
    path('create/', CreatePost.as_view(), name='create'), 
]
