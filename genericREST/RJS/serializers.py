from django.contrib.auth.models import User, Group
from RJS.models import Image, LinkedDescriptor
from rest_framework import serializers

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    descriptors = serializers.HyperlinkedRelatedField(
        many = True,
        queryset = LinkedDescriptor.objects.all(),
        read_only = False,
        view_name = 'descriptor-detail'
    )
    class Meta:
        model = Image
        fields = ['url', 'imageUrl', 'descriptors']

class DescriptorSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'image-detail'
    )
    class Meta:
        model = LinkedDescriptor
        fields = ['url', 'name', 'images']

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']