import sys
import os

# Code has been modified from original found on: https://stackoverflow.com/questions/42251295/file-path-for-pyinstaller-bundled-images

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)