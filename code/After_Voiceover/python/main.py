from code.filepaths.filepaths import (
    background_music_path,
    directory_path,
    video_output_dir,
    credentials_path,
    token_path,
    source_dir,
    backup_dir
)
from code.After_Voiceover.python.GetTitleClass import GetTitle
from code.After_Voiceover.python.VideoBuilderClass import VideoBuilderClass
from code.After_Voiceover.python.GetThumbnailClass import GetThumbnailClass  # Import the GetThumbnailClass
from code.After_Voiceover.python.DisplayDetails import DisplayDetails
from code.After_Voiceover.python.GetDescriptionClass import DescriptionGetter  # Import DescriptionGetter
from code.After_Voiceover.python.YoutubeUploader import YoutubeUploader  # Import YoutubeUploader
from code.After_Voiceover.python.BackupCleanup import BackupCleanup  # Import BackupCleanup
import os

def main():
    title = ""
    thumbnail_path = ""  # Variable to store the thumbnail path
    description = ""  # Variable to store the video description
    video_path = " "  # Variable to store video
    backup_cleanup = BackupCleanup(source_dir, backup_dir)  # Create an instance of BackupCleanup

    while True:
        print("\n" + "="*25)
        print("1: Title")
        print("2: Build Video")
        print("3: Pick Thumbnail")
        print("4: Enter Description")
        print("5: Display Details")
        print("6: Post to YouTube")
        print("7: Backup and Cleanup")  # New option for Backup and Cleanup
        print("8: Exit")  # Updated Exit option number
        print("="*25 + "\n")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")  # Updated choice prompt


        if choice == '1':
            get_title = GetTitle()
            get_title.prompt_for_title()
            title = get_title.get_current_title()
        elif choice == '2':
            if not title:
                print("Error: You need to set a title first.")
                continue
            video_builder = VideoBuilderClass(title, directory_path, background_music_path, video_output_dir)
            video_builder.build_video()
        elif choice == '3':  # Handle the new 'Pick Thumbnail' option
            thumbnail_getter = GetThumbnailClass()
            thumbnail_getter.choose_random_thumbnail()
            thumbnail_path = thumbnail_getter.get_thumbnail_path()
            if thumbnail_path:  # Ensure a thumbnail was successfully chosen
                print(f'Thumbnail chosen: {thumbnail_path}')
            else:
                print('No thumbnail chosen.')
        elif choice == '4':  # Handle the new 'Enter Description' option
            description_getter = DescriptionGetter()
            description_getter.prompt_for_description()
            description = description_getter.get_description()

        elif choice == '5':  # Adjusted option number for 'Display Details'
            if not (title and thumbnail_path and description):
                print("Error: Missing some details. Make sure to set title, pick a thumbnail, and enter a description first.")
                continue
            display_details = DisplayDetails(title, thumbnail_path, video_output_dir, description)
            display_details.display()

        elif choice == '6':  # New 'Post to YouTube' option
            if not (title and thumbnail_path and description):
                print("Error: Missing some details. Make sure to set title, pick a thumbnail, and enter a description first.")
                continue

            # Check the directory for a video file
            video_files = [f for f in os.listdir(video_output_dir) if f.endswith('.mp4')]
            if not video_files:  # If no video files are found
                print("Error: No video file found in the specified directory.")
                continue
            elif len(video_files) > 1:  # If multiple video files are found
                print("Error: Multiple video files found. Please ensure only the desired video file is in the directory.")
                continue
            else:
                video_path = os.path.join(video_output_dir, video_files[0])  # Set the video path to the found video file
            youtube_uploader = YoutubeUploader(
                title,
                description,
                thumbnail_path,
                video_path
            )
            youtube_uploader.authenticate()
            youtube_uploader.upload_video()
        elif choice == '7':  # New option for Backup and Cleanup
            backup_cleanup.move_and_delete_files()
        elif choice == '8':  # Updated Exit option number
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()