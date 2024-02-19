import json
import subprocess
import pandas as pd


class Export:
    @staticmethod
    def to_json(data, file_name):
        if file_name[-1] == 'n' and file_name[-2] == 'o' and file_name[-3] == 's' and file_name[-4] == 'j' and \
                file_name[-5] == '.':
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print("File saved correctly")
        else:
            print("Invalid file name")
            return

    @staticmethod
    def to_excel(data, file_name):
        df = pd.DataFrame(data)
        if file_name[-1] == 'x' and file_name[-2] == 's' and file_name[-3] == 'l' and file_name[-4] == 'x' and \
                file_name[-5] == '.':
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
        if file_name[-1] == 'v' and file_name[-2] == 's' and file_name[-3] == 'c' and file_name[-4] == '.':
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
