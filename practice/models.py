from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class State(models.Model):
    id = models.IntegerField(primarykey=True)
    name = models.CharField(max_length=50)

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

class TrackingNumbers(models.Model):
    type = models.SmallIntegerField(validators = [
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    category = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100),
    ])
    subcategory = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

class InventoryPlan: 
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

class InventoryCheck: 
    inventory_plan_id = models.ForeignKey(InventoryPlan, on_delete=models.CASCADE)
    pencils_in_stock = models.BooleanField(default = False)
    pens_in_stock = models.BooleanField(default = False)
    paper_in_stock = models.BooleanField(default=False)
    clips_in_stock = models.BooleanField(default=False)
    erasers_in_stock = models.BooleanField(default=False)



