from django.db import models


class Accomplishment(models.Model):

    MUSICAL = 0
    LINGUISTIC = 1
    OTHER = 2

    ACCOMPLISHMENT_TYPES = (
        (MUSICAL, 'Musical'),
        (LINGUISTIC, 'Linguistic'),
        (OTHER, 'Other')
    )

    name = models.CharField(max_length=100)
    accomplishment_type = models.IntegerField(choices=ACCOMPLISHMENT_TYPES)

    def __str__(self):
        return self.name
