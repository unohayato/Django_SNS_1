from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('mypost/', views.MyPost.as_view(), name='mypost'),
    path('detail/<int:pk>', views.DetailPost.as_view(), name='detail'),
    path('detail/<int:pk>/update', views.UpdatePost.as_view(), name='update'),
    path('detail/<int:pk>/delete', views.DeletePost.as_view(), name='delete'),
    path('create/', views.CreatePost.as_view(), name='create'), 
    
    path('like-home/<int:pk>', views.LikeHome.as_view(), name='like-home'),
    path('like-detail/<int:pk>', views.LikeDetail.as_view(), name='like-detail'),
    path('follow-home/<int:pk>', views.FollowHome.as_view(), name='follow-home'),
    path('follow-detail/<int:pk>', views.FollowDetail.as_view(), name='follow-detail'),
    path('follow-list/', views.FollowList.as_view(), name='follow-list'),
    
]
