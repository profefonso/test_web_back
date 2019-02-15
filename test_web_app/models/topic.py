from django.db import models
from test_web_app.models.municipality import Municipality


class Topic(models.Model):
    CREATED = 'created'
    ACTIVE = 'active'
    REJECTED = 'rejected'

    STATES_CHOICES = (
        (CREATED, CREATED),
        (ACTIVE, ACTIVE),
        (REJECTED, REJECTED)
    )

    date = models.DateField(
        auto_now_add=False
    )
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    tags = models.CharField(
        max_length=250,
        null=False,
        blank=False
    )

    state = models.CharField(
        max_length=15,
        choices=STATES_CHOICES,
        default=ACTIVE
    )

    def __str__(self):
        return str(self.date) + ' - ' + self.municipality.name
