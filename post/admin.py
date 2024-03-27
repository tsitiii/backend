from django.contrib import admin
from . import models


admin.site.register(models.Post)
admin.site.register(models.Comments)
admin.site.register(models.Report)
admin.site.register(models.PostImages)
admin.site.register(models.CommentImage)
