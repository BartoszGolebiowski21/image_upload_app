from rest_framework import serializers
from image_upload_app.models import Image, User, Tier


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Image
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    tier = TierSerializer(source='usertierassociation.tier', many=False)
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'

    def get_images(self, obj):
        images = obj.image_set.all()
        serializer = ImageSerializer(images, many=True)
        return serializer.data
