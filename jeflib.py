#this libary was created by Jefaxe
#it includes some handy function, to use thislibary simply download it, put it into the folder your running your script from
#write "import jeflib" then use jeflib.<function> to call functions.

import os
import requests
import urllib
import logging


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
def connection():
    try:
        urllib.request.urlopen("https://google.com") #Python 3.x
        return True
    except Exception as e:
        logging.error("No internet")
        return False

def downloadFile(url,name="|",overwrite=False,crash_at_404=True,crash_at_no_internet=False,crash_at_permissionError=False): #makes it easier to download files, only downloads them if they are not already downloaded (unless overwite=True is set)
    if name=="|":
        from urllib.parse import urlparse
        p = urlparse(url)
        name=p.path.rsplit("/", 1)[-1]
    if not connection():
        if crash_at_no_internet:
            raise WebError("No internet")
        else:
            logging.info("no internt, not downloading file (this can be disabled with 'crash_at_no_internet=True'")
    if not overwrite:
        if not os.path.exists(name):
            try:
                r = requests.get(url)
            except requests.exceptions.MissingSchema:
                r = requests.get("http://"+url)
            try:
                if not r.content.decode("utf-8")=="404: Not Found":
                    try:
                        with open(name,'wb') as output_file:
                            output_file.write(r.content)
                    except FileNotFoundError: #as in directory not found
                        os.makedirs(os.path.split(name)[0])
                        with open(filepath,'wb') as output_file:
                            output_file.write(r.content)
                    except PermissionError: #most likely trying to read a directory
                        if crash_at_permissionError:
                            raise WebError("You tried to read the directory "+name+" or you don't have write-permission here")
                        else:
                            logging.warn("You tried to read the directory "+name+" or you don't have write-permission here")
                            return False
                    return True
                elif r.content.decode("utf-8")=="404: Not Found" and crash_at_404:
                    raise WebError("The file said to be at "+url+" returned 404")
                    return False
                elif r.content.decode("utf-8")=="404: Not Found" and not crash_at_404:
                    logging.error(name+" could not be found at "+url)
                    return False
            except UnicodeError:
                try:
                    with open(name,'wb') as output_file:
                        output_file.write(r.content)
                except FileNotFoundError: #as in directory not found
                    #logging.debug(os.path.split(name))
                    os.makedirs(os.path.split(name)[0])
                    with open(name,'wb') as output_file:
                        output_file.write(r.content)
                return True
        else:
            logging.debug("You already have, "+name+", not downloading (force download by setting overwrite=True)")
    if overwrite:
        with open(name,'wb') as output_file:
                        output_file.write(r.content)

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
