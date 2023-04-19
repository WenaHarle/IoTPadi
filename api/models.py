from django.db import models

# Create your models here.
class Data(models.Model):
    day = models.IntegerField()
    total = models.IntegerField()
    avg = models.FloatField()
    max = models.FloatField()
    min = models.DecimalField(max_digits=20, decimal_places=20)
    sumD = models.IntegerField()
    Ourl = models.CharField(max_length=255, null=False, blank=False)
    Purl = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.day

