from django.db import models


# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_desc = models.TextField(max_length=1000)
    profile_pic = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Appeal(models.Model):
    appeal_title = models.CharField(max_length=100)
    appeal_desc = models.TextField(max_length=1000)
    appeal_pic = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.appeal_title


class Sponsor(models.Model):
    sponsor_title = models.CharField(max_length=100)
    sponsor_desc = models.TextField(max_length=1000)
    sponsor_pic = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sponsor_title


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_desc = models.TextField(max_length=1000)
    event_pic = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_title


class Gallery(models.Model):
    image_desc = models.TextField(max_length=200)
    image_pic = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_desc
