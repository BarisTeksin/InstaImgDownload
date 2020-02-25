from InstaImgDownload import login, DownloadProfilePhotos, DownloadTagPhotos
import sys

username = input('Instagram Username : ')
passwd = input('Instagram Password : ')
while True:
    download_username = input('Download Instagram Username : ')
    print("""
    ------------------------------------------------------
    1) Photo
    2) Tag Photo
    ------------------------------------------------------""")
    select = int(input('Select mode : '))
    try:
        if select == 1:
            login(username,passwd)
            DownloadProfilePhotos(download_username)
        elif select == 2:
            login(username,passwd)
            DownloadTagPhotos(download_username)
        else:
            print('Error failled select.')
    except ValueError:
        print('Please write only number.')
    control = input('Do you want to continue? (y/n) : ')
    
    if control == 'n' or control == 'N' or control == 'no' or control == 'NO':
        break
print('Quit now bot.')
sys.exit()
