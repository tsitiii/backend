from django.db import models


class Post(models.Model):
    owener = models.CharField(max_length=126)
    name = models.CharField(max_length=126)
    slug = models.CharField(max_length=15)
    video = models.FileField(upload_to='files/videos/')
    description = models.TextField()
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class PostImages(models.Model):
    post = models.CharField(max_length=512)
    images = models.ImageField(upload_to='files/images/')
    added_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    upvote_comment = models.IntegerField()
    downvote_comment = models.IntegerField()
    comment_time = models.DateTimeField(auto_now_add=True)


class CommentImage(models.Model):
    comment_image = models.ImageField(upload_to='files/comment_images/')
    added_time = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)


class Report(models.Model):
    reported_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
