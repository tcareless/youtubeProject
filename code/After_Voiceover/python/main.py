from code.filepaths.filepaths import background_music_path, directory_path, video_output_dir
from code.After_Voiceover.python.GetTitleClass import GetTitle
from code.After_Voiceover.python.VideoBuilderClass import VideoBuilderClass

def main():
    title = ""
    while True:
        print("\n" + "="*25)
        print("1: Title")
        print("2: Build Video")
        print("3: Exit")
        print("="*25 + "\n")

        choice = input("Enter your choice (1/2/3): ")

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
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
