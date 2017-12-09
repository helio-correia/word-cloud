import uuid as uuid_lib

from django.db import models


class Word(models.Model):
    id = models.UUIDField(primary_key=True,
                          db_index=True,
                          default=uuid_lib.uuid4,
                          editable=False)
    name = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

    class Meta:
        ordering = ['-count']

    def __str__(self):
        return self.name
