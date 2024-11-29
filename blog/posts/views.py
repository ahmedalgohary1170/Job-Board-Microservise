from rest_framework import generics, status
from rest_framework.response import Response

from .models import Post,PostLike,Comment
from .serializers import PostSerializer,PostLikeSerializer,CommentSerializer


class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




class PostLikeCreateAPI(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer