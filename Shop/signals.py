from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shop

@receiver(post_save, sender=Shop)
def update_popularity(sender, instance, created, **kwargs):
    if created:
        instance.popularity = 1  # 初始值可以是 1，依需求調整
        instance.save()
    else:
        instance.popularity += 1  # 假設每次更新 popularity 加 1
        instance.save()
