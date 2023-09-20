from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ImageSerializer, UserSerializer, TierSerializer
from image_upload_app.models import Image, User, Tier, UserTierAssociation
from rest_framework import status

from .utilities import generate_thumbnail



@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/images/'},
        {'GET': 'api/images/id'},
        {'GET': 'api/users/'},
        {'GET': 'api/users/id'},
        {'GET': 'api/users/token/'},
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_image(request):
    """
    Uploads an image with additional features based on the user's tier.

    This view allows authenticated users to upload images with different capabilities depending on their tier.
    
    Args:
        request (HttpRequest): The HTTP request object containing the image data and user information.

    Returns:
        Response: A JSON response containing the uploaded image's details.
        
    Raises:
        BadRequest: If the request is missing required parameters.
        
    Permissions:
        - User must be authenticated.

    """
    user = request.user

    name = request.data.get('name')
    if not name:
        return Response({"error": "No 'name' in the request"}, status=status.HTTP_400_BAD_REQUEST)
    
    file = request.data.get('file')
    if not file:
        return Response({"error": "No 'file' in the request"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_tier_association = UserTierAssociation.objects.get(user=user)
        user_tier = user_tier_association.tier
    except UserTierAssociation.DoesNotExist:
        user_tier = None

    if user_tier.name == 'Basic':
        thumbnail_200 = generate_thumbnail(file, 200)
        image = Image(
            user=user,
            name=name,
            thumbnail_200=thumbnail_200,
        )
        image.save()

    elif user_tier.name == 'Premium':
        thumbnail_200 = generate_thumbnail(file, 200)
        thumbnail_400 = generate_thumbnail(file, 400)
        image = Image(
            user=user,
            name=name,
            file=file,
            thumbnail_200=thumbnail_200,
            thumbnail_400=thumbnail_400
        )
        image.save()

    elif user_tier.name == 'Enterprise':
        file_with_expiring_link = file
        
        seconds = request.data.get('link_expiration_seconds')
        if not seconds:
            return Response({"error": "No 'link_expiration_seconds' in the request"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        link_expiration_seconds = int(seconds)

        thumbnail_200 = generate_thumbnail(file, 200)
        thumbnail_400 = generate_thumbnail(file, 400)
        image = Image(
            user=user,
            name=name,
            file=file,
            thumbnail_200=thumbnail_200,
            thumbnail_400=thumbnail_400,
            link_expiration_seconds=link_expiration_seconds,
            file_with_expiring_link=file_with_expiring_link
        )
        image.save()

    serializer = ImageSerializer(image)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



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

