# transcription/views.py

from django.shortcuts import render
from django.http import HttpResponse
from google.cloud import speech
import speech_recognition as sr
import Main

def transcribe(request):
    transcript = None

    if request.method == 'POST':
        # Your transcription code here (similar to your existing code)
        client = speech.SpeechClient.from_service_account_json("confidential.json")
        r = sr.Recognizer()

        with sr.Microphone(sample_rate=16000, chunk_size=1024) as source:
            r.adjust_for_ambient_noise(source)
            print("Listening for speech...")
            audio = r.listen(source, timeout=None)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=18000,
            language_code="en-US",
        )

        audio = speech.RecognitionAudio(content=audio.frame_data)

        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            transcript = result.alternatives[0].transcript

    return render(request, 'transcription/transcribe.html', {'transcript': transcript})
