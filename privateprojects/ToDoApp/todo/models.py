from django.db import models

# Create your models here.
class Todo(models.Model):
    time = models.DateTimeField(blank=True)
    task = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
