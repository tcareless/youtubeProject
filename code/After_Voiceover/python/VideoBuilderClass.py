import os
from moviepy.editor import concatenate_audioclips, TextClip, CompositeVideoClip, AudioFileClip
from pydub import AudioSegment

class VideoBuilderClass:
    def __init__(self, voiceover_file, background_music_path, title, video_output_dir):
        self.voiceover_file = voiceover_file  # path to the voiceover file
        self.background_music_path = background_music_path  # path to the background music file
        self.title = title  # title of the video
        self.video_output_dir = video_output_dir  # path to the video output directory
        
    def build_video(self):
        # Load audio files
        voiceover_audio = AudioSegment.from_file(self.voiceover_file)
        background_music_audio = AudioSegment.from_file(self.background_music_path)

        # Trim the longer audio file to match the length of the shorter audio file
        min_length = min(len(voiceover_audio), len(background_music_audio))
        voiceover_audio = voiceover_audio[:min_length]
        background_music_audio = background_music_audio[:min_length]

        # Overlay the two audio files
        combined_audio = voiceover_audio.overlay(background_music_audio)
        
        # Export the combined audio to a temporary file
        combined_audio.export("combined_audio.mp3", format='mp3')

        # Convert the combined audio to a moviepy AudioFileClip
        audio_clip = AudioFileClip("combined_audio.mp3")

        # Create a text clip for the title
        txt_clip = TextClip(self.title, fontsize=24, color='white', size=audio_clip.size)
        txt_clip = txt_clip.set_pos('center').set_duration(audio_clip.duration)

        # Create a video clip with the title text and combined audio
        video = CompositeVideoClip([txt_clip.set_audio(audio_clip)])
        
        # Define the output file path using os.path.join
        output_file_path = os.path.join(self.video_output_dir, "output_video.mp4")
        
        # Write the video file to the specified output directory
        video.write_videofile(output_file_path, fps=24)
        
        # Print a message indicating the video file has been created
        print(f"Video has been created and saved to {output_file_path}")
