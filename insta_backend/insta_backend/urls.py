from django.urls import path
from comments.views import (
    PostListCreateView,
    PostDetailView,
    SocialMediaCommentCreateView,
    SocialMediaCommentListView,
    SocialMediaCommentDetailView,
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', SocialMediaCommentListView.as_view(), name='comment-list'),
    path('comments/new/', SocialMediaCommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', SocialMediaCommentDetailView.as_view(), name='comment-detail'),
]
