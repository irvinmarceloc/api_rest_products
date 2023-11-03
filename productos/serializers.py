from rest_framework import serializers
from .models import Producto, Categoria
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProductoSinAuthSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=200)
    estado = serializers.CharField(max_length=50)

    def to_representation(self, instance):
        return {
            'nombre': instance.nombre,
            'estado': instance.estado,
        }

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
 
        return token
