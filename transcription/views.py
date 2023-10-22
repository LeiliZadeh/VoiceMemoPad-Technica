# transcription/views.py

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from google.cloud import speech
import speech_recognition as sr
import Main

def transcribe(request):
    transcript = None
    file_url = "/path/to/your/downloaded/file"  # Update with the actual file URL

    if request.method == 'GET':
        # Your transcription code here (similar to your existing code)
        client = speech.SpeechClient.from_service_account_json("confidential.json")
        r = sr.Recognizer()

        with sr.Microphone(sample_rate=16000, chunk_size=1024) as source:
            r.adjust_for_ambient_noise(source)
            print("Listening for speech...")
            audio = r.listen(source, timeout=10)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=18000,
            language_code="en-US",
        )
        

        audio = speech.RecognitionAudio(content=audio.frame_data)

        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            transcript = result.alternatives[0].transcript

    return JsonResponse({'url': file_url, 'text': transcript})

def index(request):
    return render(request, 'transcribe.html')

def start_recording(request):
    subprocess.run(['python', 'main.py'])
    return HttpResponse("Recording and transcription begun.")
