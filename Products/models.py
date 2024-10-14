from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class ProductReview(models.Model):
    user_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user_id} on {self.product_id}'