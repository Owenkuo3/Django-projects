from django.test import TestCase
from django.urls import reverse
from .models import Item

class FoodViewsTest(TestCase):

    def setUp(self):
        self.item = Item.objects.create(
            item_name='Apple',
            item_desc='A red apple',
            item_price=10,
            item_image='https://example.com/apple.jpg'
        )

    def test_create_item(self):
        response = self.client.post(reverse('food:create_item'), {
            'item_name': 'Banana',
            'item_desc': 'A yellow banana',
            'item_price': 5,
            'item_image': 'https://example.com/banana.jpg',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Item.objects.count(), 2)

    def test_update_item(self):
        response = self.client.post(reverse('food:update_item', args=[self.item.id]), {
            'item_name': 'Apple',
            'item_desc': 'A green apple',
            'item_price': 12,
            'item_image': 'https://example.com/green-apple.jpg',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.item.refresh_from_db()
        self.assertEqual(self.item.item_desc, 'A green apple')

    def test_delete_item(self):
        response = self.client.post(reverse('food:delete_item', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Item.objects.count(), 0)

    def test_index_view(self):
        response = self.client.get(reverse('food:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Apple')

    def test_detail_view(self):
        response = self.client.get(reverse('food:detail', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Apple')

    def test_delete_item_requires_post(self):
        response = self.client.get(reverse('food:delete_item', args=[self.item.id]))
        self.assertNotEqual(response.status_code, 302)  # Should not redirect
        self.assertEqual(Item.objects.count(), 1)


