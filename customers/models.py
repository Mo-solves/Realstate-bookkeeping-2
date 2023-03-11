from django.db import models
from computedfields.models import ComputedFieldsModel, computed


# Create your models here.


class Customer(ComputedFieldsModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, unique=True)
    rent_due = models.FloatField()
    rent_paid = models.FloatField(default=0)
    starting_date = models.DateField()
    due_date = models.DateField()
    deposit = models.FloatField(default=0)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @computed(models.FloatField(), depends=[("self", ["rent_due", "rent_paid"])])
    def balance(self):
        return self.rent_due - self.rent_paid

    @computed(models.IntegerField(), depends=[("self", ["starting_date", "due_date"])])
    def remainig_days(self):
        return (self.due_date - self.starting_date).days
