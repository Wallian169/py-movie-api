from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        max_length=1000,
    )
    duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
