from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.email