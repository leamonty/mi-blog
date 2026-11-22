
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'blog/post_form.html'

    def test_func(self):
        return self.get_object().autor == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        return self.get_object().autor == self.request.user
