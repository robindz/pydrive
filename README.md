# pydrive (en)
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
    1. You save this file in the same directory as `pydrive.py` and `rename the file to 'client_secret.json'`
    2. You pass the path of this json file when using the program using the optional `-c` or `--credentials` argument
    
# Usage
## First time usage
When using pydrive for the first time, you will have to authenticate with Google.

Add the `-c` or `--credentials` argument to specify the path to your client secret file if you did not follow step 6i.

A browser will open a you will be prompted to allow this application to authenticate using your account, accept.

### Example #1 (8i)
`python pydrive.py --id some_valid_id`

### Example #2 (8ii)
`python pydrive.py --id some_valid_id --credentials path/to/client_secret`

Your authentication data is stored in `token.pickle`, located in the same directory as `pydrive.py`. If this file is changed, deleted or damaged, you will have to go through the authentication process again.

## Normal usage
Currently, pydrive allows you to download Google Drive files based on their Google Drive file id. These can be found in the URLs of shareable links: `https://drive.google.com/file/<TYPE>/<FILE_ID>/view`

Optionally, you can rename the file using the optional `-n` or `--name` argument, this will also overwrite the file extension.

Note, if you are remoted into a terminal you will have to use the `--no-localhost` option to authenticate.

## pydrive (ko)
구글드라이브의 파일을 다운로드 할 수 있는 프로그램입니다. 파이썬 3.8.1 버전 이상 설치하시길 권장합니다.

## 사전작업
1. 파이썬을 다운로드 하고 인스톨 합니다. https://www.python.org/downloads/

2. 구글 종속성 파이썬 라이브러리를 설치합니다.

    `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

3. [구글드라이브 api를 설정 하기 위해 링크를 클릭합니다.](https://developers.google.com/drive/api/v3/enable-drive-api)
4. `Google API Console`링크를 클릭합니다. 그리고 `ENABLE APIS AND SERVICCES` 링크를 눌러줍니다.
    * 프로젝트가 없다면 프로젝트를 만들어주셔야 합니다. 우측 상단 `프로젝트 만들기` 를 통해 프로젝트를 만들어줍니다. 그런다음 4번 스텝을 따르시기 바랍니다.
5. `Google Drive API` 검색후 해당 API를 페이지로 이동한 뒤 `사용` 버튼을 눌러줍니다.
6. 좌측에 `사용자 인증 정보` 페이지에 접속후 상단 `사용자 인증 정보 만들기`에서 `OAuth 클라이언트 ID` 를 클릭하여 만들어줍니다.
    * 처음 만들경우 동의화면 구성을 추가적으로 해줘야 합니다. User Type 에서 `외부` 를 선택해주세요. 그리고 어플정보를 간단하게 기입하여 생성해주세요.
    * 클라이언트 ID만들기 페이지에서 애플리케이션 유형은 `데스크톱 앱`으로 선택하시고 이름은 원하시는 이름대로 생성하세요.
7. 생성한 데스크톱 Oauth 페이지로 이동한 뒤 상단 `JSON 다운로드` 버튼을 통해 해당 파일을 받아줍니다.
8. 여기에서 두가지 선택옵션중에 하나를 선택하여 진행해주세요.
    1. 다운로드한 json 파일의 이름을 `client_secret.json`으로 변경한 뒤 `pydrive.py` 파일과 동일한 위치에 둡니다.
    2. 다운로드한 파일및 파일명의 위치를 기억한뒤 이 프로그램의 옵션 `-c`또는 `--credentials`를 이용하여 json파일의 위치를 잡아줍니다.
        `e.g) --credentials /home/pi/client_secret.json`

# 사용법
## 첫 실행일 경우
만약 pydrive를 처음 실행한다면 구글에 계정을 인증하는 과정이 필요합니다.

위 사전작업의 8번 항목중에 한가지 방법으로 구글계정에 로그인해야합니다.

해당 프로그램을 첫 실행시 프로그램은 구글에 로그인하는 링크를 줄 것이고 해당 링크를 브라우저에서 실행한다음 로그인하시면 됩니다.

### Example #1 (8-i)
`python pydrive.py --id some_valid_id`

### Example #2 (8-ii)
`python pydrive.py --id some_valid_id --credentials path/to/client_secret`

### Example #3 파이선을 구동하는 컴퓨터와 로그인하는 컴퓨터가 다를경우
`python pydrive.py --id some_valid_id --no-localhost`

`python pydrive.py --id some_valid_id --credentials path/to/client_secret --no-localhost`

인증된 데이터는 `pydrive.py`과 같은 디렉토리에 있는 `token.pickle` 파일에 저장됩니다. 이 파일이 변경되거나 삭제된다면 인증절차를 다시 거쳐야 합니다.

## 정상적인 작동법
Pydrive는 Google Drive의 파일 `ID(고유값)`를 기반으로  Google Drive에서 파일을 다운로드 합니다.

이 아이디 값은 구글드라이브 공유 링크에서 찾을 수 있습니다.

`https://drive.google.com/file/<파일 타입>/<파일_ID(이거를 복사하세요)>/view`

선택적으로 `-n` 또는 `--name` 옵션를 사용하여 파일이름을 변경할 수 있으며 파일 확장자명을 덮어씌울수도 있습니다. 따라서 `-n` 옵션을 사용시 확장자가 없도록 파일이름을 설정하면 확장자명이 지워져버릴 수 있습니다. 확장자가 필요하다면 꼭 기제 해주세요.

#### 확장자가 필요 없는 경우
`e.g) --name 151128 MBC 음악중심 트와이스-우아하게`

#### 확장자가 필요 한 경우
`e.g) --name 151128 MBC 음악중심 트와이스-우아하게.tp`

추가로 프로그램을 사용하는 서버와 다른 컴퓨터에서 로그인 할 경우 `--no-localhost` 옵션을 추가하여 인증하시기 바랍니다. 이 경우 로그인 이후 나오는 인증값을 터미널에 입력해주시면 됩니다.