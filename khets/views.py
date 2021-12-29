from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User

class PostListView(ListView):
    model=Post
    template_name='khets/home.html'
    context_object_name='posts'
    ordering=['-Date']
    paginate_by=4

class UserPostListView(ListView):
    model=Post
    template_name='khets/user_post.html'
    context_object_name='posts'
    paginate_by=4
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-Date')

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['name','content','address']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['name','content','address']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url = '/khet/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False