from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Test(TimeStampedModel):
    name = models.CharField(
        'Test',
        max_length= 50
    )
    class Meta:
        verbose_name= 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.name