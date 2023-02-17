from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import datetime, os
import calendar
import configparser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-o", "--option", default="UPDATE", help="Option [UPDATE] or [SHOW]")
parser.add_argument("-d", "--days", default=3, type=int, help="Number de days to check event after now")
args = vars(parser.parse_args())

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Customize it
# TODO
PATH_GPOLY = '/home/jeferson/git/gfeed/configs/'
USER = os.environ.get('USER')

def createToken():

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


def getAllEvents(creds) -> None:

    # Get list of calendars
    if creds != None:
        service = build('calendar', 'v3', credentials=creds)
        page_token = None
        IdList = []
        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                IdList.append(calendar_list_entry['id'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break

        eventList = [] 
#        now = datetime.datetime.utcnow()
        now = datetime.datetime.utcnow()

        for ID in IdList:
            page_token = None
            while True:
                events= service.events().list(
                        calendarId=ID,
                        singleEvents=True,
                        orderBy='startTime',
                        timeMin= now.isoformat() + 'Z',
                        timeMax= (
                            now + 
                            datetime.timedelta(days= args['days'])).isoformat() + 'Z',
                        ).execute()
                for event in events['items']:
                    eventList.append(event)
                page_token = events.get('nextPageToken')
                if not page_token:
                    break
        eventList = sorted(eventList,
                           key=lambda x: 
                          datetime.datetime.strptime(x['start']['dateTime'][:-9],
                                                     '%Y-%m-%dT%H:%M')
                           )

        with open(PATH_GPOLY + 'feedCalendar.txt', 'w') as feedCal:
            for ev in eventList:
                strPoly = formatString(ev)
                feedCal.write(strPoly)
#        import pdb; pdb.set_trace()
        if not eventList:
            print("Enjoy your day!!!")
        else:
            print(formatString(eventList[0])[:-1])
    else:
        print("Cannot be get the credentials!")


def formatString(event):

    dt = event["start"]["dateTime"][:-9]
    dt = datetime.datetime.strptime(dt, '%Y-%m-%dT%H:%M')
    strPoly = calendar.day_name[ dt.weekday() ][:3] + " at "
    strPoly += dt.strftime("%H:%M") + " "
    strPoly += event["summary"] + "\n"

    return strPoly


def showEvents():

    config = configparser.ConfigParser()

    if os.path.exists(PATH_GPOLY + 'showOptions.cfg'):

        config.read(PATH_GPOLY + 'showOptions.cfg')
        countLine =  int(config['DEFAULT']['eventcount'])
        eventSize = int(config['DEFAULT']['eventsize'])
       
        countLine = countLine + 1
        if countLine >= eventSize:
            countLine = 0
  
        with open(PATH_GPOLY + 'feedCalendar.txt', 'r') as feedCal:
            calendarEvent = feedCal.readlines()[countLine]

        config['DEFAULT']['eventcount'] = str(countLine)
        config['TOKEN'] = {'id': ''}

        with open(PATH_GPOLY + 'showOptions.cfg', 'w') as configfile:
            config.write(configfile)

    else:
        with open(PATH_GPOLY + 'feedCalendar.txt', 'r') as feedCal:
            countLine = len(feedCal.readlines())
            feedCal.seek(0)
            calendarEvent = feedCal.readlines()[0]

        config['DEFAULT'] = {'eventsize': countLine,
                             'eventcount': 0,
                             }
        config['TOKEN'] = {'id': ''}
        with open(PATH_GPOLY + 'showOptions.cfg', 'w') as configfile:
            config.write(configfile)
    print(calendarEvent[:-1])


if __name__ == '__main__':
    if args['option'] == 'UPDATE':
        creds = createToken() 
        getAllEvents(creds)
    elif args['option'] == 'SHOW':
        showEvents()
    else:
        print("Please type getEvent.py -h")
