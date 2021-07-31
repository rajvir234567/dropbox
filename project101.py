import dropbox

class UploadData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.A1E9sIe4_opMJU7lihrm_nYx4DVnOjR3E3ucNQ7IsdbE6CMBgQQJfL6G7fdRvSV0i9f54peL0N2VaQPjz8DTrO6q9QIDlUeiNsoePwixTvdnVfpGIr0O7U8IWv83yxfk53kIT4GyC4g"
    uploadData = UploadData(access_token)
    file_from = "file1.txt"
    file_to = "/test_dropbox/file1.txt"
    uploadData.upload_file(file_from,file_to)

main()