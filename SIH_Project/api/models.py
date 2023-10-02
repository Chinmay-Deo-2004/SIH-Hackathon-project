from django.db import models
from SIH_Project.db_connection import db

# Create your models here.

class AudioEntry (models.Model):
    audio_file = models.FileField()
    transcript = models.TextField(default="")
    sentiment = models.CharField(max_length=10)
    suggestions = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
