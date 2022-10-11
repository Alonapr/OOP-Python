"""
Main module.
Uses all the data received earlier, ensures running the program from console.
Contains such functions: executor_info(), laboratory_task(), process(path).
"""

from sys import argv
from info import Info
from load import Builder
from settings_loader import SettingLoader

def executor_info():
    """
    Prints information about executor.
    """
    name = "Alona Predkova"
    print("This program is coded by " + name)

def laboratory_task():
    """
    Prints information about task of laboratory.
    """
    variant = "138"
    print("Variant № " + variant)
    print("This program processes the data of the semester journal of inspections of student attendance by the deanery"
          "\nand captures absent.")

def process(path):
    """
    Main function.
    Reads loaded in class SettingLoader ini file and processes information.
    """
    try:
        settings = SettingLoader()
        settings.load_ini(path)
        if settings.check_settings():
            info = Info()
            builder = Builder()
            builder.load(info, settings.get_path_csv(), settings.get_path_json(), settings.get_encoding())
            info.parse_data()
            info.processing(settings.get_fname())
    except BaseException:
        print("\n***** program aborted *****")

if __name__ == "__main__":
    executor_info()
    laboratory_task()
    print("*****")
    if len(argv) == 2:
        process(argv[1])
    else:
        print("***** program aborted *****")
