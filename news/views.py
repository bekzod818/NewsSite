from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class NewsListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    posts = Post.published.all()
    content = {'post': post, 'posts': posts}
    return render(request, 'detail.html', content)


class PostCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'slug', 'cat', 'author', 'photo', 'body', 'status']
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'photo', 'body']
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list')
