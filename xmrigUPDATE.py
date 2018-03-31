# coding=utf-8
import urllib,re,time,json,os,zipfile,requests,subprocess
domain='https://github.com'
data = json.load(open('config.json'))
ver2=int(data[0]["version"].replace('.',''))
refresh=data[0]["refresh"]
path=data[0]["path"]
link_name = {}
exc = {}
def getver():
    url='https://github.com/Bendr0id/xmrigCC/releases'
    website = urllib.urlopen(url)
    html = website.read()
    links = re.findall(r'(?<=<a href=")[^"]*\bgcc-win64.zip\b', html)
    link_name['link']=(domain)+(links[0])
    link=links[0]
    version=link.split('/')
    ver0=version[5]
    return ver0

def download_file(url):
    dir=os.getcwd()
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    fname=dir+'\\'+local_filename
    exc['filename']=(fname)
    with open(fname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):  
            if chunk:
                f.write(chunk)
def update():
    process=subprocess.Popen(['taskkill', '/F', '/IM', 'xmrigDaemon.exe', '/IM', 'xmrigMiner.exe'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    zip_dir=exc.get('filename')
    print zip_dir
    zip_ref = zipfile.ZipFile(zip_dir, 'r')
    zip_ref.extract('xmrigMiner.exe',path)
    zip_ref.extract('xmrigDaemon.exe',path)
    zip_ref.close()
    
def newver(ver):
    with open('config.json', 'r+') as file:
        json_data = json.load(file)
        for item in json_data:
            if item['version']:
                item['version'] = ver
    with open('config.json', 'w') as file:
        json.dump(json_data, file, indent=2)
        
while True:
    ver0=getver()
    ver=int(ver0.replace('.',''))
    if ver > ver2:
        download_link=link_name.get('link')
        print download_link
        download_file(download_link)
        time.sleep(15)
        update()
        ver1=data[0]["version"] = ver0
        ver2=int(data[0]["version"].replace('.',''))
        newver(ver1)
    else:
        print 'ok',ver,ver2
        time.sleep(refresh)
        
    
    
        
