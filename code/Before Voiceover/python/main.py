from audioDownloaderclass import AudioDownloader
from Transcribeclass import Transcribe
from getTokenclass import GetToken
import filepaths

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
                filepaths.token_path, filepaths.credentials_path, filepaths.local_folder_path)
            audio_downloader.download_audio()
        elif choice == '2':
            transcriber = Transcribe(
                filepaths.directory_path, filepaths.output_dir)
            transcriber.transcribe_files()
        elif choice == '3':
            token_getter = GetToken(
                filepaths.token_path, filepaths.credentials_path)
            token_getter.obtain_token()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
