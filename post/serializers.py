from rest_framework import serializers
from .models import Post, PostImages, Comments, CommentImage, Report

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'