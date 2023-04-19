from django.db import models

from api.commons.abstracts import SameField


class Company(SameField):
    """ 2 """
    name = models.CharField(max_length=255)
    u_name = models.CharField(max_length=255, unique=True)
    inn = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return f'{self.name} {self.inn}'

