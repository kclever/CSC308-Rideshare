from djongo import models

# Create your models here.

class Item(models.Model):
    # title = models.CharField(max_length=100, default=0)p
    # description = models.CharField(max_length=100, default=0)
    name_u = models.CharField(max_length=100, verbose_name="Name")
    from_u = models.CharField(max_length=100, verbose_name="From")
    to_u = models.CharField(max_length=100, verbose_name="To")
    when_u = models.DateTimeField(verbose_name="When")
    seats_u = models.IntegerField(verbose_name="Seats")
    cost_u = models.DecimalField(max_digits=6, verbose_name="Cost", decimal_places=2)
    will_drop_u = models.BooleanField(verbose_name="Willing to drop along the way")
    extra_details_u = models.TextField(max_length=500, verbose_name="Extra Details")

class Account(models.Model):
    first_u = models.CharField(max_length=50, verbose_name='First Name')
    last_u = models.CharField(max_length=50, verbose_name='Last Name')
    user_u = models.CharField(max_length=50, verbose_name='Username')
    password_u = models.CharField(max_length=64, verbose_name='Password')
    email_u = models.CharField(max_length=50, verbose_name='Email')