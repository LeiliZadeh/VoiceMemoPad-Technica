# Imports the Google Cloud client library
from google.cloud import speech
import speech_recognition as sr

def transcribe_microphone():
    # Instantiates a client with the JSON credentials file in the same directory
    client = speech.SpeechClient.from_service_account_json("confidential.json")

    # Initialize the recognizer
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

    # Detects speech from the microphone
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
        with open("transcript.txt", "w") as f:
            f.write(result.alternatives[0].transcript)

if __name__ == "__main__":
    while True:
        input("Press Enter to start recording (or Ctrl+C to exit)...")
        transcribe_microphone()
