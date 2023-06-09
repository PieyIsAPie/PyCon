#other shit
import psutil
import hashlib
import os
import socket, urllib.request
from globals import *
import base64
import ftplib
import tqdm
from getpass import getpass
#engines
import pyttsx3
import openai
import py_mini_racer
import colorama

ctx = py_mini_racer.MiniRacer()

def cd(dir):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(f"Directory '{dir}' not found")
    except PermissionError:
        print(f"Permission denied: '{dir}'")
def list_files(dir=None):
    if dir is None:
        dir = os.getcwd()
    files = os.listdir(dir)
    listfiles = ""
    filescount = 0
    for file in files:
        filescount += 1
        listfiles += f"{file}\n"
    return f"--- {filescount} Files/Dirs ---\n{listfiles}-------------------------------\n"

def list_filecontent(file):
    fin = open(file, "r")
    print(fin.read())
    fin.close()
def list_disk():
    partitions = psutil.disk_partitions()
    l = str()
    disks = []
    for partition in partitions:
        if partition.device not in disks:
            disks.append(partition.device)
    for disk in disks:
        l += f"{disk}\n"
    return l
def filesum(fnc, type, file, hash=None):
    if fnc == "validate":
        if type == "sha256":
            if hash == hashlib.sha256(open(file, "r").read().encode()).hexdigest():
                print("They match!")
            elif hash != hashlib.sha256(open(file, "r").read().encode()).hexdigest():
                print("They do not match.")
        if type == "sha512":
            if hash == hashlib.sha512(open(file, "r").read().encode()).hexdigest():
                print("They match!")
            elif hash != hashlib.sha512(open(file, "r").read().encode()).hexdigest():
                print("They do not match.")
        if type == "sha1":
            if hash == hashlib.sha1(open(file, "r").read().encode()).hexdigest():
                print("They match!")
            elif hash != hashlib.sha1(open(file, "r").read().encode()).hexdigest():
                print("They do not match.")
        if type == "sha384":
            if hash == hashlib.sha384(open(file, "r").read().encode()).hexdigest():
                print("They match!")
            elif hash != hashlib.sha384(open(file, "r").read().encode()).hexdigest():
                print("They do not match.")
        if type == "md5":
            if hash == hashlib.md5(open(file, "r").read().encode()).hexdigest():
                print("They match!")
            elif hash != hashlib.md5(open(file, "r").read().encode()).hexdigest():
                print("They do not match.")
    if fnc == "generate":
        if type == "sha256":
            print(hashlib.sha256(open(file, "r").read().encode()).hexdigest())
        if type == "sha512":
            print(hashlib.sha512(open(file, "r").read().encode()).hexdigest())
        if type == "sha1":
            print(hashlib.sha1(open(file, "r").read().encode()).hexdigest())
        if type == "sha384":
            print(hashlib.sha384(open(file, "r").read().encode()).hexdigest())
        if type == "md5":
            print(hashlib.md5(open(file, "r").read().encode()).hexdigest())

