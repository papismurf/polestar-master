from django.db import models


# Create your models here.

class Ships(models.Model):
    imo = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Positions(models.Model):
    # The relation between ships and their points maintained by it's imo
    def save(self, *args, **kwargs):
        self.full_clean()  # performs regular validation then clean()
        super(Positions, self).save(*args, **kwargs)

    imo = models.ForeignKey(Ships, on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    # latitude and longitude fields should be decimal with 9 maximum digit with 6 decimal places for example 180.454545
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

