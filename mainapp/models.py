from django.db import models

# Create your models here.
from django.db import models

class HonorCodeViolation(models.Model):
    name = models.CharField(max_length=255, blank=True)
    date_of_incident = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='violations_photos/', blank=True, null=True)
    file = models.FileField(upload_to='violation_files/', blank=True, null=True)
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    def __str__(self):
        return f"Violation by {self.name} on {self.date_of_incident}"