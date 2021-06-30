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

    def create(self, validated_data):
        descriptors_data = validated_data.pop('descriptors')
        image = Image.objects.create(**validated_data)
        descriptors_existing = LinkedDescriptor.objects.all()
        for descriptor_data in descriptors_data:
            if descriptors_existing.filter(name=descriptor_data.name).exists():
                LinkedDescriptor.objects.create(**descriptor_data)
        return image

    def update(self, instance, validated_data):
        instance.imageUrl = validated_data.get('imageUrl', instance.imageUrl)
        descriptors_data = validated_data.pop('descriptors')
        descriptors_existing = LinkedDescriptor.objects.all()
        for descriptor_data in descriptors_data:
            if descriptors_existing.filter(name=descriptor_data.name).exists():
                LinkedDescriptor.objects.create(**descriptor_data)
        instance.descriptors = validated_data.get(descriptors_data, instance.descriptors)


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