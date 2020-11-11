
from django.db import models
from django.contrib.auth.models import User


class Profile_Model(models.Model):
    username       = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    User_Name      = models.CharField(max_length=120, null=True)
    Friends        = models.IntegerField(default=0)
    Followers      = models.IntegerField(default=0)
    First_Name     = models.CharField(max_length=120, null=True)
    Last_Name      = models.CharField(max_length=120, null=True)
    Address        = models.CharField(max_length=120, null=True)
    Job            = models.CharField(max_length=120, null=True)
    Bio            = models.TextField(default='BIO', max_length=80)
    Number_Phone   = models.CharField(max_length=16, null=True)
    Profile_Image  = models.ImageField(upload_to='users_profiles/profiles_images/',
                        default='users_profiles/profiles_images/default_profile_image.jpg')
    Cover_Image    = models.ImageField(upload_to='users_profiles/covers_images/',
                        default='users_profiles/covers_images/default_cover_image.jpg')
    Editable       = models.BooleanField(default=True)

    def __str__(self):
        return self.username.username

class User_Accounts(models.Model):
    username       = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Facebook_Link  = models.CharField(max_length=160, default='')
    Twitter_Link   = models.CharField(max_length=160, default='')
    Youtube_Link   = models.CharField(max_length=160, default='')
    LinkedIn_Link  = models.CharField(max_length=160, default='')
    Instagram_Link = models.CharField(max_length=160, default='')
    Github_Link    = models.CharField(max_length=160, default='')
    Kaggle_Link    = models.CharField(max_length=160, default='')
    Codepen_Link   = models.CharField(max_length=160, default='')

    def __str__(self):
        return self.username.username


class Sharing_Post(models.Model):
    username    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Post        = models.TextField()
    Font_Color  = models.CharField(max_length=10, default='white')
    Font_Size   = models.IntegerField(default=18)
    BG_Color    = models.CharField(max_length=10, default='rgba(10, 10, 10, .5)')
    Good_Num    = models.IntegerField(default=0)
    Amazing_Num = models.IntegerField(default=0)
    Stars_Num   = models.IntegerField(default=0)
    Post_Date   = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.username.username


class Sharing_Image(models.Model):
    username    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Image       = models.ImageField(upload_to='users_profiles/uploads_images/', null=True)
    Image_Text  = models.TextField(null=True)
    Good_Num    = models.IntegerField(default=0)
    Amazing_Num = models.IntegerField(default=0)
    Stars_Num   = models.IntegerField(default=0)
    Image_Date  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.username.username


class Notifications(models.Model):
    username            = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Notification_Type   = models.CharField(max_length=64)
    Notification_Text   = models.CharField(max_length=240)
    Notification_Status = models.CharField(max_length=32)

    def __str__(self):
        return self.username.username


class Followers(models.Model):
    username  = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Username')
    Follower  = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Follower')
    is_Friend = models.BooleanField(default=False)

    def __str__(self):
        return self.username.username

class Stars_Votes(models.Model):
    Star = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Star')
    Vote = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='Vote')

    def __str__(self):
        return self.Star.username
