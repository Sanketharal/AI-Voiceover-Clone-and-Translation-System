import whisper

# Load the whisper model only once
model = whisper.load_model("base")  # You can use "small" or "medium" for better accuracy
 
def transcribe_video(video_path):
    """
    Transcribes speech from a video/audio file to text using Whisper.
    Input: video_path (e.g., "TestVideo.mp4")
    Output: transcribed text as string
    """
    result = model.transcribe(video_path)
    return result["text"]
