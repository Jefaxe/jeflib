#simply download this file, and have import path.to.downjef (if not in your project's root), or import downjef.
#then use downjef.run()
#use run(forceUpdate=True) to force jeflib to update everytime (instead of just on the first download). NOTE: If there are backwards-breaking changes, this may break your project!
import urllib.request
import os
import shutil

def run(forceUpdate=False):
    if not os.path.exists("libs/jeflib.py") and not ForceUpdate:
        if not os.path.exists("libs"):
            os.mkdir("libs")
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jeflib/main/jeflib.py") as response, open("libs/jeflib.py", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
     else:
        if not os.path.exists("libs"):
            os.mkdir("libs")
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jeflib/main/jeflib.py") as response, open("libs/jeflib.py", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

            
if __name__=="__main__":
    run()
