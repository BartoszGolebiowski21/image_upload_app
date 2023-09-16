from django.shortcuts import render

from .models import User, UserTierAssociation

def user_detail(request, id):
    user = User.objects.get(id=id)
    user_tier_association = UserTierAssociation.objects.get(user=user)

    context = {
        "user": user,
        "images": user.image_set.all(),
        "tier": user_tier_association.tier if user_tier_association else None,
    }
    return render(request, 'image_upload_app/user_detail.html', context)
