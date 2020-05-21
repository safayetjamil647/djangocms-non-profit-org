from django.db import models


# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_desc = models.TextField(max_length=1000)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.blog_title

