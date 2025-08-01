from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    #new field
    end_date = models.DateField(null=True, blank=True)

    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title