from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=20000)
    puplish_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True,null=True)
    auther_id = models.IntegerField()


    def __save__(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)


    def __str__(self) -> str:
        return self.title

class PostLike(models.Model):
    post = models.ForeignKey(Post,related_name="post_likes",on_delete=models.CASCADE)
    user_id = models.IntegerField()

    def __str__(self) -> str:
        return str(self.post)
    


class Comment(models.Model):
    user_id = models.IntegerField()
    post = models.ForeignKey(Post,related_name="comment_post",on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    comment_data = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return str(self.post)