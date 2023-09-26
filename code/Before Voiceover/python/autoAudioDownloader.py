from google.oauth2 import service_account
from googleapiclient.discovery import build

# Specify the paths to your credentials and where you want to store the token
credentials_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/credentials.json'
token_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/token.json'

creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        creds = service_account.Credentials.from_service_account_file(
            credentials_path,  # Use the actual path to your credentials file
            scopes=SCOPES
        )
    # Save the credentials for the next run
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

# Build the service
service = build('drive', 'v3', credentials=creds)
