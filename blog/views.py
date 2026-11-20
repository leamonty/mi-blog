from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.select_related('autor').all()
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.select_related('autor').all()
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
