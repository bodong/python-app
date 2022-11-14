def write_file(file_name):
    print("writing file")
    f = open(file_name, "w+")

    for i in range(10):
        f.write("data " + str(i) + "\r\n")

    f.close()

def read_file(file_name):
    f = open(file_name, "r")
    contents = f.read()
    print(contents)
    
    # lines = f.readlines()
    # for c in lines:
        # print(c)


