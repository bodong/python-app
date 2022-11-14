import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = "Ia7jPziZQ8Ah6jge"
SECRET_KEY = "cgcefhWOh5QeqOal2kketli6Tiy7EhLT"
S3_URL = "http://localhost:9000"


def get_file_name_by_version(file_version):
    return "data/" + str(file_version) + ".csv"


def read_file(file_version):
    f = open(get_file_name_by_version(file_version), "r")
    contents = f.read()
    print(contents)
    f.close()


def upload_s3(file_type, file_version, bucket, file_name):
    s3 = boto3.client('s3', endpoint_url=S3_URL, aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file('data/' + str(file_type) + "/" + str(file_version) + ".csv", bucket, file_name)
        print("Upload successfully")
        return True
    except FileNotFoundError:
        print("File is not found")
        return False
    except NoCredentialsError:
        print("Creds is not available")
        return False
