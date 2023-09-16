from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer, UserSerializer, TierSerializer
from image_upload_app.models import Image, User, Tier


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/images/'},
        {'GET': 'api/images/id'},
        {'GET': 'api/users/'},
        {'GET': 'api/users/id'},
    ]
    return Response(routes)


# IMAGES

@api_view(['GET'])
def get_images(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_image(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImageSerializer(image, many=False)
    return Response(serializer.data)


# USERS

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# TIERS

@api_view(['GET'])
def get_tiers(request):
    tiers = Tier.objects.all()
    serializer = TierSerializer(tiers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_tier(request, pk):
    tier = Tier.objects.get(id=pk)
    serializer = TierSerializer(tier, many=False)
    return Response(serializer.data)