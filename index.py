import os
import shutil
from classes.InputGateway import InputGateway
from classes.Validator import Validator

print("Welcome to the StarSector Portrait Replacer.")

ss_install_path = InputGateway.star_sector_install_path()

source_asset_path = InputGateway.source_asset_path()

destination_asset_path = InputGateway.destination_asset_path()

ss_portraits_path = os.path.join(ss_install_path, "starsector-core", "graphics", "portraits")
ss_characters_path = os.path.join(ss_install_path, "starsector-core", "graphics", "portraits", "characters")
destination_characters_path = os.path.join(destination_asset_path, "characters")

ss_file_names = [
    f for f 
    in os.listdir(ss_portraits_path) 
    if (os.path.isfile(os.path.join(ss_portraits_path, f)) and not f == "godiva.jpg") # cute cat
] + [
    os.path.join("characters", f) for f 
    in os.listdir(ss_characters_path) 
    if (os.path.isfile(os.path.join(ss_characters_path, f)))
]

ss_file_names = sorted(ss_file_names, key=lambda f: f.lower().replace("_", "0").replace("characters", "zcharacters"))

custom_source_assets = [
    f for f 
    in os.listdir(source_asset_path) 
    if (os.path.isfile(os.path.join(source_asset_path, f))) and f.split(".")[-1] == "png"
]
custom_source_assets.sort()

if (len(custom_source_assets) == 0):
    print("Error: This directory has no png files: " + source_asset_path)
    exit()

if (not os.path.exists(destination_characters_path)):
    os.mkdir(destination_characters_path)

i = -1
for filename in ss_file_names:
    i += 1

    if (i > len(custom_source_assets) - 1):
        i = 0

    file_to_copy = os.path.join(source_asset_path, custom_source_assets[i])
    destination_file_path = os.path.join(destination_asset_path, ss_file_names[i])

    shutil.copy(file_to_copy, destination_file_path)

print("OK")
