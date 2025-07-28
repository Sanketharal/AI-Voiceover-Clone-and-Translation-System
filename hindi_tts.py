
from gtts import gTTS

def generate_hindi_audio(hindi_text, output_path="hindi_output.wav", voice=None):
    """
    Generate Hindi audio from text using Google Text-to-Speech (gTTS)
    
    Args:
        hindi_text: The Hindi text to convert to speech
        output_path: Path to save the output audio file
        voice: Not used for gTTS but kept for API compatibility
    
    Returns:
        Path to the generated audio file
    """
    try:
        # Create gTTS object with Hindi language ('hi')
        tts = gTTS(text=hindi_text, lang='hi', slow=False)
        
        # Save the audio file
        tts.save(output_path)
        
        print(f"✅ Hindi audio saved to: {output_path} using Google TTS")
        return output_path
    
    except Exception as e:
        print(f"❌ Error with Google TTS: {e}")
        return None