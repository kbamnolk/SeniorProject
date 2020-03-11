import argparse
import six
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate

def text_to_text():
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    """
    target = 'en'
    text = 'Como te llamas?'
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    return result['translatedText']
    
def text_to_speech(input_text):
	# Instantiates a client
	client = texttospeech.TextToSpeechClient()

	# text input is hardcoded for now
	text_input = texttospeech.types.SynthesisInput(text=input_text)

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

translated_text = text_to_text()
text_to_speech(translated_text)
