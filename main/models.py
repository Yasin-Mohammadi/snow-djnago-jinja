from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass  # You can add custom fields later if needed

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio_images/')
    content = models.TextField()

    def __str__(self):
        return self.title

class Setting(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"