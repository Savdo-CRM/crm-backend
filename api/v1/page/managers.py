from django.contrib.auth.models import BaseUserManager
from api.v1.page.enums import PageTypes
from django.db.models.query import QuerySet


class PageManager(BaseUserManager):
    """  """
    def create_page(
        self, phone, first_name, last_name, company_id, password, **extra_fields
    ):

        if not phone:
            raise ValueError('The email must not be empty')
        if not first_name:
            raise ValueError('The page must have a Phonenumber')
        if not last_name:
            raise ValueError('The page must have a First Name')
        if not company_id:
            raise ValueError('The page must have a Last Name')

        page = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            company_id=company_id,
        )
        page.set_password(password)
        page.save(using=self._db)
        return page

    def create_superpage(
        self, phone, first_name, last_name, company_id, password, **extra_fields
    ):
        page = self.create_page(
            phone=phone,
            first_name=first_name,
            password=password,
            last_name=last_name,
            company_id=company_id,
        )
        page.is_admin = True
        page.is_staff = True
        page.is_superpage = True
        page.save(using=self._db)
        return page
    
