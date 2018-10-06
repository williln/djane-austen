from django.contrib.auth import get_user_model
from django.db import models

from accomplishments.models import Accomplishment


User = get_user_model()


class Person(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accomplishments = models.ManyToManyField(Accomplishment, related_name='people')

    def get_musical_accomplishments_count(self):
        return self.accomplishments.filter(
            accomplishment_type=Accomplishment.MUSICAL
        ).count()

    def get_linguistic_accomplishments_count(self):
        return self.accomplishments.filter(
            accomplishment_type=Accomplishment.LINGUISTIC
        ).count()

    def get_other_accomplishments_count(self):
        return self.accomplishments.filter(
            accomplishment_type=Accomplishment.OTHER
        ).count()

    def is_musically_accomplished(self):
        return self.get_musical_accomplishments_count() >= 3

    def is_linguistically_accomplished(self):
        return self.get_linguistic_accomplishments_count() >= 3

    def is_otherwise_accomplished(self):
        return self.get_other_accomplishments_count() >= 3

    def is_something_in_air(self):
        return True

    def is_accomplished(self):
        return (
            self.is_musically_accomplished() and
            self.is_linguistically_accomplished() and
            self.is_otherwise_accomplished() and
            self.is_something_in_air()
        )
