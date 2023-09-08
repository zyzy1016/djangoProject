from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class NewUser(AbstractUser):
    role_type = [
        [0, 'admin'],
        [1, 'user']
    ]

    roles = models.IntegerField(verbose_name='角色', choices=role_type, default=1)
    # name = models.CharField(_('name'), max_length=150)
    last_login = models.DateTimeField(_('last_login'), blank=True, null=True, auto_now=True)

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass
