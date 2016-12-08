from flask import Flask, jsonify, send_file
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from PIL import Image
import csv
import httplib
from httplib import HTTP
from urlparse import urlparse
import urllib2
import cStringIO
import urllib
import os
import time
from urlparse import urlparse
from threading import Thread
import httplib, sys, getopt
from Queue import Queue
import StringIO

def check_url(url):
	try:
		connection = urllib2.urlopen(url)
		return connection.getcode()
		connection.close()
	except:
		return 404

with open('/home/swapnil/Desktop/O.C.M.I.D/data.txt', 'r') as f :
    x = 0
    for line in f :
       url = line
       if (check_url(line)<400):
           file = urllib.urlopen(url)
           img = Image.open(file)
           newpath = '/home/swapnil/Desktop/O.C.M.I.D/images/' 
           if not os.path.exists(newpath):
                os.makedirs(newpath)
           img.save("/home/swapnil/Desktop/O.C.M.I.D/images/"+str(x+1)+'.jpg', img.format, quality=100)
           x = x+1
       else :
           x = x
            
