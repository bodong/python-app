import file_service


if __name__ == "__main__":
    file_version = "v1"

    file_service.upload_s3(file_version, "test-bucket-ref", "something.csv")