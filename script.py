import requests
import urllib
import json
from collections import namedtuple
import shutil
from threading import Thread
import os
import multiprocessing

#---------------------------------------------
#Enter the API URL here:
api_url = "https://nekos.life/api/v2/img/neko"
#---------------------------------------------

def neko():
    while True:
        filename = ""
        with requests.Session() as s:
            api_output = s.get(api_url)

        output = api_output.text

        x = json.loads(output, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        url = x.url
        filename = url[url.rfind("/")+1:]
        exists = os.path.exists(filename)

        if not exists:
            grab = requests.get(url, stream=True)
            if grab.status_code == 200:
                with open(filename, "wb") as f:
                    grab.raw.decode_content = True
                    shutil.copyfileobj(grab.raw, f)
            print("Sucessfully downloaded " + filename)

for i in range(multiprocessing.cpu_count()):
    t = Thread(target=neko)
    t.start()
