from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Need to call clean_fields to trigger validators function
def validate_postcode(value):
    if len(value) != 5:
        raise ValidationError("Postcode must be 5 digits long")


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    postcode = models.CharField(max_length=5, validators=[validate_postcode])
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name



