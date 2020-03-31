# Keystroke-Logger
A keystroke logger implemented using Python in Windows 10

## Introduction
The objective of this project is to design a keystroke logger which periodically sends emails to the server's email address. For the purpose of this project, the creator of the keyLogger is referred to as the server and the remote computer on which the keyLogger is installed is referred to as the host.
Two processes are simultaneously performed namely:
- Logging keystrokes
- Periodically sending emails containing the logs to the server

## Summary & Additional Notes
When run, a new text file is created on the host computer, in a location specified by the server. This text file contains a log of the keystrokes on the host computer. An email containing this text file as an attachment is sent from a dummy email address to the server's email address periodically.

It is advisable to create a dummy account to push the email to the server's email as this dummy account has to be made less secure than an average gmail account in order to allow a local python script to create and send emails from this account.

To convert the keylogger to an executable from the python script using cmd:
1. Install pyinstaller:
pip_path install pyinstaller
eg:
>> C:\Python\Scripts\pip.exe install pyinstaller 
2. pyinstaller_path python_script_path
eg:
>> C:\Python\Scripts\pyinstaller.exe C:\Windows\Temp\keyLogger.py


To share the keylogger (.exe) with another computer:
- Upload the executable to your google drive and share the drive link with the desired computer. (might not work with secure accounts)
- If the keylogger is already installed on another computer on your local network workgroup then it can be accessed through powershell using procedure mentioned in powershellPSSession.ps1
