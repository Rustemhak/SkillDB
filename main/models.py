from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=120, default='Название мероприятия')
    place = models.CharField(max_length=120, default='Место проведения')
    date = models.CharField(max_length=120)
    people = models.CharField(max_length=120, default='Количество людей')
    donnates = models.TextField()
    comments = models.TextField()
    visible = models.BooleanField(default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    background_image = models.ImageField(null=True, blank=True)
    emoji_image = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % self.id

    class Meta:
        ordering = ["-id", "-timestamp"]
