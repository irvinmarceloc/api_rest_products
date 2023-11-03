from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])  # Requiere autenticación y que el usuario sea del staff
def edit_product(request, pk):
    try:
        product = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({"message": "El producto no existe"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductoSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])  # Requiere autenticación y que el usuario sea del staff
def delete_product(request, pk):
    try:
        product = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response({"message": "El producto no existe"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response({"message": "Producto eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_product(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        return Response({"message": "El nombre de usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new user
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    return Response("Usuario creado con exito!!!")

 #login
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
