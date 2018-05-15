from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)

from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

from django.contrib.auth.models import User
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None, mobile_no=None,name=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_no=mobile_no,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,name,mobile_no):
        user=self.create_user(
        email,
        password=password,name=name,mobile_no=mobile_no
    )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    # mobile_no = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Invalid Mobile Number !!!")
    mobile_no = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    is_staff = models.BooleanField(('staff status'), default=False,)
    is_superuser = models.BooleanField(('staff status'),default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_no']

class Item(models.Model):
    ITEM_TYPE = (
        ('V', 'Villa'),
        ('P', 'Plot'),
        ('F', 'Flat'),
    )
    CITY = (
        ('KOCHI','kochi'),
        ('TRIVANDRUM','trivandrum'),
        ('KOTTAYAM','kottayam'),
        ('THRISSUR','thrissur'),
        ('KOZHIKODE','kozhikode'),

    )
    item_title = models.CharField(max_length=50)
    item_description = models.CharField(max_length=90)
    item_type = models.CharField(max_length=1, choices=ITEM_TYPE)
    item_images = models.ImageField(upload_to='realapp/images')
    creator_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, )
    # contact_phone_no = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Invalid Mobile Number !!!")
    contact_phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    city = models.CharField(max_length=20, choices=CITY)
    price = models.IntegerField(default=1)

# for viewing data rather than objects in admin
    def __str__(self):
        return self.item_title


class Registration(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)







