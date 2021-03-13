#this libary was created by Jefaxe
#it includes some handy function, to use this libary simply download it, put it into the folder your running your script from
#write "import jeflib" then use jeflib.<function> to call functions.
#or use downjef at the github page to automate the download, and use "import libs.jeflib as jb", then use "jb.<function>"

import os
import urllib.request #why do both need to be imported, isn't urllib.requst part of urllib?
import logging
import shutil

#exceptions
class WebError(Exception):
    pass

def moveFile(this,that):
    try:
        os.rename(this,that)
    except FileNotFoundError:
        thatList=that.rsplit("/",1)[:-1]
        thatString=""
        for i in thatList:
            thatString +=i
        createFolder(thatString)
        os.rename(this,thatString+"/"+that.rsplit("/",1)[-1])
def clearFile(name):
   if os.path.exists(name):
       os.remove(name)
       with open(name,"w") as recreate:
           pass
   else:
       with open(name,"w") as recreate:
           pass
def connected():
    try:
        urllib.request.urlopen("https://google.com") #Python 3.x
        return True
    except Exception as e:
        return False

def downloadFile(url,name="|",overwrite=False,NotFoundCrash=True,LostConnectionCrash=True): #makes it easier to download files, only downloads them if they are not already downloaded (unless overwite=True is set)
    if name=="|":
        from urllib.parse import urlparse
        p = urlparse(url)
        name=p.path.rsplit("/", 1)[-1]
    if not connected():
        if LostConnectionCrash:
            raise WebError("No internet")
        else:
            logging.error("No internt")
            return False
    if not overwrite:
        if not os.path.exists(name):
            try:
                try:
                    # Download the file from `url` and save it locally under `name`:
                    with urllib.request.urlopen(url) as response, open(name, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                except ValueError: #if http / https is not supplied, give http (will redirect to https if availiable)
                    with urllib.request.urlopen("http://"+url) as response, open(name, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                with open(name,"rb") as contents:
                    contents=contents.read()
            except urllib.error.HTTPError as e:
                if not NotFoundCrash:
                    logging.error(url+" is not a file")
                else:
                    raise WebError(url+" is not a file")
            except urllib.error.URLError:
                if not NotFoundCrash:
                    logging.error(url+"'s host was not found")
                else:
                    raise WebError(url+"'s host was not found")
        else:
            logging.debug("You already have, "+name+", not downloading (force download by setting overwrite=True)")
    if overwrite:
        try:
                try:
                    # Download the file from `url` and save it locally under `name`:
                    with urllib.request.urlopen(url) as response, open(name, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                except ValueError: #if http / https is not supplied, give http (will redirect to https if availiable)
                    with urllib.request.urlopen("http://"+url) as response, open(name, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                with open(name,"rb") as contents:
                    contents=contents.read()
            except urllib.error.HTTPError as e:
                if not NotFoundCrash:
                    logging.error(url+" is not a file")
                else:
                    raise WebError(url+" is not a file")
            except urllib.error.URLError:
                if not NotFoundCrash:
                    logging.error(url+"'s host was not found")
                else:
                    raise WebError(url+"'s host was not found")

def createFile(filename,contents,overwite=False): #creates a file if it does not exits, otherwise does nothing
    if not os.path.exists(filename) or overwite==True:
        with open(filename):
            crt.write(str(contents))
            return True
    else:
        return False

def createFolder(foldername): #creates a folder (or tree of folder) if it does not exist, otherwise does nothing
    if not os.path.exists(foldername):
        os.makedirs(foldername)

def replace_line(file_name, line_num, text):#replaces a given line of a given file
    #this function is from stack overflow, https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()


if __name__=="__main__":
    print("Hey! This isn't meant to be run, just import it")
