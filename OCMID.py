#V1.0 - 26/07/2016

#importing the urlib.request module for the interfacing of the program from the internet.
import urllib.request;
print("hello world");
def ImageDownloader():
    #making a file object named as fileOpenObjectOnReadMode for the file data.txt in the read mode.
    fileOpenObjectOnReadMode = open("data.txt","r");
    #we imported the os module for the directory creation at the os.path
    #or simply wherever the wolvieDummy.py/file is saved as!.
    import os;
    #os.makedirs() method is used for the creation of the directory named as the DownloadedImageURLFile.
    os.makedirs("DownloadedImageURLFile");
    #creation of a integer implicitly declared variable named as indexForName.
    indexForName = 0;
    #using the for loop and iterate through every URL present in the file data.txt via the file object : fileOpenObjectOnReadMode
    for lineByLineIterate in fileOpenObjectOnReadMode:
        #using the try - except clause.
        try:
            urllib.request.urlretrieve(lineByLineIterate,"DownloadedImageURLFile/"+str(indexForName)+".jpeg");
            indexForName = indexForName + 1;
        #if you see carefully we are catching every exception produced over here
        except:
            print("ExceptionHTTP 403 Error @ : "+str(indexForName));
            continue;
    #hence the version is completed
