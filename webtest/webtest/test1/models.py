from django.db import models

# Create your models here.
class lgzp1(models.Model):
    __table__ = "lgzp1"
    id = models.IntegerField(primary_key=True, auto_created=True),
    info = models.CharField(max_length=10000)


