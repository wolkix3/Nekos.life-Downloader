from collections import namedtuple
from threading import Thread

import multiprocessing
import requests
import shutil
import json
import os


#---------------------------------------------
#Enter the API URL here:
api_url = "https://nekos.life/api/v2/img/neko"
#---------------------------------------------


def download(url,path):
    
    response = requests.get(url,stream = True)
    
    if response.status_code == 200:
        with open(path,"wb") as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw,file)
    
    print("Sucessfully downloaded " + path)
    

def neko():
    while True:
        
        path = ""
        
        with requests.Session() as session:
            response = session.get(api_url)

        output = response.text

        info = json.loads(output,
            object_hook = lambda d : namedtuple('X',d.keys())(*d.values()))

        url = info.url
        path = url[url.rfind("/") + 1:]

        if not os.path.exists(path):
            download(url,path);

for i in range(multiprocessing.cpu_count()):
    thread = Thread(target = neko)
    thread.start()
