from django.urls import path
from .views import NewsListView, post_detail, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name="post_detail"),
    path('create/', PostCreateView.as_view(), name="post_new"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete")
]
