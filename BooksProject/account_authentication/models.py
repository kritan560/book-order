from django.db import models

# Create your models here.
class AccountAuthentication(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    logo = models.ImageField(upload_to='account_authentication/logo/')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email