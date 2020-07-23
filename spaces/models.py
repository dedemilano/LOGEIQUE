from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='client')
    contact = models.CharField(max_length=50)
    rent_proposal = models.BigIntegerField(null=True)
    deposit_proposal = models.BigIntegerField(null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

    def __str__(self):
        return f'{self.user}'

    class Meta():
        ordering = ['user', 'rent_proposal',
                    'deposit_proposal', 'contact']


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    clients = models.ManyToManyField(
        Client, related_name="landlords", through="Deal")

    def __str__(self):
        return f'{self.username}'

    class Meta():
        ordering = ['user', 'contact']


class House(models.Model):
    house_area = models.CharField(max_length=50)
    house_rent = models.BigIntegerField()
    house_deposit = models.BigIntegerField()
    house_kind = models.CharField(max_length=50)
    house_rooms_number = models.PositiveSmallIntegerField()
    house_available = models.BooleanField()
    house_to_sell = models.BooleanField()
    house_image = models.ImageField(upload_to="houses/" , )
    landlord = models.ForeignKey(
        Landlord, on_delete=models.CASCADE, related_name="houses")

    def __str__(self):
        return f'{self.area} , {self.kind}'

    class Meta():
        ordering = ['house_area', 'house_kind',
                    'house_rooms_number', 'house_rent', 'house_deposit']


class Deal(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_deals")
    landlord = models.ForeignKey(
        Landlord, on_delete=models.CASCADE, related_name="landlord_deals")

    concluded = models.BooleanField()
