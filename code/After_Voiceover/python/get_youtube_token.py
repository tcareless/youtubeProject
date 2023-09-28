from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def main():
    """Shows basic usage of the YouTube API.
    Calls the YouTube Data API to retrieve the video and channel information
    for a video and displays the results.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/tyler/Desktop/youtubeProject/code/After_Voiceover/python/client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

if __name__ == '__main__':
    main()
