from rest_framework import viewsets
from .serializers import UsersSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

'''
class UsersViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UsersSerializer
'''

class UsersViewSet(APIView):
  def get(self, request, format=None):
    user = User.objects.all()
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)
  def post(self, request, format=None):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

