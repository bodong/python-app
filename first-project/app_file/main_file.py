import file_service
import hello_file

if __name__ == "__main__":
    file_name = "mydata.csv"
    # file_service.write_file("mydata.csv")
    # file_service.read_file("mydata.csv")

    hello_file.os_util(file_name)