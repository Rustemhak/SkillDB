from django.db import models


# Create your models here.
from django.db.models import CASCADE


class Students(models.Model):
    StudentsType = models.TextChoices('StudentsType', 'Профорг Культорг Спорторг Соцорг Научорг Инфорг Волонтеры')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    area = models.CharField(max_length=20, choices=StudentsType.choices)

    def get_full_name(self):
        full_name = '%s %s' % (self.name, self.surname)
        return full_name.strip()

    def __str__(self):
        return "%s %s %s" % (self.name, self.surname, self.area)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

