import pickle
import os.path
import io
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class auth:
    def __init__(self,SCOPES,CLIENT_SECRET_FILE=''):
        self.SCOPES = SCOPES
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE
    
    def get_credentials(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        else:
            print('token.pickle doesn\'t exist, requesting new credentials...')
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print('Previous credentials have expired, refreshing...')
                creds.refresh(Request())
            else:
                print('Using','\''+self.CLIENT_SECRET_FILE+'\'','as client secret file.')
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CLIENT_SECRET_FILE, self.SCOPES)
                creds = flow.run_console()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds
        