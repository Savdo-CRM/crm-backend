from django.contrib.auth.models import BaseUserManager


class PageManager(BaseUserManager):
    """  """
    def create_user(
        self, phone, name, company, page, password, **extra_fields
    ):

        if not phone:
            raise ValueError('The email must not be empty')
        if not name:
            raise ValueError('The user must have a last Name')
        if not company:
            raise ValueError('The user must have a Company')
        if not page:
            raise ValueError('The user must have a page')

        user = self.model(
            name=name,
            phone=phone,
            company_id=company,
            page=page,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, phone, name, company, page, password, **extra_fields
    ):
        user = self.create_user(
            phone=phone,
            password=password,
            name=name,
            company=company,
            page=page
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
