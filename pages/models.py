from django.db import models


class SportSkills(models.Model):
    name = models.CharField(max_length=150)
    id = models.IntegerField(primary_key=True)
