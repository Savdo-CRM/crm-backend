from django.contrib.auth.models import BaseUserManager


class PageManager(BaseUserManager):
    """  """
    def create_user(
        self, phone, first_name, last_name, company, page, password, **extra_fields
    ):

        if not phone:
            raise ValueError('The email must not be empty')
        if not first_name:
            raise ValueError('The user must have a first name')
        if not last_name:
            raise ValueError('The user must have a last Name')
        if not company:
            raise ValueError('The user must have a Company')
        if not page:
            raise ValueError('The user must have a page')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            company_id=company,
            page=page,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, phone, first_name, last_name, company, page, password, **extra_fields
    ):
        user = self.create_user(
            phone=phone,
            first_name=first_name,
            password=password,
            last_name=last_name,
            company=company,
            page=page
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    # def _create_user(self, phone, first_name, last_name, company, password, **extra_fields):
    #     if not phone:
    #         raise ValueError("Fill phone")
    #     if not first_name:
    #         raise ValueError("Fill first_name")
    #     if not last_name:
    #         raise ValueError("Fill last_name")
    #     if not company:
    #         raise ValueError("Fill company")
    #     if not password:
    #         raise ValueError("Fill password")
    #     user = self.model(
    #         phone=phone, first_name=first_name, last_name=last_name, company_id=company, **extra_fields
    #     )
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_user(
    #     self, phone, first_name, last_name, company, password, **extra_fields
    # ):
    #     extra_fields.setdefault("is_staff", False)
    #     extra_fields.setdefault("is_admin", False)
    #     extra_fields.setdefault("is_superuser", False)
    #     return self._create_user(phone, first_name, last_name, company, password, **extra_fields)

    # def create_superuser(
    #     self, phone, first_name, last_name, company, password, **extra_fields
    # ):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_admin", True)
    #     extra_fields.setdefault("is_superuser", True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")

    #     return self._create_user(phone, first_name, last_name, company, password, **extra_fields)
    
