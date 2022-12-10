from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Post, Connection

class FollowList(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'list.html'

  def get_queryset(self):
      my_connection = Connection.objects.get_or_create(user=self.request.user)
      all_follow = my_connection[0].following.all()
      return Post.objects.filter(user__in=all_follow)

  def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['connection'] = Connection.objects.get_or_create(user=self.request.user)
      return context

class FollowBase(LoginRequiredMixin, View):
   def get(self, request, *args, **kwargs):
       pk = self.kwargs['pk']
       target_user = Post.objects.get(pk=pk).user
       my_connection = Connection.objects.get_or_create(user=self.request.user)

       if target_user in my_connection[0].following.all():
           obj = my_connection[0].following.remove(target_user)
       else:
           obj = my_connection[0].following.add(target_user)
       return obj

class FollowHome(FollowBase):
   def get(self, request, *args, **kwargs):
       super().get(request, *args, **kwargs)
       return redirect('home')

class FollowDetail(FollowBase):
   def get(self, request, *args, **kwargs):
       super().get(request, *args, **kwargs)
       pk = self.kwargs['pk'] 
       return redirect('detail', pk)

class LikeBase(LoginRequiredMixin, View):
   def get(self, request, *args, **kwargs):
       pk = self.kwargs['pk']
       related_post = Post.objects.get(pk=pk)
       
       if self.request.user in related_post.like.all(): 
           obj = related_post.like.remove(self.request.user)
       else:                         
           obj = related_post.like.add(self.request.user)  
       return obj


class LikeHome(LikeBase):
   def get(self, request, *args, **kwargs):
       super().get(request, *args, **kwargs)
       return redirect('home')


class LikeDetail(LikeBase):
   def get(self, request, *args, **kwargs):
       super().get(request, *args, **kwargs)
       pk = self.kwargs['pk'] 
       return redirect('detail', pk)
     
     

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   template_name = 'delete.html'
   success_url = reverse_lazy('mypost')

   def test_func(self, **kwargs):
       pk = self.kwargs["pk"]
       post = Post.objects.get(pk=pk)
       return (post.user == self.request.user) 

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