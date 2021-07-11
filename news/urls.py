from django.urls import path
from .views import NewsListView, post_detail, PostCreateView, PostUpdateView, PostDeleteView, IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="home"),
    path('blog/', NewsListView.as_view(), name='post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name="post_detail"),
    path('blog/create/', PostCreateView.as_view(), name="post_new"),
    path('blog/<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete")
]
