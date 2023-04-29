from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin, BaseUserManager ,AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name,  password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name,  password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

        
class CustomUser(AbstractUser , PermissionsMixin):
    email = models.EmailField(verbose_name='email' , max_length=60 , unique=True)
    user_name = models.CharField(max_length=30 , unique=True)
    start_date = models.DateTimeField(auto_now_add=True , verbose_name='date joined')
    last_login = models.DateTimeField(auto_now=True , verbose_name='last login')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.user_name

