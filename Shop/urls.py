from django.urls import path
from .views import ShopListCreateView, ShopDetailView

urlpatterns = [
    path('', ShopListCreateView.as_view(), name='shop-list-create'),
    path('<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
]
