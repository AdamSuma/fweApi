from django.db import models

# Create your models here.

class CSVFile(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='csv_files/')
    name = models.CharField(max_length=150, default="default.csv", null=False)
    class Meta:
        unique_together = ('uploaded_at', 'name')
