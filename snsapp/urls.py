from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('mypost/', views.MyPost.as_view(), name='mypost'),
    path('detail/<int:pk>', views.DetailPost.as_view(), name='detail'),
    path('detail/<int:pk>/update', views.UpdatePost.as_view(), name='update'),
    path('detail/<int:pk>/delete', views.DeletePost.as_view(), name='delete'),
    path('create/', views.CreatePost.as_view(), name='create'), 
]
