# Import necessary libraries and modules
import os
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# Import file path variables from filepaths.py
from filepaths import token_path, credentials_path, local_folder_path

class AudioDownloader:

    SCOPES = ['https://www.googleapis.com/auth/drive']

    def __init__(self, token_path, credentials_path, local_folder_path):
        self.token_path = token_path
        self.credentials_path = credentials_path
        self.local_folder_path = local_folder_path

    def authenticate(self):
        creds = None
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open(self.token_path, 'w') as token:
                token.write(creds.to_json())
        return creds

    def download_audio(self):
        creds = self.authenticate()
        service = build('drive', 'v3', credentials=creds)

        query = f"name = 'audio' and mimeType = 'application/vnd.google-apps.folder'"
        results = service.files().list(q=query, fields="files(id)").execute()
        items = results.get('files', [])

        if not items:
            print('No folder found.')
            return
        
        folder_id = items[0]['id']  # Get the first folder found

        query = f"'{folder_id}' in parents"
        results = service.files().list(q=query, fields="files(id, name)").execute()
        items = results.get('files', [])
        
        for item in items:
            request = service.files().get_media(fileId=item['id'])
            fh = io.FileIO(os.path.join(self.local_folder_path, item['name']), 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            print(f'Downloaded {item["name"]}')

            # Delete file from Google Drive after downloading
            service.files().delete(fileId=item['id']).execute()
            print(f'Deleted {item["name"]}')

# Update the __main__ section to use the imported file path variables
if __name__ == '__main__':
    audio_downloader = AudioDownloader(token_path, credentials_path, local_folder_path)
    audio_downloader.download_audio()