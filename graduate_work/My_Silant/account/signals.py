from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from My_Silant import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user(sender, instance, created, **kwargs):
    role_choices = {'CLIENT':'Client', 'SERVICE_COMPANY': 'Service_company',' MANAGER': 'Manager'}
    if created:
        try:
            group = Group.objects.get(name=role_choices.get(instance.role))
            instance.groups.add(group)
        except Group.DoesNotExist:
            pass