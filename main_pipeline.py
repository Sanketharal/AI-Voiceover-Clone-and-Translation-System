from asr import transcribe_video
from translate import translate_to_hindi
from hindi_tts import generate_hindi_audio
from moviepy import VideoFileClip, AudioFileClip
from tkinter import Tk, filedialog

def choose_video():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.avi")])
    return file_path

def merge_audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path).with_duration(video_clip.duration)
    final = video_clip.with_audio(audio_clip)
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')

def main():
    video_path = choose_video()
    if not video_path:
        print("❌ No video selected")
        return

    english_text = transcribe_video(video_path)
    print("🔤 Transcription:", english_text)

    hindi_text = translate_to_hindi(english_text)
    print("🌐 Hindi:", hindi_text)

    audio_path = generate_hindi_audio(hindi_text, output_path="hindi_audio.wav")
    if audio_path:
        output_video = "output_hindi_video.mp4"
        merge_audio_to_video(video_path, audio_path, output_video)
        print(f"✅ Final video saved as: {output_video}")

if __name__ == "__main__":
    main()
