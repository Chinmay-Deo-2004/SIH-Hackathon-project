from django.db import models
from SIH_Project.db_connection import db

# Create your models here.

class AudioEntry (models.Model):
    audio_file = models.FileField(upload_to='audio_files')
    sentiment = models.CharField(max_length=10)
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
