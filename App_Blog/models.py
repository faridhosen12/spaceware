from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post-author')
    blog-title = models.CharField(max_length=264, verbose_name='put a title')
    slug = models.SlugField(max_length=264,unique=True)
    blog-content = models.TextField(verbose_name='what is your mind?')
    blog-image = models.ImageField(upload-to='blog-image',verbose_name='image')
    publish-date = models.DateTimeField(auto_now_add= True)
    update-date = models.DateTimeField(auto_now=True)


def __def__(self):
    return self.blog_title

class comment(models.Model):
    Blog=models.ForeignKey(blog,on_delete= models.CASCADE,related_name='blog-comment')
    User=models.ForeignKey(User,on_delete= models.CASCADE,related_name='user-comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.comment

class likes(models.Model):
    blog =models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    User= models.ForeignKey(User,on_delete=models,CASCADE,related_name='liker_user')
