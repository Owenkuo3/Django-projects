import pytest
from rest_framework.test import APIClient
from food.models import Item

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_item(django_db):
    return Item.objects.create(
        item_name='Apple',
        item_desc='A red apple',
        item_price=10,
        item_image='https://example.com/apple.jpg'
    )

def test_get_items(api_client):
    response = api_client.get('/food/item/')
    assert response.status_code == 200

def test_post_item(api_client):
    data = {
        'item_name': 'Banana',
        'item_desc': 'A yellow banana',
        'item_price': 5,
        'item_image': 'https://example.com/banana.jpg'
    }
    response = api_client.post('/food/add', data, format='json')
    assert response.status_code == 201

def test_get_item(create_item, api_client):
    response = api_client.get(f'/food/{create_item.id}/')
    assert response.status_code == 200

def test_put_item(create_item, api_client):
    data = {
        'item_name': 'Green Apple',
        'item_desc': 'A green apple',
        'item_price': 12,
        'item_image': 'https://example.com/green_apple.jpg'
    }
    response = api_client.put(f'/food/update/{create_item.id}/', data, format='json')
    assert response.status_code == 200

def test_delete_item(create_item, api_client):
    response = api_client.delete(f'/food/delete/{create_item.id}')
    assert response.status_code == 204
