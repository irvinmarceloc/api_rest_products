from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Producto
from .serializers import ProductoSerializer, ProductoSinAuthSerializer, CategoriaSerializer, MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication




@api_view(['GET'])
def product_list(request):
    products = Producto.objects.all()
    serializer = ProductoSinAuthSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    try:
        product = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(product)
        return Response(serializer.data)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# register
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new user
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    return Response("new user born")

 #login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
