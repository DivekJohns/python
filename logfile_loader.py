# # -----------------------------------------------------
# # Module name: logfile_loader
# # Developed by Divek John.
# # File to download text file from S3 bucket within given dates
# -----------------------------------------------------

import os
from dotenv import load_dotenv
import boto3
from io import BytesIO
from gzip import GzipFile
import datetime

load_dotenv('../.env')


class AwsS3Client:
    def __init__(self):
        self.s3client = boto3.client(
            's3',
            region_name=os.getenv("aws_region"),
            aws_access_key_id=os.getenv("aws_access_key_id"),
            aws_secret_access_key=os.getenv("aws_secret_access_key"),
        )


class TextFileLoader(AwsS3Client):
    def __init__(self, bucket_name, log_folder, start_date_time, end_date_time):
        super().__init__()
        self.files = [];
        try:
            file_lists = boto3.resource('s3',
                                        aws_access_key_id=os.getenv("aws_access_key_id"),
                                        aws_secret_access_key=os.getenv("aws_secret_access_key"),
                                        ).Bucket(bucket_name)
            file_lists = file_lists.objects.filter(Prefix=log_folder)
            for file in file_lists:
                if start_date_time < file.last_modified.replace(tzinfo=None) < end_date_time:
                    file_object = self.s3client.get_object(Bucket=bucket_name, Key=file.key)
                    file_data = BytesIO(file_object['Body'].read())
                    self.files.append(GzipFile(None, 'rb', fileobj=file_data).read().decode('utf-8'))
        except Exception as error:
            print(' - Exception Thrown -')
            print(error)


if __name__ == '__main__':
    log_files = TextFileLoader('bucket name',
                              'folder to check files on given dates', datetime.datetime(year=2020, month=3, day=16, hour=15),
                              datetime.datetime.now()).files
    print('%s files were found' % len(log_files))
    for file in log_files:
        print('++++++++++++++++++++++++++++++ File Start ++++++++++++++++++++++++++++++')
        print(file)
        print('--------------------------------------- EOF ---------------------------------------')
