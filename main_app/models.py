from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'Admin'
        REGULAR= "REGULAR", 'Regular'
    base_role = Role.REGULAR
    role = models.CharField(max_length=50, choices=Role.choices)
    def save(self , *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class Admin(User):
    base_role =User.Role. ADMIN
    class meta:
        proxy = True

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img= models.URLField(null=True , blank=True)
    phone_number = models.IntegerField(max_length=10 , null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    bio = models.TextField(null=True , blank=True)

class Anime (models.Model):
    publisher = models.ForeignKey(User, on_delete= models.SET_NULL , null=True , blank=True)
    title = models.CharField(max_length=50)
    poster = models.URLField( null=True , blank=True )
    genre = models.CharField(max_length=100 , default='Action')
    rating =models.FloatField(default=0.0)
    description = models.TextField(default= 'No description yet', null=True , blank=True)
    def __str__(self):
        return f'{self.title}'

class Post (models.Model):
    auther = models.ForeignKey(User, on_delete= models.SET_NULL , null=True , blank=True)
    poster = models.URLField( null=True , blank=True )
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)