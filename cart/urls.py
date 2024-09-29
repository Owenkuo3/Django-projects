from django.urls import path
from .views import CartListCreateView, CartRetrieveUpdateDestroyView

urlpatterns = [
    path('', CartListCreateView.as_view(), name='cart-list-create'),
    path('<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),
]
