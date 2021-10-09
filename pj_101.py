	import dropbox
class TransferData:
    def token(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
    f = open("E:/imtiyaz's project folder/pj_101", 'rb')
    dbx.files_upload(f.read(), "E:/imtiyaz's project folder/pj_101")
    def main():
        access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
        transferData = TransferData(access_token)
        file_from = input("E:/imtiyaz's project folder/pj_101")
        file_to = input("E:/imtiyaz's project folder/pj_101") 
        # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
# API v2
        transferData.upload_file(file_from, file_to)
        print("file has been moved !!!")