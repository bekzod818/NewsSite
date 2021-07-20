from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Category, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView
from .forms import CommentForm


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'index.html'


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


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'slug', 'cat', 'photo', 'body', 'status']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user super user ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'body', 'photo']
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 style="text-align:center;">Bunday sahifa topilmadi (404)</h1>')
