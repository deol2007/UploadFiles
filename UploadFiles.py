import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token='t7QaD1nF_WsAAAAAAAAAAVLIPy8rKV6jZ6iic9nisTwGWUh8VNtE-ySmc8pQcZu2'
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer:")
    file_to=input("enter the full path to upload to dropbox:")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()