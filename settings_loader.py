"""
Includes class SettingLoader.
"""

import json
class SettingLoader:
    """
    Loads ini file.
    """
    def __init__(self, path_csv="none", path_json="none", encoding="none", fname="none"):
        self.__path_csv = path_csv
        self.__path_json = path_json
        self.__encoding = encoding
        self.__fname = fname

    def set_path_csv(self, value):
        """
        Sets value of path_scv.
        """
        self.__path_csv = value

    def set_path_json(self, value):
        """
        Sets value of path_json.
        """
        self.__path_json = value

    def set_encoding(self, value):
        """
        Sets value of encoding.
        """
        self.__encoding = value

    def set_fname(self, value):
        """
        Sets value of fname.
        """
        self.__fname = value

    def get_path_csv(self):
        """
        Gets value of path_scv.
        """
        return self.__path_csv

    def get_path_json(self):
        """
        Gets value of path_json.
        """
        return self.__path_json

    def get_encoding(self):
        """
        Gets value of encoding.
        """
        return self.__encoding

    def get_fname(self):
        """
        Gets value of fname.
        """
        return self.__fname

    def load_ini(self, path):
        """
        Loads ini file content.
        """
        print("ini " + path + ":", end=" ")
        with open(path, "r", encoding="utf-8") as f:
            text = json.load(f)
            self.__path_csv = text["input"]["csv"]
            self.__path_json = text["input"]["json"]
            self.__encoding = text["input"]["encoding"]
            self.__fname = text["output"]["fname"]
            print("OK")

    def check_settings(self):
        """
        Checks if path to csv, path to json and encoding are not none.
        """
        if self.__path_csv != "none" and self.__path_json != "none" and self.__encoding != "none" \
                and self.__fname != "none":
            return True
        else:
            return False


