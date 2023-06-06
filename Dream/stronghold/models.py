from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE) #The user info(First name, last name etc.)
    id_user = models.IntegerField() #unique user ID
    bio = models.TextField(blank=True) #user bio description
    profile_img = models.ImageField(upload_to='profile_images', default = 'book-icon.png') #Storage so the user can upload profile images


    def __str__(self):
        return self.user.username

class Post(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user