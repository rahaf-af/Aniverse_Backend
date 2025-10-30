from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#---------------User---------------
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'Admin'
        REGULAR= "REGULAR", 'Regular'
    base_role = Role.REGULAR
    role = models.CharField(max_length=50, choices=Role.choices)
    def save(self , *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)

class Admin(User):
    base_role =User.Role.ADMIN
    class Meta:
        proxy = True

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , related_name="profile")
    profile_img= models.URLField(null=True , blank=True)
    phone_number = models.CharField(max_length=10, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    bio = models.TextField(null=True , blank=True)



#---------------Anime---------------
class Anime (models.Model):
    publisher = models.ForeignKey(User, on_delete= models.SET_NULL , null=True , blank=True)
    title = models.CharField(max_length=50)
    poster = models.URLField( null=True , blank=True )
    genre = models.CharField(max_length=100 , default='Action')
    global_rating =models.FloatField(default=0.0)
    description = models.TextField(default= 'No description yet', null=True , blank=True)
    def __str__(self):
        return f'{self.title}'

class AnimeFavorit (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , related_name="anime_favorit")
    anime = models.ForeignKey(Anime, on_delete= models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , related_name="anime_comment")
    anime = models.ForeignKey(Anime, on_delete= models.CASCADE )
    text= models.CharField(max_length=100, null=True , blank=True)
    rating =models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



#---------------Post---------------
class Post (models.Model):
    auther = models.ForeignKey(User, on_delete= models.CASCADE , related_name="auther")
    poster = models.URLField( null=True , blank=True )
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class PostFavorit (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , related_name="post_favorit")
    post= models.ForeignKey(Post, on_delete= models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , related_name="anime_post")
    anime = models.ForeignKey(Post, on_delete= models.CASCADE )
    text= models.CharField(max_length=100, null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)