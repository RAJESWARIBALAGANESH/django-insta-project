from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, SocialMediaComment
from .serializers import PostSerializer, SocialMediaCommentSerializer

# --------- Post Views ---------

class PostListCreateView(APIView):
    """
    API view to list all posts or create a new post.
    """
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    """
    API view to retrieve a single post by ID.
    """
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post)
        return Response(serializer.data)

# --------- Comment Views ---------

class SocialMediaCommentCreateView(APIView):
    """
    Create a new social media comment.
    """
    def post(self, request):
        serializer = SocialMediaCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SocialMediaCommentListView(APIView):
    """
    Retrieve all social media comments.
    """
    def get(self, request):
        comments = SocialMediaComment.objects.all().order_by('-created_at')
        serializer = SocialMediaCommentSerializer(comments, many=True)
        return Response(serializer.data)

class SocialMediaCommentDetailView(APIView):
    """
    Retrieve a single comment by ID.
    """
    def get(self, request, pk):
        try:
            comment = SocialMediaComment.objects.get(pk=pk)
        except SocialMediaComment.DoesNotExist:
            return Response({'detail': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SocialMediaCommentSerializer(comment)
        return Response(serializer.data)
