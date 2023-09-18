import uuid

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
    code = models.UUIDField(verbose_name='uuid', default=uuid.uuid4, editable=False)

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass


# class Book(models.Model):
#     name = models.CharField(verbose_name='书名', max_length=10)
#     author = models.CharField(verbose_name='作者', max_length=10)
#     is_delete = models.BooleanField(verbose_name='是否删除', default=False)
