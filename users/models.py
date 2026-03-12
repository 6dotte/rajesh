from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, name, mobile_no, email, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(name, mobile_no, email, password, **other_fields)

    def create_user(self, name, mobile_no, email, password, **other_fields):

        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')

        email = self.normalize_email(email)
        user = self.model(mobile_no, email=email, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}

USER_TYPE = (
    ("User", "User"),
    ("Admin", "Admin")
)


class NewUser(AbstractBaseUser, PermissionsMixin):
    mobile_no = models.CharField(max_length=11, null=True, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    father_name = models.CharField(max_length=25, blank=True, null=True)
    qualification = models.CharField(max_length=55, blank=True, null=True)
    location = models.CharField(max_length=25, default='', blank=True)
    joining_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_no_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    address = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    user_type = models.CharField(
        max_length=15, choices=USER_TYPE, default='User', blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_no', 'password']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Users"
