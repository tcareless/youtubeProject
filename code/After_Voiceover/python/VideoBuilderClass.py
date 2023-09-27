import os
from moviepy.editor import concatenate_audioclips, TextClip, CompositeVideoClip, AudioFileClip
from pydub import AudioSegment
from code.filepaths.filepaths import voiceover_output_dir, background_music_path, video_output_dir
from GetTitleClass import GetTitle




class VideoBuilderClass:
    def __init__(self, voiceover_output_dir, background_music_path, title_getter, video_output_dir):
        self.voiceover_dir = voiceover_output_dir  # path to the voiceover directory
        self.background_music_path = background_music_path  # path to the background music file
        self.title_getter = title_getter  # instance of GetTitle class
        self.video_output_dir = video_output_dir  # path to the video output directory


    def get_voiceover_file(self):
        for filename in os.listdir(self.voiceover_dir):
            if filename.endswith('.m4a'):
                return os.path.join(self.voiceover_dir, filename)
        print("No .m4a file found in the specified directory.")
        return None
    
    def build_video(self):
        # Get the title for the video
        self.title_getter.prompt_for_title()
        self.title = self.title_getter.get_current_title()

        # Get the path to the voiceover file
        self.voiceover_file = self.get_voiceover_file()
        if self.voiceover_file is None:
            return  # Exit if no voiceover file is found

        try:
            # Load audio files
            print("Loading audio files...")
            voiceover_audio = AudioSegment.from_file(self.voiceover_file)
            background_music_audio = AudioSegment.from_file(self.background_music_path)
            print("Audio files loaded successfully.")
        except Exception as e:
            print(f"Error loading audio files: {e}")
            return

        try:
            # Trim the longer audio file to match the length of the shorter audio file
            print("Trimming audio files...")
            min_length = min(len(voiceover_audio), len(background_music_audio))
            voiceover_audio = voiceover_audio[:min_length]
            background_music_audio = background_music_audio[:min_length]
            print("Audio files trimmed successfully.")
        except Exception as e:
            print(f"Error trimming audio files: {e}")
            return

        try:
            # Overlay the two audio files
            print("Overlaying audio files...")
            combined_audio = voiceover_audio.overlay(background_music_audio)
            print("Audio files overlayed successfully.")
        except Exception as e:
            print(f"Error overlaying audio files: {e}")
            return

        try:
            # Export the combined audio to a temporary file
            print("Exporting combined audio...")
            combined_audio.export("combined_audio.mp3", format='mp3')
            print("Combined audio exported successfully.")
        except Exception as e:
            print(f"Error exporting combined audio: {e}")
            return

        try:
            # Convert the combined audio to a moviepy AudioFileClip
            print("Converting audio to moviepy AudioFileClip...")
            audio_clip = AudioFileClip("combined_audio.mp3")
            print("Conversion successful.")
        except Exception as e:
            print(f"Error converting audio: {e}")
            return

        try:
            # Create a text clip for the title
            print("Creating text clip...")
            txt_clip = TextClip(self.title, fontsize=28, color='#F5F5F5', font='DejaVu-Sans', size=(1920, 1080))
            txt_clip = txt_clip.set_pos('center').set_duration(audio_clip.duration)
            print("Text clip created successfully.")
        except Exception as e:
            print(f"Error creating text clip: {e}")
            return

        try:
            # Create a video clip with the title text and combined audio
            print("Creating video clip...")
            video = CompositeVideoClip([txt_clip.set_audio(audio_clip)])
            print("Video clip created successfully.")
        except Exception as e:
            print(f"Error creating video clip: {e}")
            return

        try:
            # Define the output file path using os.path.join
            output_file_path = os.path.join(self.video_output_dir, "output_video.mp4")
                
            # Write the video file to the specified output directory
            print(f"Writing video file to {output_file_path}...")
            video.write_videofile(output_file_path, fps=24)
                
            # Print a message indicating the video file has been created
            print(f"Video has been created and saved to {output_file_path}")
                
            # Delete the voiceover file
            print(f"Deleting voiceover file {self.voiceover_file}...")
            os.remove(self.voiceover_file)
            print(f"Voiceover file {self.voiceover_file} deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")

        try:
            # Delete the combined audio file
            print("Deleting combined audio file combined_audio.mp3...")
            os.remove("combined_audio.mp3")
            print("Combined audio file deleted successfully.")
        except Exception as e:
            print(f"Error deleting combined audio file: {e}")

if __name__ == '__main__':
    title_getter = GetTitle() # Create an instance of GetTitle
    video_builder = VideoBuilderClass(voiceover_output_dir, background_music_path, title_getter, video_output_dir)
    video_builder.build_video()

