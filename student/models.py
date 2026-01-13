from django.db import models

# Create your models here.
class courses(models.Model):
    course = models.CharField(max_length=60)

    def __str__(self):
        return self.course

class students(models.Model):
    name = models.CharField(max_length=150)
    college_id = models.CharField(max_length=12)
    course = models.ManyToManyField(courses)
