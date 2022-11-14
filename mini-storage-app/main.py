import function.s3_file_service as s3

file_type = "payment"
file_version = "v1"
file_final_name = "testv1.csv"
bucket = "test-bucket-ref"

if __name__ == "__main__":
    s3.upload_s3(file_type, file_version, bucket, file_final_name)
