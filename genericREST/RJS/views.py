from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from RJS.models import Image, LinkedDescriptor
from rest_framework import viewsets
from rest_framework import permissions
from RJS.serializers import ImageSerializer, DescriptorSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

class DescriptorViewSet(viewsets.ModelViewSet):
    queryset = LinkedDescriptor.objects.all()
    serializer_class = DescriptorSerializer
    permission_classes = [permissions.IsAuthenticated]


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("placeholder")