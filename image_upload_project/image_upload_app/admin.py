from django.contrib import admin

from .models import Tier, Image, UserTierAssociation

# Register your models here.

admin.site.register(Tier)
admin.site.register(Image)
admin.site.register(UserTierAssociation)