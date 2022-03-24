from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class AuthUserManager(BaseUserManager):
    def create(self, first_name, last_name, email, phone,  password, **other_fields ):
        if not email:
            raise ValueError('Email cannot be empty')
        if not phone:
            raise ValueError('Phone cannot be empty.')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,first_name, last_name, email, phone,  password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        return self.create( first_name, last_name, email, phone,  password, **other_fields )


class UserModel(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=False, null=False, max_length=45)
    last_name  = models.CharField(blank=False, null=False, max_length=45)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField(blank=False, null=False, unique=True)
    is_email_verified = models.BooleanField(default=False)
    # is_phone_verified = models.BooleanField(default=False) For Future Use
    is_tutor=models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = AuthUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'is_tutor' ]

    class Meta:
        verbose_name = "UserAccounts"
        verbose_name_plural = "UserAccounts"

    def get_full_name(self):
        """Retreive full name of User """
        return f'{self.first_name} {self.last_name}'
    
    def get_short_name(self):
        """Retreive short name of User """
        return self.first_name

    def __str__(self):
        return "@{}".format(self.email)
    
    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'admin@e-shop.com',
            [self.email],
            fail_silently=False,
        )

