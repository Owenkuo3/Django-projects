from django.test import TestCase
from .models import Shop

class ShopModelTest(TestCase):

    def setUp(self):
        self.shop = Shop.objects.create(
            name="Test Shop",
            description="This is a test description",
            address="123 Test Street",
            contact_email="test@example.com",
            contact_phone="123-456-7890"
        )

    def test_shop_creation(self):
        self.assertEqual(self.shop.name, "Test Shop")
        self.assertEqual(self.shop.description, "This is a test description")
        self.assertEqual(self.shop.address, "123 Test Street")
        self.assertEqual(self.shop.contact_email, "test@example.com")
        self.assertEqual(self.shop.contact_phone, "123-456-7890")

    def test_shop_str(self):
        self.assertEqual(str(self.shop), "Test Shop")
