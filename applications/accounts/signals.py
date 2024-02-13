from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Действия при создании нового пользователя
        pass
    else:
        # Действия при обновлении существующего пользователя
        pass
