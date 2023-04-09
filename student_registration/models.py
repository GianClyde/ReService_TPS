from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
import uuid
from django.template.defaultfilters import slugify
import os
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
branch = [
    ("afpovai","AFPOVAI"),
    ("bayani rd", "Bayani Rd")
]
status = [
    ("PENDING","pending"),
    ("APPROVED", "approved"),
    ("DECLINED", "declined")
]
class UserAccountManager(BaseUserManager):

    def create_superuser(self, email,password, **other_fields):
        other_fields.setdefault('is_staff' , True)
        other_fields.setdefault('is_active' , True)
        other_fields.setdefault('is_superuser' , True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self.create_user(email,password, **other_fields)

    def create_user(self, email,password, **other_fields):

        if not email:
            raise ValueError('email is necessary')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user

class StudentUserManager(BaseUserManager):
    def get_queryset(self,*arg,**kwargs):
        results = super().get_queryset(*arg,**kwargs)
        return results.filter(role=User.Role.STUDENT)

class StudentUserManager(BaseUserManager):
    def get_queryset(self,*arg,**kwargs):
        results = super().get_queryset(*arg,**kwargs)
        return results.filter(role=User.Role.DRIVER)
    

class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'Admin'
        STUDENT = "STUDENT",'Student'
        DRIVER = "DRIVER",'Driver'

    base_role = Role.ADMIN

    id = models.UUIDField(
         primary_key = True,
         unique=True,
         default=uuid.uuid4,
         editable = False)
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    logged = models.IntegerField(null=False, default=0)
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','middle_name','contact_no']

    objects = UserAccountManager()
        
    def __str__(self):
        return self.last_name


class StudentUser(User):


    class Meta:
        proxy = True

class DriverUser(User):

    class Meta:
        proxy = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.CharField(max_length=100, null=True,blank=True)
    parent_contactNo = models.CharField(max_length=100,null=True,blank=True)
    parent_address = models.CharField(max_length=100,null=True,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    lot = models.CharField(max_length=100, null=True,blank=True)
    street = models.CharField(max_length=100, null=True,blank=True)
    village = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=100, null=True,blank=True)
    zipcode = models.IntegerField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    age = models.IntegerField(null=True)
    school_branch=models.CharField(max_length=100,choices=branch, default='bayani rd')
    section = models.CharField(max_length=100, null=True,blank=True)
    year_level= models.CharField(max_length=100, null=True,blank=True)
    def __str__(self):
        return str(self.user)
    
class Driverprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    franchise= models.CharField(max_length=100, null=True,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    lot = models.CharField(max_length=100, null=True,blank=True)
    street = models.CharField(max_length=100, null=True,blank=True)
    village = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=100, null=True,blank=True)
    zipcode = models.IntegerField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    age = models.IntegerField(null=True)
    school_branch=models.CharField(max_length=100,choices=branch, default='bayani rd')
    assigned_route = models.CharField(max_length=100, null=True,blank=True)
    liscense_no = models.CharField(max_length=100, null=True,blank=True)
    operator=models.CharField(max_length=100, null=True,blank=True)
    franchise_no =  models.IntegerField(null=True,blank=True)
    vehicle = models.OneToOneField('Vehicle',on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.user)

class Reservation(models.Model):
    reservation_id = models.UUIDField(
         primary_key = True,
         unique=True,
         default=uuid.uuid4,
         editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Driverprofile,on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100,choices=status, default='PENDING')

    def __str__(self):
        return str(self.reservation_id)
    
class Vehicle(models.Model):
    vehicle_id  = models.UUIDField(
         primary_key = True,
         unique=True,
         default=uuid.uuid4,
         editable = False)
    model = models.CharField(max_length=100)
    plate_no = models.CharField(max_length=10)
    def __str__(self):
        return str(self.model + str(self.vehicle_id))




@receiver(post_save, sender=StudentUser)
def create_user_profile(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance)
    Reservation.objects.create(user=instance)
#this method to update profile when user is updated
@receiver(post_save, sender=StudentUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.reservation.save()


@receiver(post_save, sender=DriverUser)
def create_user_profile(sender, instance, created, **kwargs):
    Driverprofile.objects.create(user=instance)

#this method to update profile when user is updated
@receiver(post_save, sender=DriverUser)
def save_user_profile(sender, instance, **kwargs):
    instance.driverprofile.save()


