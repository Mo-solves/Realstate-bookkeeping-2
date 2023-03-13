from django.db import models
from computedfields.models import ComputedFieldsModel, computed


# Create your models here.


class Customer(ComputedFieldsModel):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, unique=True)
    rent_due = models.FloatField()
    rent_paid = models.FloatField(default=0)
    starting_date = models.DateField()
    due_date = models.DateField()
    deposit = models.FloatField(default=0)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @computed(models.FloatField(), depends=[("self", ["rent_due", "rent_paid"])])
    def balance(self):
        return self.rent_due - self.rent_paid

    @computed(models.IntegerField(), depends=[("self", ["starting_date", "due_date"])])
    def remainig_days(self):
        (self.due_date - self.starting_date).days
        return (self.due_date - self.starting_date).days


class RealState(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True
    )
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location
