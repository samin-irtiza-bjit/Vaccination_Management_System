# Import the models module
from django.db import models

# Define the User model
class User(models.Model):
    # Define the fields
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    nid = models.IntegerField()

    # Define a string representation of the model
    def __str__(self):
        return self.name

# Define the Vaccine model
class Vaccine(models.Model):
    # Define the fields
    vaccine_name = models.CharField(max_length=50)

    # Define a string representation of the model
    def __str__(self):
        return self.vaccine_name

# Define the Vaccination model
class Vaccination(models.Model):
    # Define the fields
    user = models.ForeignKey(User, on_delete=models.CASCADE) # PK and FK to User
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE) # PK and FK to Vaccine
    vaccination_date = models.DateField()

    # Define a string representation of the model
    def __str__(self):
        return f"{self.user} received {self.vaccine} on {self.vaccination_date}"
