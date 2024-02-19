import json
import subprocess
import pandas as pd


class Export:
    @staticmethod
    def to_json(data, file_name):
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def to_excel(data, file_name):
        df = pd.DataFrame(data)
        try:
            df.to_excel(file_name, engine='openpyxl', index=False)
        except:
            print("Error while writing to Excel file.")

    @staticmethod
    def to_csv(data, file_name):
        df = pd.DataFrame(data)
        try:
            df.to_csv(file_name, index=False)
        except:
            print("Error while writing to CSV file.")


class Requirements:

    @staticmethod
    def install_requirements():
        try:
            subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
            print("Packages installed correctly.")
        except subprocess.CalledProcessError as e:
            print("Error while installing packages", e)
