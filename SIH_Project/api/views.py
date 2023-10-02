from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioEntry
from .serializers import AudioEntrySerializer, CreateAudioEntrySerializer
<<<<<<< HEAD
=======
import openai
>>>>>>> 9102f49f5e1ed292e5cf5f8ac9cf586537b6b878

# Create your views here.

#returns all AudioEntries and allows creation of new AudioEntries
class AudioView(generics.ListAPIView):
    class Meta:
        queryset = AudioEntry.objects.all()
        serializer_class = AudioEntrySerializer

class CreateAudioEntryView(APIView):
    serializer_class = CreateAudioEntrySerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.data.get('audio_file')
<<<<<<< HEAD
            audio_entry = AudioEntry(audio_file=audio_file)
=======
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            audio_entry = AudioEntry(audio_file=audio_file, transcript=transcript)
>>>>>>> 9102f49f5e1ed292e5cf5f8ac9cf586537b6b878
            audio_entry.save()
            return Response(AudioEntrySerializer(audio_entry).data, status=status.HTTP_201_CREATED)
