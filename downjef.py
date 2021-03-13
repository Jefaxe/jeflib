import urllib.request
import os
import shutil


if not os.path.exists("libs/jeflib.py"):
    if not os.path.exists("libs"):
        os.mkdir("libs")
    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jeflib/main/jeflib.py") as response, open("libs/jeflib.py", 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
