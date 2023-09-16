from django.db import models
from django.contrib.auth.models import User


class Tier(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    thumbnail_sizes = models.TextField()
    original_link = models.BooleanField(default=False)
    expiring_link = models.BooleanField(default=False)
    link_expiration_seconds = models.IntegerField(default=3600)

    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="images", blank=True, null=True)
    name = models.CharField(max_length=50)
    thumbnail_200 = models.ImageField(upload_to='thumbnails/200/', null=True, blank=True)
    thumbnail_200_link = models.URLField(null=True, blank=True)
    thumbnail_400 = models.ImageField(upload_to='thumbnails/400/', null=True, blank=True)
    thumbnail_400_link = models.URLField(null=True, blank=True)
    original_link = models.URLField(null=True, blank=True)
    expiring_link = models.URLField(null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} uploaded by {self.user}"


class UserTierAssociation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s plan: {self.tier.name}"
