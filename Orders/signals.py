from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_order_total(sender, instance, **kwargs):
    if kwargs.get('created', False):
        print(f"Order {instance.id} created. Calculating total.")
        instance.calculate_total()