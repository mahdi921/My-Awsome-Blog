from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.name} - {self.subject}'