from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            price=50.00,
            stock=10
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'This is a test product.')
        self.assertEqual(self.product.price, 50.00)
        self.assertEqual(self.product.stock, 10)

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_price_update(self):
        self.product.price = 60.00
        self.product.save()
        self.assertEqual(self.product.price, 60.00)

    def test_product_stock_update(self):
        self.product.stock = 5
        self.product.save()
        self.assertEqual(self.product.stock, 5)

    def test_product_delete(self):
        self.product.delete()
        self.assertEqual(Product.objects.count(), 0)
