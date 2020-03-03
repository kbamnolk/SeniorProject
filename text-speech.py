#!/usr/bin/env python3
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# text input is hardcoded for now
text_input = texttospeech.types.SynthesisInput(text="this is a test for the text to speech")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
# audio file type is temporary
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(text_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')