from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(operation_description="List all products")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a product by ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new product")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a product by ID")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a product by ID")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer