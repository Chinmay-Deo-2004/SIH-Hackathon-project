from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioEntry
from .serializers import AudioEntrySerializer, CreateAudioEntrySerializer

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
            audio_entry = AudioEntry(audio_file=audio_file)
            audio_entry.save()
            return Response(AudioEntrySerializer(audio_entry).data, status=status.HTTP_201_CREATED)
