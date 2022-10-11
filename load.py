"""
Includes class Builder.
"""

import csv
import json

from info import Info

class Builder:
    """
    Loads csv and json files content,
    checks the files for compliance.
    """
    def __init__(self, row_num=0, lecture_num=0):
        self.__row_num = row_num
        self.__lecture_num = lecture_num

    def load_data(self, info: Info, csv_path: str, encoding: str):
        """
        Loads scv file content
        and converts rows in it to object info.
        """
        arr2 = []
        print("input-csv " + csv_path + ":", end=" ")
        with open(csv_path, newline="", encoding=encoding) as f:
            reader = csv.reader(f)
            for row in reader:
                curr_row = row[0].split(";")
                arr2.extend([curr_row])
            info.set_information(arr2)
            print("OK")

    def load_stat(self, json_path: str, encoding: str):
        """
        Loads json file content.
        """
        print("input-json " + json_path + ":", end=" ")
        with open(json_path, 'r', encoding=encoding) as f:
            text = json.load(f)
            self.__lecture_num = text["number of lectures"]
            self.__row_num = text["number of rows"]
            print("OK")

    def fit(self, info: Info):
        """
        Checks if number of lectures and number of rows in csv file
        coincide with respectively number of lectures and number of rows from json file.
        """
        if info.lecture_count() == self.__lecture_num and info.info_count()+1 == self.__row_num :
            return True
        else:
            return False

    def load(self, info: Info, csv_path: str, json_path: str, encoding: str):
        """
        Prints if csv and json content coincide or not.
        """
        self.load_data(info, csv_path, encoding)
        self.load_stat(json_path, encoding)
        print("json?=csv:", end=" ")
        if self.fit(info):
            print("OK")
        else:
            print("UPS")
