from django.db import models

# Create your models here.

class Item(models.Model):
    # title = models.CharField(max_length=100, default=0)
    # description = models.CharField(max_length=100, default=0)
    name_u = models.CharField(max_length=100, verbose_name="Name")
    from_u = models.CharField(max_length=100, verbose_name="From")
    to_u = models.CharField(max_length=100, verbose_name="To")
    when_u = models.DateTimeField(verbose_name="When")
    seats_u = models.IntegerField(verbose_name="Seats")
    cost_u = models.DecimalField(max_digits=6, verbose_name="Cost", decimal_places=2)
    will_drop_u = models.BooleanField(verbose_name="Willing to drop along the way")
    extra_details_u = models.TextField(max_length=500, verbose_name="Extra Details")

class RideRequestPost(models.Model):
    # title = models.CharField(max_length=100, default=0)
    # description = models.CharField(max_length=100, default=0)
    name_u = models.CharField(max_length=100, verbose_name="Name")
    from_u = models.CharField(max_length=100, verbose_name="From")
    to_u = models.CharField(max_length=100, verbose_name="To")
    when_u = models.DateTimeField(verbose_name="When")
    # seats_u = models.IntegerField(verbose_name="Seats")
    # cost_u = models.DecimalField(max_digits=6, verbose_name="Cost", decimal_places=2)
    # will_drop_u = models.BooleanField(verbose_name="Willing to drop along the way")
    extra_details_u = models.TextField(max_length=500, verbose_name="Extra Details")

