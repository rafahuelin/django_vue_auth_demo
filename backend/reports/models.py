import uuid
from django.db import models


class Report(models.Model):
    ACCESS_LEVELS = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=160)
    content = models.TextField()
    minimum_access_level = models.CharField(max_length=6, choices=ACCESS_LEVELS, default=ACCESS_LEVELS[0])        

    def __str__(self):
        return self.title
