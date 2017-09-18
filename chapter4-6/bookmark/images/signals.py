from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    # 这个通知的作用是当喜欢用户发生改变时,及时的更新total_likes字段
    instance.total_likes = instance.users_like_count()
    instance.save()