def tcpclient(host, port=80):
    port = int(port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(client.recv(4096).decode())
    while True:
        i = input("PyCon - (TCP) ")
        if i == "quit":
            client.close()
            break
        else:
            client.send(i.encode())
            print(client.recv(4096).decode())

def udpclient(host, port=161):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(client.recvfrom(4096)[0].decode())
    while True:
        i = input("PyCon - (UDP) ")
        if i == "quit":
            client.close()
            break
        else:
            client.sendto(i.encode(), (host, port))
            print(client.recvfrom(4096)[0].decode())

def askgpt(command: str):
    if command:
        # Set up the OpenAI API client
        openai.api_key = cfg["Settings.OpenAI_AskGPT"]["API_KEY"]

        # Send the command to ChatGPT
        response = openai.Completion.create(
            **cfg["Settings.OpenAI_AskGPT.API_Options"]
        )

        # Speak the response
        if response.choices:
            reply = response.choices[0].text.strip()
            print("Response:", reply)
        else:
            print("No response received.")

def speak(*args):
    text = " ".join(args)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def hget(url, out):
    filename = url.split('/')[-1]
    with tqdm(unit = 'B', unit_scale = True, unit_divisor = 1024, miniters = 1, desc = filename) as t:
        urllib.request.urlretrieve(url, filename = os.path.join(out, filename), reporthook = uh(t), data = None)

def setsetting(setting: str, value):
    category = setting.split('.')[1]
    option = setting.split('.')[2]
    cfg.set(f"Settings.{category}", option=option, value=value)
    with open(configp, 'w') as configfile:
        cfg.write(configfile)
    cfg.read(configp)

def getsetting(setting: str):
    category = f"{setting.split('.')[0]}.{setting.split('.')[1]}"
    print(cfg.get(category, setting.split('.')[2]))

def settings(fnc, setting: str, value=None):
    if fnc == "get":
        getsetting(setting)
    elif fnc == "set":
        if value == None:
            raise ValueError(value)
        setsetting(setting, value)
    else:
        print(f"Unsupported function: {fnc}")

def jss(*value):
    if os.path.exists(value):
        with open(value, "r") as a:
            ctx.execute(a.read())
    else:
        ctx.execute(value)

def enc(type, *value: str):
    if type == "b64":
        print(base64.b64encode(value[0].encode()).decode())
    if type == "b32":
        print(base64.b32encode(value[0].encode()).decode())
    if type == "b16":
        print(base64.b16encode(value[0].encode()).decode())
    if type == "b85":
        print(base64.b85encode(value[0].encode()).decode())
    if type == "a85":
        print(base64.a85encode(value[0].encode()).decode())
    if type == "b32hex":
        print(base64.b32hexencode(value[0].encode()).decode())
    if type == "urlb64":
        print(base64.urlsafe_b64encode(value[0].encode()).decode())
    if type == "stdb64":
        print(base64.standard_b64encode(value[0].encode()).decode())

def dec(type, *value: str):
    if type == "b64":
        print(base64.b64decode(value[0]).decode())
    if type == "b32":
        print(base64.b32decode(value[0]).decode())
    if type == "b16":
        print(base64.b16decode(value[0]).decode())
    if type == "b85":
        print(base64.b85decode(value[0]).decode())
    if type == "a85":
        print(base64.a85decode(value[0]).decode())
    if type == "b32hex":
        print(base64.b32hexdecode(value[0]).decode())
    if type == "urlb64":
        print(base64.urlsafe_b64decode(value[0]).decode())
    if type == "stdb64":
        print(base64.standard_b64decode(value[0]).decode())

def ftp(ip, port, passive=True):
    port = int(port)
    passive = bool(passive)
    user = input("Username: ")
    password = getpass()
    if ftplib.FTP.voidcmd('FEAT') == "AUTH TLS" or "AUTH SSL":
        print("This server is TLS!")
        ftp = ftplib.FTP_TLS(ip)
    else:
        ftp = ftplib.FTP(ip)
    ftp.login(user, password)
    ftp.set_pasv(passive)

    while True:
        command = input("PyCon - (FTP )")
        cmd = command.split(" ")[0]
        args = command.split(" ")[1:]
        if cmd == "list":
            try:
                files = ftp.nlst()
                print(files)
            except ftplib.error_perm as resp:
                if str(resp) == "550 No files found":
                    print("No files in this directory")
                else:
                    raise
        elif cmd == "get":
            with open(args[0], 'wb') as fd:
                total = ftp.size(args[0])

                with tqdm.tqdm(total=total) as pbar:
                    def callback_(data):
                        pbar.update(len(data))
                        fd.write(data)

                    ftp.retrbinary('RETR {}'.format(args[0]), callback_)
        elif cmd == "post":
            with open(args[0], 'wb') as fd:
                total = len(fd.read())

                with tqdm.tqdm(total=total) as pbar:
                    def callback_(data):
                        pbar.update(len(data))

                    ftp.storbinary('STOR {}'.format(args[0]), callback=callback_)
def diff(file1, file2):
    if hashlib.sha256(open(file1, "r").read().encode()).hexdigest() == hashlib.sha256(open(file2, "r").read().encode()).hexdigest():
        sha256 = True
    elif hashlib.sha256(open(file1, "r").read().encode()).hexdigest() != hashlib.sha256(open(file2, "r").read().encode()).hexdigest():
        sha256 = False
    if hashlib.sha512(open(file1, "r").read().encode()).hexdigest() == hashlib.sha512(open(file2, "r").read().encode()).hexdigest():
        sha512 = True
    elif hashlib.sha512(open(file1, "r").read().encode()).hexdigest() != hashlib.sha512(open(file2, "r").read().encode()).hexdigest():
        sha512 = False
    if hashlib.sha1(open(file1, "r").read().encode()).hexdigest() == hashlib.sha1(open(file2, "r").read().encode()).hexdigest():
        sha1 = True
    elif hashlib.sha1(open(file1, "r").read().encode()).hexdigest() != hashlib.sha1(open(file2, "r").read().encode()).hexdigest():
        sha1 = False
    if hashlib.sha384(open(file1, "r").read().encode()).hexdigest() == hashlib.sha384(open(file2, "r").read().encode()).hexdigest():
        sha384 = True
    elif hashlib.sha384(open(file1, "r").read().encode()).hexdigest() != hashlib.sha384(open(file2, "r").read().encode()).hexdigest():
        sha384 = False
    if hashlib.md5(open(file1, "r").read().encode()).hexdigest() == hashlib.md5(open(file2, "r").read().encode()).hexdigest():
        md5 = True
    elif hashlib.md5(open(file1, "r").read().encode()).hexdigest() != hashlib.md5(open(file2, "r").read().encode()).hexdigest():
        md5 = False
    if open(file1, "r").read() == open(file2, "r").read():
        m = True
    elif open(file1, "r").read() != open(file2, "r").read():
        m = False
    
    if sha256 == True:
        print("SHA256 test " + colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL)
    elif sha256 == False:
        print("SHA256 test " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)
    if sha512 == True:
        print("SHA512 test " + colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL)
    elif sha512 == False:
        print("SHA512 test " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)
    if sha1 == True:
        print("SHA1 test " + colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL)
    elif sha1 == False:
        print("SHA1 test " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)
    if sha384 == True:
        print("SHA384 test " + colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL)
    elif sha384 == False:
        print("SHA384 test " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)
    if md5 == True:
        print("MD5 test " + colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL)
    elif md5 == False:
        print("MD5 test " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)
    if m == True:
        print("File contents test " + colorama.Fore.GREEN + "SUCCESS" + colorama.Style.RESET_ALL)
    elif m == False:
        print("File contents test " + colorama.Fore.RED + "FAILED" + colorama.Style.RESET_ALL)

    
