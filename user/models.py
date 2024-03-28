from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# from core.models import org

user_model = settings.AUTH_USER_MODEL

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique = True, blank = False)
    first_name = models.CharField(max_length=255,blank = False)
    last_name = models.CharField(max_length=255,blank = False)


class Profile(models.Model):
    user = models.OneToOneField(user_model,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='user/profile',blank=True)
    # org = models.ForeignKey()
    org_email = models.EmailField(blank=True)
    verified_org = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s profile"