from tkinter import Tk
from tkinter.filedialog import askdirectory
from classes.Validator import Validator

class InputGateway:
    def star_sector_install_path():
        path = askdirectory(title='Please pick your StarSector install folder')
        if (not Validator.is_star_sector_install_path_valid(path)):
            raise Exception("Install path not valid")
        return path

    def source_asset_path():
        path = askdirectory(title='Please pick your custom assets\' folder')
        return path

    def destination_asset_path():
        path = askdirectory(title='Please pick your destination folder')
        return path
