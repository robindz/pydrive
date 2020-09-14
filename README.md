# pydrive
Python program to download Google Drive files. Build with Python 3.8.1

# Prerequisites
1. Download and install Python: https://www.python.org/downloads/

2. Download and install the Google dependencies

    `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

3. [Enable the Google Drive API](https://developers.google.com/drive/api/v3/enable-drive-api)
4. Go to the `credentials` menu and click `CREATE CREDENTIALS`
5. Create a new OAuth client ID
6. In the `credentials` menu, the newly created OAuth client ID should be added to the OAuth 2.0 Client IDs list.
7. Download its data by either clicking the download icon on the right, or by clicking the edit button and then on the `DOWNLOAD JSON` button.
8. You now have two options:
    1. You save this file in the same directory as `pydrive.py` and `rename the file to 'client_secret.json`
    2. You pass the path of this json file when using the program using the optional `-c` or `--credentials` argument
    
# Usage
## First time usage
When using pydrive for the first time, you will have to authenticate with Google.

Add the `-c` or `--credentials` argument to specify the path to your client secret file if you did not follow step 6i.

A browser will open a you will be prompted to allow this application to authenticate using your account, accept.

### Example #1 (8i)
`python pydrive.py --id some_valid_id`

### Example #2 (8ii)
`python pydrive.py --id some_valid_id --credentials path_to_client_secret`

Your authentication data is stored in `token.pickle`, located in the same directory as `pydrive.py`. If this file is changed, deleted or damaged, you will have to go through the authentication process again.

## Normal usage
Currently, pydrive allows you to download Google Drive files based on their Google Drive file id. These can be found in the URLs of shareable links: `https://drive.google.com/file/<TYPE>/<FILE_ID>/view`

Optionally, you can rename the file using the optional `-n` or `--name` argument, this will also overwrite the file extension.
