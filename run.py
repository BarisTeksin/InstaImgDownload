from InstaImgDownload import login, DownloadProfilePhotos, DownloadTagPhotos

username = input('Instagram Username : ')
passwd = input('Instagram Password : ')
download_username = input('Download Instagram Username : ')
download_post_count = int(input('Download Instagram User post count : '))


login(username,passwd)

DownloadProfilePhotos(download_username,download_post_count)
