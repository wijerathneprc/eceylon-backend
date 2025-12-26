from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CategoryViewSet, ProductModelViewSet, ProductViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product' )
router.register(r'images', ImageViewSet, basename='image' )
router.register(r'product-models', ProductModelViewSet, basename='product_model')
urlpatterns = router.urls
