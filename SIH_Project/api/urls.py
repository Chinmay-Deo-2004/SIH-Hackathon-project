from django.urls import path
from .views import AudioView, CreateAudioEntryView

urlpatterns = [
    path('audio', AudioView.as_view()),
    path('create-audio-entry', CreateAudioEntryView.as_view())
]