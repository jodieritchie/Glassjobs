from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
    # Reference to user in database
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

# Checks if user exist and if not creates it
User.userprofile = property(lambda u: Userprofile.objects.get_or_create(user=u)[0])
