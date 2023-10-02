from rest_framework import serializers
from .models import AudioEntry

class AudioEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioEntry
        fields = ['id','audio_file', 'sentiment', 'suggestions', 'created_at']

class CreateAudioEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioEntry
        fields = ['audio_file']   