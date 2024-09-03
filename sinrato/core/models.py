from django.db import models



# Create your models here.

class Subscribe(models.Model):
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Subscribe"
        verbose_name_plural = "Subscribes"