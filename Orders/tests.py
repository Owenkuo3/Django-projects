from django.test import TestCase
from django.contrib.auth import get_user_model
from Products.models import Product
from .models import Order, OrderItem
from decimal import Decimal

class OrderModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        self.product = Product.objects.create(name='Test Product', price=25, stock=100)
        self.order = Order.objects.create(user=self.user, status='Pending')
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price=25)

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'testuser')
        self.assertEqual(self.order.status, 'Pending')
        self.assertEqual(self.order.total_amount, 50)
        self.assertEqual(str(self.order), f"Order {self.order.id} by testuser")

    def test_orderitem_creation(self):
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.order_item.price, 25)
        self.assertEqual(str(self.order_item), "2 x Test Product")

    def test_order_total_amount_calculation(self):
        self.order.calculate_total()
        expected_total = Decimal('50.00')
        self.assertEqual(self.order.total_amount, expected_total)
        
def test_signal_triggers_calculate_total(self):
    order = Order.objects.create(user=self.user, status='Pending')
    OrderItem.objects.create(order=order, product=self.product, quantity=2, price=25)
    
    order.refresh_from_db()
    
    expected_total = Decimal('50.00')
    self.assertEqual(order.total_amount, expected_total)