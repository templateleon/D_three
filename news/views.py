#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'details_news.html' 
    context_object_name = 'new_s'
    queryset = Post.objects.filter(type='NW')

