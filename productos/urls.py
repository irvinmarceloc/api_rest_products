from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('products', views.product_list, name='product-list'),
    path('products/<int:pk>', views.product_detail, name='product-detail'),
    path('products/edit/<int:pk>', views.edit_product, name='edit-product'),  
    path('products/delete/<int:pk>', views.delete_product, name='delete-product'),
    path('products/create', views.create_product, name='create-product'),  
    path('login', views.MyTokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('register', views.register),
]

