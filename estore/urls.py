

from django.urls import path
from . import views



urlpatterns = [
    path('category', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/list', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),
    
    path('brand', views.BrandCreateView.as_view(), name='brand-create'),
    path('brand/list', views.BrandListView.as_view(), name='brand-list'),
    path('brand/<int:pk>/update', views.BrandUpdateView.as_view(), name='update-udate'),
    path('brand/<int:pk>/delete', views.BrandDeleteView.as_view(), name='brand-delete'),
    
    path('image/', views.ImageCreateView.as_view(), name='image-create'),
    path('image/list', views.ImageListView.as_view(), name='image-list'),
    path('image/<int:pk>/update', views.ImageUpdateView.as_view(), name='image-update'),
    path('image/<int:pk>/delete', views.ImageDeleteView.as_view(), name='image-delete'),
     
    
    path('product', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>', views.ProdView.as_view(), name='product-view'),
    path('product/list', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/update', views.ProductUdateView.as_view(), name='product-udate'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name='product-delete'),
    
    path('config', views.ProductConfigCreateView.as_view(), name='product-config-create'),
    path('config/list', views.ProductConfigListView.as_view(), name='product-config-list'),
    # path('config/list', views.ProductConfigListView.as_view(), name='product-config-list'),
    # path('config/list', views.ProductConfigListView.as_view(), name='product-config-list'),
    
   
    path('user/', views.UserCreateView.as_view(), name='user-register'),
    path('user/list', views.UserListView.as_view(), name='users-list'),
    # path('user/<pk:int>/update', views.UserUdateView.as_view(), name='user-update'),
    # path('user/<pk:int>/delete', views.UserDeleteView.as_view(), name='user-delete'),
    
    path('address', views.UserAddressCreateView.as_view(), name='address-create'),
    path('address/<int:pk>', views.UserAddressRetrieveView.as_view(), name='address-view'),
    path('address/list', views.UserAddressListView.as_view(), name='address-list'),
    path('address/<int:pk>/update', views.UserAddressUpdateView.as_view(), name='address-udate'),
    path('address/<int:pk>/delete', views.UserAddressDeleteView.as_view(), name='address-delete'),
    
    
    path('cart', views.CartCreateView.as_view(), name='cart-create'),
    path('cart/<int:pk>', views.CartRetrieveView.as_view(), name='cart-view'),
    path('cart/list', views.CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/update', views.CartUpdateView.as_view(), name='cart-udate'),
    path('cart/<int:pk>/delete', views.CarDeleteView.as_view(), name='cart-delete'),
    
    
    path('order', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>', views.OrderRetrieveView.as_view(), name='order-view'),
    path('order/list', views.OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/update', views.OrderUpdateView.as_view(), name='order-udate'),
    path('order/<int:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'), 
    path('province', views.ProvinceListView.as_view(), name='provice'), 
]
