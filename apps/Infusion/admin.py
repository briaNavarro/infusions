from django.contrib import admin

from .models import InfuseLog, MessageBoard, Comment
# Register your models here.

admin.site.register(InfuseLog)
admin.site.register(MessageBoard)
admin.site.register(Comment)
