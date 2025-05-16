from django.urls import path, include
from .views import (
    SocialMediaCommentCreateView,
    SocialMediaCommentListView,
    SocialMediaCommentDetailView,
)

urlpatterns = [
    path('comments/', SocialMediaCommentListView.as_view(), name='comment-list'),
    path('comments/create/', SocialMediaCommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', SocialMediaCommentDetailView.as_view(), name='comment-detail'),
]
