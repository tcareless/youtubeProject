import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from code.filepaths.filepaths import token_path, client_secrets_path

class YoutubeUploader:
    def __init__(self, title, description, thumbnail_path, video_path):
        self.title = title
        self.description = description
        self.thumbnail_path = thumbnail_path
        self.video_path = video_path
        self.youtube = None

    def authenticate(self):
        # Check if token.json is available to authenticate, else request user for authentication
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, scopes=["https://www.googleapis.com/auth/youtube.upload"])
            creds = flow.run_local_server(port=0)
            with open(token_path, 'w') as token_file:
                token_file.write(creds.to_json())

        self.youtube = build("youtube", "v3", credentials=creds)

    def upload_video(self):
        request_body = {
            'snippet': {
                'title': self.title,
                'description': self.description,
                'categoryId': '24'  # Assuming the category is People & Blogs, change this as per your requirement
            },
            'status': {
                'privacyStatus': 'private'  # Setting video privacy to private, change this as per your requirement
            }
        }

        media = MediaFileUpload(self.video_path, chunksize=-1, resumable=True)
        request = self.youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        )

        response = request.execute()

        # Uploading thumbnail after video upload
        video_id = response['id']
        self.upload_thumbnail(video_id)

        print(f'Video uploaded successfully: {response}')

    def upload_thumbnail(self, video_id):
        request = self.youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(self.thumbnail_path)
        )
        response = request.execute()
        print(f'Thumbnail uploaded successfully: {response}')

# Usage example:
if __name__ == "__main__":
    uploader = YoutubeUploader('Test Title', 'Test Description', 'thumbnail.jpg', 'video.mp4')
    uploader.authenticate()
    uploader.upload_video()
