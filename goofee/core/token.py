
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class ToknTest():

    def __init__(self):

    # check if exist the temporary folder
    creds = None
    if os.path.exists(PATH_GPOLY + 'token.json'):
        creds = Credentials.from_authorized_user_file(PATH_GPOLY + 'token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    '/home/'+ USER + '/.google_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(PATH_GPOLY + 'token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print('An error occurred: %s' % error)
    return creds
