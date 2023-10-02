from django.db import models
from SIH_Project.db_connection import db

# Create your models here.

class AudioEntry (models.Model):
<<<<<<< HEAD
    audio_file = models.FileField(upload_to='audio_files')
    sentiment = models.CharField(max_length=10)
    suggestions = models.TextField()
=======
    audio_file = models.FileField()
    transcript = models.TextField(default="")
    sentiment = models.CharField(max_length=10)
    suggestions = models.TextField(default="")
>>>>>>> 9102f49f5e1ed292e5cf5f8ac9cf586537b6b878
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
