import os

class Validator:
    def is_star_sector_install_path_valid(path):
        return "starsector.exe" in map(lambda path: path.split("/")[-1], os.listdir(path))
