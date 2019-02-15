from django.db import models
from test_web_app.models.district import District


class Municipality(models.Model):
    district = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    comments = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.district.iso_district_code + ' - ' + self.name
