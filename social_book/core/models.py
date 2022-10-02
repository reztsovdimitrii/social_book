import uuid
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images',
        default='blank-profile-picture.png'
    )
    location = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    create_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.id)


class LikePost(models.Model):
    post_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='like_post'
    )
    username = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='like_post'
    )

    def __str__(self) -> str:
        return str(self.username)
