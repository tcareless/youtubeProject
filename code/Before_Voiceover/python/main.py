from code.filepaths.filepaths import token_path, credentials_path, local_folder_path, directory_path, output_dir

from code.Before_Voiceover.python.audioDownloaderclass import AudioDownloader
from code.Before_Voiceover.python.getTokenclass import GetToken
from code.Before_Voiceover.python.Transcribeclass import Transcribe


def main():
    while True:
        print("\n" + "="*25)
        print("1: Download audio files from Drive")
        print("2: Transcribe audio files")
        print("3: Obtain Google Drive token")
        print("4: Exit")
        print("="*25 + "\n")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            audio_downloader = AudioDownloader(
                token_path, credentials_path, local_folder_path)  # Updated
            audio_downloader.download_audio()
        elif choice == '2':
            transcriber = Transcribe(
                directory_path, output_dir)  # You need to ensure directory_path and output_dir are defined
            transcriber.transcribe_files()
        elif choice == '3':
            token_getter = GetToken(
                token_path, credentials_path)  # Updated
            token_getter.obtain_token()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
