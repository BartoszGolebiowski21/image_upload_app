from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Tier(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="images", null=True)
    name = models.CharField(max_length=50)
    thumbnail_200 = models.ImageField(upload_to='thumbnails/200/', null=True, blank=True)
    thumbnail_400 = models.ImageField(upload_to='thumbnails/400/', null=True, blank=True)
    file_with_expiring_link = models.ImageField(upload_to="images/expiring", blank=True, null=True)
    link_expiration_seconds = models.IntegerField(validators=[MinValueValidator(300), 
        MaxValueValidator(30000),], null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} uploaded by {self.user}"
    
@receiver(pre_delete, sender=Image)
def delete_image_files(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

    if instance.thumbnail_200:
        if os.path.isfile(instance.thumbnail_200.path):
            os.remove(instance.thumbnail_200.path)

    if instance.thumbnail_400:
        if os.path.isfile(instance.thumbnail_400.path):
            os.remove(instance.thumbnail_400.path)


class UserTierAssociation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s tier: {self.tier.name}"
