from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Interest(models.Model):
    name = models.CharField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    posts = models.ManyToManyField('Post', related_name='posts', blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
       

    def __str__(self):
        return self.body[0:50]



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Interest, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
       

