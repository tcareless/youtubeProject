# Import necessary libraries and modules
import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Import file path variables from filepaths.py
from code.filepaths.filepaths import token_path, credentials_path

# Define the GetToken class
class GetToken:
    SCOPES = ['https://www.googleapis.com/auth/drive']

    def __init__(self, token_path, credentials_path):
        self.token_path = token_path
        self.credentials_path = credentials_path

    def obtain_token(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            self.credentials_path, self.SCOPES)
        creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(self.token_path, 'w') as token:
            token.write(creds.to_json())

# Update the __main__ section to use the imported file path variables
if __name__ == '__main__':
    token_getter = GetToken(token_path, credentials_path)
    token_getter.obtain_token()
