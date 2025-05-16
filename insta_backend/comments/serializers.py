from rest_framework import serializers
from .models import Post, SocialMediaComment

class SocialMediaCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaComment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = SocialMediaCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'comments']
