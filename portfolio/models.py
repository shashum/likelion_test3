from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    major = models.CharField(max_length=200)
    grade = models.IntegerField()
    hometown = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.name
