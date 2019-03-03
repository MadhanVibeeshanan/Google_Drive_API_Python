from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'drive-python-quickstart.json')
    # A oauth2client.client.Storage object stores and retrieves Credentials objects. This section describes the various methods to create and use Storage objects
    store = Storage(credential_path)
    credentials = store.get()
    
    """
    The purpose of a Flow class is to acquire credentials that authorize your application access to user data.
        In order for a user to grant access, OAuth 2.0 steps require your application to potentially redirect their browser multiple times.
        A Flow object has functions that help your application take these steps and acquire credentials.
        Flow objects are only temporary and can be discarded once they have produced credentials, but they can also be pickled and stored.
        This section describes the various methods to create and use Flow objects.
    """
    
    if not credentials or credentials.invalid:
        # The oauth2client.client.flow_from_clientsecrets() method creates a Flow object from a client_secrets.json file. 
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Drive API.
    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    #Use the authorize() function of the Credentials class to apply necessary credential headers to all requests made by an httplib2.Http instance
    http = credentials.authorize(httplib2.Http())
    #Once an httplib2.Http object has been authorized, it is typically passed to the build function
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    main()
