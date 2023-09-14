from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    FARMER = 1
    HARVESTER = 2
    VILLAGER =3

    ROLE_CHOICES = (
        (FARMER, 'Farmer'),
        (HARVESTER, 'Harvester'),
        (VILLAGER, 'Villager'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    # You can create Role model separately and add ManyToMany if user has more than one role
      
    REQUIRED_FIELDS = ['role']

    def can_edit(self):
        if self.role == 1:
            return True
        else:
            return False
