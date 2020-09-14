from __future__ import print_function
import os.path
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

class drive:
    def __init__(self,creds):
        self.SERVICE = build('drive','v3',credentials=creds)

    def __get_file_info(self,file_id):
        return self.SERVICE.files().get(fileId=file_id).execute()

    def download_file(self,file_id,file_name,chunk_size,output_directory):
        file_info = self.__get_file_info(file_id)
        if file_name is None:
            file_name = file_info['name']

        if output_directory is not None and os.path.exists(output_directory):
            if output_directory.endswith('/'):
                file_name = output_directory + file_name
            else:
                file_name = output_directory + '/' + file_name

        request = self.SERVICE.files().get_media(fileId=file_id)
        fh = io.FileIO(file_name, 'wb')
        downloader = MediaIoBaseDownload(fh, request=request, chunksize=chunk_size)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print('Download %d%%.' % int(status.progress() * 100))
        