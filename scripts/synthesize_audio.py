from parler_tts import ParlerTTS

def synthesize_audio(transcript, output_file):
    """
    Convert transcript into audio file.
    """
    tts = ParlerTTS()
    audio = tts.synthesize(transcript)
    with open(output_file, 'wb') as f:
        f.write(audio)
