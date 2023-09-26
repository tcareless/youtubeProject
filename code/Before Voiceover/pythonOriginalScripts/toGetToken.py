import os
from google_auth_oauthlib.flow import InstalledAppFlow

def main():
    # If modifying these SCOPES, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/drive']
    
    token_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/token.json'
    credentials_path = '/home/tyler/Desktop/youtubeProject/code/Before Voiceover/python/credentials.json'

    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

if __name__ == '__main__':
    main()
