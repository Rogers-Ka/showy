from django.db import models


# Create your models here.
class Sign(models.Model):
    Username = models.CharField(max_length=70, default='')
    Email = models.EmailField(default='')
    Password = models.CharField(max_length=200, default='')

    def __str__(self):
        return f'{self.Username}'


class Upload(models.Model):
    Username = models.CharField(max_length=70, default='')
    Phone = models.CharField(max_length=70, default='')
    Country = models.CharField(max_length=70, default='')
    State = models.CharField(max_length=70, default='')
    Parish = models.CharField(max_length=70, default='')
    Media = models.CharField(max_length=70, default='')
    item = models.CharField(max_length=100, default='')
    price = models.CharField(max_length=100, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='static/images', max_length=100)

    def __str__(self):
        return f'{self.Username} uploaded {self.item}'


class Login(models.Model):
    Email = models.EmailField(default='')
    Password = models.CharField(max_length=100, default='')

