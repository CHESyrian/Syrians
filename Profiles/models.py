from django.db import models
from django.contrib.auth.models import User
from My_Account.models import Sharing_Post, Sharing_Image


class Posts_Good( models.Model ):
    Post      = models.ForeignKey(Sharing_Post, on_delete=models.CASCADE, null=True)
    username  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Good_Date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Post.id, self.username.username


class Posts_Amazing( models.Model ):
    Post         = models.ForeignKey(Sharing_Post, on_delete=models.CASCADE, null=True)
    username     = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Amazing_Date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Post.id, self.username.username


class Posts_Shares(models.Model):
    Post       = models.ForeignKey(Sharing_Post, on_delete=models.CASCADE, null=True)
    username   = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Share_Date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Post.id, self.username.username