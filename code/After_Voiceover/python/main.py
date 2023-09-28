from code.filepaths.filepaths import background_music_path, directory_path, video_output_dir
from code.After_Voiceover.python.GetTitleClass import GetTitle
from code.After_Voiceover.python.VideoBuilderClass import VideoBuilderClass
from code.After_Voiceover.python.GetThumbnailClass import GetThumbnailClass  # Import the GetThumbnailClass
from code.After_Voiceover.python.DisplayDetails import DisplayDetails

def main():
    title = ""
    thumbnail_path = ""  # Variable to store the thumbnail path
    while True:
        print("\n" + "="*25)
        print("1: Title")
        print("2: Build Video")
        print("3: Pick Thumbnail")
        print("4: Display Details")
        print("5: Exit")
        print("="*25 + "\n")

        choice = input("Enter your choice (1/2/3/4/5): ")

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
        elif choice == '4':  # Handle the new 'Display Details' option
            if not title or not thumbnail_path:
                print("Error: Missing some details. Make sure to set title and pick a thumbnail first.")
                continue
            display_details = DisplayDetails(title, thumbnail_path, video_output_dir)
            display_details.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
