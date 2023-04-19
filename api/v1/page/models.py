from django.db import models
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from .enums import PageTypes
from api.commons.abstracts import SameField
from api.v1.company.models import Company
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin
)
from api.v1.page.managers import (
    PageManager,
)


class Page(SameField, AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    city = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    page = models.CharField(max_length=22, choices=PageTypes.choices())
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = PageManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'company', 'page']

    def __str__(self) -> str:
        return f'{self.phone}'
    
    @cached_property
    def get_phone(self):
        return self.phone.split('|')[-1]

    def clean(self) -> None:
        if self.page != 'admin' and not self.company:
            raise ValidationError('User must be choose one company!!!')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



