
"""
from django.urls import path
from .views import ( PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView )
from .views import post_detail_view, CommentUpdateView, CommentDeleteView
from .views import post_list_view, posts_by_tag



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path("post/<slug:slug>/", post_detail_view, name="post_detail"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("", post_list_view, name="post_list"),
    path("tag/<slug:tag_slug>/", posts_by_tag, name="posts_by_tag"),
]

"""