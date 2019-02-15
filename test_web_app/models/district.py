from django.db import models


class District(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    iso_district_code = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name + ' - ' + self.iso_district_code
