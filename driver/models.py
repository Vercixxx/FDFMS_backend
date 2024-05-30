from django.db import models
from users.models import GeneralUser


class Driver(GeneralUser):
    license_number = models.CharField(max_length=50, blank=True, null=True)
    ln_release_date = models.DateField(max_length=50, blank=True, null=True)
    ln_expire_date = models.DateField(max_length=50, blank=True, null=True)
    ln_published_by = models.CharField(max_length=70, blank=True, null=True)
    ln_code = models.CharField(max_length=15, blank=True, null=True)

    wage_tariff = models.ForeignKey(
        'WageTariff', db_column='wage_tariff', on_delete=models.SET_NULL, blank=True, null=True)
    
    rate = models.ForeignKey('Rating', db_column='rate', on_delete=models.SET_NULL, blank=True, null=True)

    # User color
    color_choices = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('brown', 'Brown'),
        ('black', 'Black'),
        ('white', 'White'),
        ('cyan', 'Cyan'),
        ('magenta', 'Magenta'),
        ('lime', 'Lime'),
        ('teal', 'Teal'),
        ('lavender', 'Lavender'),
        ('maroon', 'Maroon'),
        ('navy', 'Navy'),
        ('olive', 'Olive'),
        ('silver', 'Silver'),
    )

    user_color = models.CharField(
        max_length=20,
        choices=color_choices,
        default='green'
    )

    class Meta:
        db_table = 'Drivers'

    def __str__(self):
        return self.username


class DailyWork(models.Model):
    driver = models.ForeignKey(
        Driver, db_column='driver', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    orders = models.IntegerField(default=0)
    start_work = models.TimeField()
    end_work = models.TimeField()
    working_time = models.TimeField()
    orders_per_hour = models.FloatField(default=0.0)

    class Meta:
        db_table = 'DailyWorkReports'


class WageTariff(models.Model):
    name = models.CharField(max_length=50)
    basic_hourly_rate = models.FloatField()
    orders_bonus = models.FloatField()
    fuel_bonus = models.FloatField()

    starting_new_billing_period = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'WageTariff'

    def __str__(self):
        return self.name


class Rating(models.Model):
    # Rating options
    rating_options = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    rating = models.CharField(
        max_length=1,
        choices=rating_options,
        default='1'
    )
    
    # Day options
    day_options = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )

    day = models.CharField(
        max_length=1,
        choices=day_options,
        default='1'
    )
    
    hour = models.TimeField()
        

    class Meta:
        db_table = 'DriverRatings'

    def __str__(self):
        return self.rating
