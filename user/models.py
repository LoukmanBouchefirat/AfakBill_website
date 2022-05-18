from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    Is_normal = models.BooleanField('Utilisateur normal', default=False) 
    Is_revendeur = models.BooleanField('Revendeur', default=True) 
    Is_approved = models.BooleanField(default=False , null=True)
    def __str__(self):
        return self.user.username





   



