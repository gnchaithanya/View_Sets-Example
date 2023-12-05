from django.db import models

# Create your models here.
class Produuct_category(models.Model):
    Category_name=models.CharField(max_length=100)
    Category_id=models.IntegerField()

    def __str__(self):
        return self.Category_name

class Product(models.Model):
    Pname=models.CharField(max_length=100)
    Pid=models.IntegerField()
    P_Price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.Pname