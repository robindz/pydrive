import argparse
import sys
import os
from auth import auth
from drive import drive
from google.auth.exceptions import RefreshError

# Constant variables
SCOPES = ['https://www.googleapis.com/auth/drive']

# Make argparser
parser = argparse.ArgumentParser(description='Download Google Drive files with pydrive.')
parser.add_argument('-i', '--id', metavar='', type=str, help='id of the file', required=True)
parser.add_argument('-n', '--name', metavar='', type=str, help='output filename', default='')
parser.add_argument('-c', '--credentials', metavar='', type=str, help='path to client secret file (default client_secret.json)', default='client_secret.json')

args = parser.parse_args()

def main():
    drive_authorization = auth(SCOPES, args.credentials)
    drive_credentials = None
    try:
        drive_credentials = drive_authorization.get_credentials()
        drive_service = drive(drive_credentials)
        drive_service.download_file(args.id, args.name)
    except FileNotFoundError as fnfe:
        print('\''+args.credentials+'\' was not found or is not a valid client secret file', file=sys.stderr)
    except RefreshError as rfe:
        print('An error occured whilst refreshing your credentials. If this issue persists, delete the \'token.pickle\' file and try again.', file=sys.stderr)

if __name__ == '__main__':
    main()