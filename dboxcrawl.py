import sys
import re 
import requests
import os
if len(sys.argv) < 4:
    print("eksik argv")
    exit()
diziname , dizisezon , dizibolum = sys.argv[1],sys.argv[2],sys.argv[3]
diziurl = "http://www.dizibox1.com/"+diziname+"-"+str(dizisezon)+"-sezon-"+str(dizibolum)+"-bolum-izle/"
maincontent = str(requests.get(diziurl).content)
vidid = re.findall(r'play.dizibox.net/king/king.php\?v=(.*?)"', maincontent)[0]
headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"}
jsonresp = requests.post("http://play.dizibox.net/king/king.php?p=GetVideoSources",headers=headers, data={"ID":vidid}).json()
vidlink = jsonresp["VideoSources"][0]["file"]
os.system("mpv "+ vidlink)

