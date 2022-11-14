import datetime
import os
from os import path
from datetime import date, time, timedelta
import time


def os_util(file_name):
    print(os.name)

    print("Item exists: " + str(path.exists(file_name)))
    print("Item is file: " + str(path.isfile(file_name)))
    print("Item is dir: " + str(path.isdir(file_name)))

    print("Item path: ", path.realpath(file_name))
    print("Item path and name: ", path.split(path.realpath(file_name)))