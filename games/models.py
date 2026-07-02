from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    release_year = models.IntegerField()
    na_sales = models.DecimalField(max_digits=8, decimal_places=2)
    eu_sales = models.DecimalField(max_digits=8, decimal_places=2)
    jp_sales = models.DecimalField(max_digits=8, decimal_places=2)
    other_sales = models.DecimalField(max_digits=8, decimal_places=2)
    global_sales = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name