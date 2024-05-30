from django.db import models
from django.utils import timezone

from driver.models import Driver


class Car(models.Model):

    vin = models.TextField(max_length=17, primary_key=True)

    license_plate = models.TextField(
        max_length=10, unique=True, null=True, blank=True)
    
    active = models.BooleanField(default=True)

    brand = models.TextField()
    model = models.TextField()

    # Year of production
    YEAR_CHOICES = [(r, r) for r in range(1990, timezone.now().year+1)]
    year_of_prod = models.PositiveIntegerField(
        choices=YEAR_CHOICES, default=timezone.now().year)
    # Year of production

    color = models.TextField()
    mileage = models.IntegerField(default=0)
    engine_cap = models.FloatField()
    engine_pow = models.IntegerField()

    # Transmission
    transmission_choices = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    )

    transmission = models.CharField(
        max_length=20,
        choices=transmission_choices,
        default='Manual'
    )
    # Transmission

    policy_number = models.TextField()
    is_oc = models.BooleanField()
    is_ac = models.BooleanField()
    phone_policy_contact = models.CharField(max_length=20)

    def __str__(self):
        return self.vin

    class Meta:
        db_table = 'Cars'


class CarDailyReports(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    driver = models.ForeignKey(
        Driver, db_column='driver', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, db_column='car', on_delete=models.CASCADE)

    car_mileage = models.CharField(max_length=7)

    car_condition_options = (
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )

    car_condition = models.CharField(
        max_length=1,
        choices=car_condition_options,
        default='3'
    )

    cleanliness_options = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )

    car_cleanliness = models.CharField(
        max_length=1,
        choices=cleanliness_options,
        default='5'
    )

    additional_remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'CarDailyReports'
        
class CarDamage(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    driver = models.ForeignKey(
        Driver, db_column='driver', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, db_column='car', on_delete=models.CASCADE)

    car_mileage = models.CharField(max_length=7)

    description = models.TextField(max_length=1000)
    