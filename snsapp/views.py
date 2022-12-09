from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Post

class Home(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'list.html'
  
  def get_queryset(self):
    return Post.objects.exclude(user=self.request.user)
  
class MyPost(LoginRequiredMixin, ListView):
   """自分の投稿のみ表示"""
   model = Post
   template_name = 'list.html'

   def get_queryset(self):
       return Post.objects.filter(user=self.request.user)