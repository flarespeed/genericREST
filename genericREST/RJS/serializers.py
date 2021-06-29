from django.contrib.auth.models import User, Group
from RJS.models import Image, LinkedDescriptor
from rest_framework import serializers

class NonRecursiveDescriptorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkedDescriptor
        fields = ['url', 'name', 'images']
        extra_kwargs = {'images': {'required': False}}

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    descriptors = NonRecursiveDescriptorSerializer(many=True, read_only=True)
    class Meta:
        model = Image
        fields = ['url', 'imageUrl', 'descriptors']
        extra_kwargs = {'descriptors': {'required': False}}

class DescriptorSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = LinkedDescriptor
        fields = ['url', 'name', 'images']
        extra_kwargs = {'images': {'required': False}}

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