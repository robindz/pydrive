import argparse
import sys
import os
from auth import auth
from drive import drive
from google.auth.exceptions import RefreshError
from googleapiclient.http import DEFAULT_CHUNK_SIZE

# Constant variables
SCOPES = ['https://www.googleapis.com/auth/drive']

# Make argparser
parser = argparse.ArgumentParser(description='Download Google Drive files with pydrive.')
parser.add_argument('-i', '--id', metavar='', type=str, help='id of the file', required=True)
parser.add_argument('-n', '--name', metavar='', type=str, help='output filename')
parser.add_argument('-c', '--credentials', metavar='', type=str, help='path to client secret file (default: client_secret.json)', default='client_secret.json')
parser.add_argument('-s', '--chunk-size', metavar='', type=int, help='chunk size used to download files in bytes (default: 100MB)',default=DEFAULT_CHUNK_SIZE)
parser.add_argument('-o', '--output-directory', metavar='', type=str, help='directory where files will be downloaded to')

args = parser.parse_args()

def main():
    drive_authorization = auth(SCOPES, args.credentials)
    drive_credentials = None
    try:
        drive_credentials = drive_authorization.get_credentials()
        drive_service = drive(drive_credentials)
        drive_service.download_file(args.id, args.name, args.chunk_size, args.output_directory)
    except FileNotFoundError as fnfe:
        print('\''+args.credentials+'\' was not found or is not a valid client secret file', file=sys.stderr)
    except RefreshError as rfe:
        print('An error occured whilst refreshing your credentials. If this issue persists, delete the \'token.pickle\' file and try again.', file=sys.stderr)

if __name__ == '__main__':
    main()