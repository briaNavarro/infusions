from django.db import models
from apps.login_app.models import User

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=25)
    about = models.TextField()
    active = models.CharField(max_length=3)
    age = models.IntegerField()
    kreator = models.ForeignKey(
        User, related_name='user_prof', on_delete=models.CASCADE)


class InfuseLog(models.Model):
    date = models.DateField()
    time = models.TimeField()
    desc = models.TextField()
    bleed = models.CharField(max_length=3)
    dose_amount = models.CharField(max_length=100)
    dose_onHand = models.IntegerField()
    kreator = models.ForeignKey(
        User, related_name='user_logs', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.kreator.first_name}, {self.id}'


class MessageBoard(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kreator = models.ForeignKey(
        User, related_name='user_msg', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='like_message')

    def __str__(self):
        return f'{self.kreator}, {self.id}'


class Comment(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kreator = models.ForeignKey(
        User, related_name='user_comments', on_delete=models.CASCADE)
    msg_kreator = models.ForeignKey(
        MessageBoard, related_name='msgboard_comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.kreator}, {self.id}'


class Meta:
    ordering = {'id', }
