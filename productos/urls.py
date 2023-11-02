from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('products', views.product_list, name='product-list'),
    path('products/<int:pk>', views.product_detail, name='product-detail'),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('register', views.register),
]

