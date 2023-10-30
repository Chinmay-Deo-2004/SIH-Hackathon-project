from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AudioEntry
from .serializers import AudioEntrySerializer, CreateAudioEntrySerializer
import openai
import os
import tempfile
from decouple import config
import whisper
import soundfile as sf
import numpy as np
import io


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
            #here type of audio_file is NoneType. It should be bytes. Let's see if we can fix it.
            #uplod to test.mp3 




            #storing audio in temp file to be used by openai
            
            
            # with open('./audio_files/test.mp3', 'rb') as audio_file:
                # audio_data = audio_file.read()
                # openai.api_key = "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"
                # transcript = openai.Audio.transcribe("whisper-1", file=audio_file)

                # audio, sample_rate = sf.read(io.BytesIO(audio_data))                
            model = whisper.load_model("base")
            transcript = model.transcribe("./audio_files/test")

                

            audio_entry = AudioEntry(audio_file=audio_file, transcript=transcript) 
            audio_entry.save()
            return Response(AudioEntrySerializer(audio_entry).data, status=status.HTTP_201_CREATED)
