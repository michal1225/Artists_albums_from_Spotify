import json
import re
import subprocess
import pandas as pd


class Export:
    @staticmethod
    def to_json(data, file_name):
        pattern = r"\.json$"
        if re.search(pattern, file_name):
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print("File saved correctly")
        else:
            print("Invalid file name")
            return

    @staticmethod
    def to_excel(data, file_name):
        df = pd.DataFrame(data)
        pattern = r"\.xlsx$"
        if re.search(pattern, file_name):
            try:
                df.to_excel(file_name, engine='openpyxl', index=False)
                print("File saved correctly")
            except:
                print("Error while writing to Excel file.")
        else:
            print("Invalid file name")
            return

    @staticmethod
    def to_csv(data, file_name):
        df = pd.DataFrame(data)
        pattern = r"\.csv$"
        if re.search(pattern, file_name):
            try:
                df.to_csv(file_name, index=False)
                print("File saved correctly")
            except:
                print("Error while writing to CSV file.")
        else:
            print("Invalid file name")
            return


class Requirements:

    @staticmethod
    def install_requirements():
        try:
            subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
            print("Packages installed correctly.")
        except subprocess.CalledProcessError as e:
            print("Error while installing packages", e)
