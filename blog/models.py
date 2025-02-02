from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default='blog/assets/img/blog/default.jpg')
    counted_views = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    tag = TaggableManager()
    login_required = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.title} - {self.id}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blog:single", kwargs={"pid": self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255, blank=True, default='-empty-')
    message = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.name} - {self.post}'