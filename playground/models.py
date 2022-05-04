from django.db import models

class Category(models.Model):
    category_id = models.TextField()
    category = models.TextField()

class Country(models.Model):
    country_name = models.TextField()
    country_code = models.TextField()

class Video(models.Model):
    video_id = models.TextField()
    title = models.TextField()
    published_at = models.TextField()
    channel_id = models.TextField() 
    country_code = models.TextField()
    thumbnail_link = models.TextField()
    category_id = models.TextField()

class Ytchannel(models.Model):
    channel_id = models.TextField()
    channel_title = models.TextField()

class Ytviews(models.Model):
    video_id = models.TextField()
    channel_id = models.TextField()
    trending_date = models.TextField()
    view_count = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    comment_count = models.IntegerField()
    comments_disabled = models.BooleanField()
    ratings_disabled = models.BooleanField()