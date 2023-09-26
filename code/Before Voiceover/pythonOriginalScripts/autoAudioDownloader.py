import os
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds = None
    token_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/token.json'
    credentials_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/credentials.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    # Call the Drive v3 API
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
    
    local_folder_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/'
    
    for item in items:
        request = service.files().get_media(fileId=item['id'])
        fh = io.FileIO(os.path.join(local_folder_path, item['name']), 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        print(f'Downloaded {item["name"]}')

        # Delete file from Google Drive after downloading
        service.files().delete(fileId=item['id']).execute()
        print(f'Deleted {item["name"]}')

if __name__ == '__main__':
    main()