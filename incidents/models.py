from django.db import models

# Create your models here.

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
