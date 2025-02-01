from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.user.username} on {self.date} at {self.time}"