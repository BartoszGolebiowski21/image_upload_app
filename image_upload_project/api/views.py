from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ImageSerializer, UserSerializer, TierSerializer
from image_upload_app.models import Image, User, Tier
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes

from .utilities import generate_thumbnail


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/images/'},
        {'GET': 'api/images/id'},
        {'GET': 'api/users/'},
        {'GET': 'api/users/id'},
        {'GET': 'api/tiers/'},
        {'GET': 'api/tiers/id'},
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @parser_classes([MultiPartParser, FormParser])
def upload_image(request):
    if request.method == 'POST':
        user = request.user
        name = request.data.get('name')
        file = request.data.get('file')
        image = Image(user=user, name=name, file=file)
        image.save()

        thumbnail_200 = generate_thumbnail(image, 200)
        image.thumbnail_200.save(name + "-thumbnail200.jpg", thumbnail_200)

        thumbnail_400 = generate_thumbnail(image, 200)
        image.thumbnail_400.save(name + "-thumbnail400.jpg", thumbnail_400)

        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
