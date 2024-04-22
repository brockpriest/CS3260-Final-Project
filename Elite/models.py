from datetime import datetime
from django.core.validators import MaxValueValidator
from django.db import models
from django.shortcuts import get_object_or_404


# Create Models Here

class VehicleInformation(models.Model):
    current_year = datetime.now().year
    id = models.AutoField(primary_key=True)
    CHOICES = [
        ('purchased', 'Purchased'),
        ('sold', 'Sold'),
        ('hidden', 'Hidden')
    ]
    dropdown_field = models.CharField(max_length=20, choices=CHOICES, null=False, default='purchased')
    Year = models.IntegerField(validators=[MaxValueValidator(current_year+1)])
    Make = models.CharField(max_length=200, null=False)
    Model = models.CharField(max_length=200, null=False)
    VIN = models.CharField(max_length=20, null=False)

    # Purchase information
    PurchaseDate = models.DateField(null=True, blank=True)
    PurchasePrice = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    PurchasedFrom = models.CharField(max_length=200, null=True, blank=True)

    # Sold Information
    SoldDate = models.DateField(null=True, blank=True)
    SoldPrice = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    SoldTo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.id.__str__() + " " + self.Make + " " + self.Model + " " + self.VIN


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    VehicleId = models.ForeignKey(VehicleInformation, on_delete=models.CASCADE)
    Description = models.CharField(max_length=1000)
    Date = models.DateField()
    Amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.Description


def search_expenses(vehicle_id):
    try:
        # Get the VehicleInformation object with the given vehicle_id
        #vehicle_info = get_object_or_404(VehicleInformation, pk=vehicle_id)

        # Filter Expense objects related to the vehicle_info object
        expenses_info = Expense.objects.filter(VehicleId_id=vehicle_id)

        return expenses_info
    except VehicleInformation.DoesNotExist:
        # Handle case when VehicleInformation object does not exist
        return None
    except Expense.DoesNotExist:
        # Handle case when Expense object does not exist
        return None
