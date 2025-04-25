from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']  # Ordenar por data de criação, mais recentes primeiro
