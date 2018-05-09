from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)

from django.contrib.auth.models import PermissionsMixin

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
    mobile_no = models.IntegerField()

    is_staff = models.BooleanField(('staff status'), default=False,)
    is_superuser = models.BooleanField(('staff status'),default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_no']






class Item(models.Model):
    ITEM_TYPE = (
        ('V','Villa'),
        ('P','Plot'),
        ('F','Flat'),
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
    name = models.CharField(max_length=15)
    contact_phone_no = models.IntegerField()
    city = models.CharField(max_length=20, choices=CITY)
    price=models.IntegerField(default=1)


    def __str__(self):
        return self.name + ": " + str(self.item_images)






