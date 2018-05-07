from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)

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

    def create_superuser(self,email,password):
        user=self.create_user(
        email,
        password=password
    )
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=10)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'






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






