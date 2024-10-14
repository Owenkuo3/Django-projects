from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductReviewViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet)
router.register(r'product-reviews', ProductReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
