from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_user(self, username, email, contact, user_type, password):
        if not email:
            raise ValueError('Users must have an email address.')

        if not username:
            raise ValueError('Users must have a name.')

        if not contact:
            raise ValueError('Users must add their contact number.')

        if not user_type:
            raise ValueError('Users must select an option.')

        if not password:
            raise ValueError('Users must create a password')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            contact=contact,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, contact, user_type, username="MG01"):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            contact=contact,
            user_type=user_type
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    contact = PhoneNumberField(null=True, blank=True, unique=True)
    user_type = models.CharField(max_length=12,
                                 choices=(('standalone', 'StandAlone'), ('organization', 'Organization')),
                                 default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'contact', 'user_type']

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser
