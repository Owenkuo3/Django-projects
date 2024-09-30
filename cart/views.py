from rest_framework import viewsets
from .models import cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated


class CartViewSet(viewsets.ModelViewSet):
    queryset = cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    