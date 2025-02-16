from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['POST'])
def login(request):
  user = get_object_or_404(User, username=request.data['username'])

  if not user.check_password(request.data['password']):
    return Response({'error': 'incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
  
  token, created = Token.objects.get_or_create(user=user)
  serializer = UserSerializer(instance=user)

  return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()  # Ya guarda la contraseña encriptada
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def profile(request):
  print(request.user)
  serializer = UserSerializer(instance=request.user)

  return Response(serializer.data, status=status.HTTP_200_OK)