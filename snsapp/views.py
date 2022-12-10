from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Post

class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model =Post
  template_name = 'update.html'
  fields = ['title', 'content']
  
  def get_success_url(self, **kwargs):
    pk = self.kwargs["pk"]
    return reverse_lazy('detail', kwargs={"pk": pk})
  
  def test_func(self, **kwargs):
       pk = self.kwargs["pk"]
       post = Post.objects.get(pk=pk)
       return (post.user == self.request.user) 
  
  

class CreatePost(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'create.html'
  fields = ['title', 'content']
  success_url = reverse_lazy('mypost')
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
    

class DetailPost(LoginRequiredMixin, DetailView):
  model = Post
  template_name = 'detail.html'

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