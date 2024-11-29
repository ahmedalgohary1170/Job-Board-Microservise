from rest_framework import serializers

from .models import Comment,Post,PostLike



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','auther_id','title','content','puplish_at','slug','likes_count','comments_count','comments']

    def get_likes_count(self,obj):
        return PostLike.objects.filter(post=obj).count()

    def get_comments_count(self,obj):
        return Comment.objects.filter(post=obj).count()
        
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'