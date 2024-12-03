SysInfo - a Neofetch inspiritation in Python
------------------------------------------------------------------------------------------------------------------------------------------------------
Introduction ->

This project was made because I wanted to change the ascii art in the Windows version of Neofetch which is accessible from Winget in Windows 11 or 
via the github page: https://github.com/nepnep39/neofetch-win

------------------------------------------------------------------------------------------------------------------------------------------------------
Notes ->
  - Install required libraries for python using pip (sys, os, GPUtil, cpuinfo, psutil, platform, ctypes, glob, pyfiglet, colorama)
  - Originally made for Windows (Linux was not tested, might update for it to run on both in future) 
  - Gpu information only available for Nvidia cards (possibility of making it work for both AMD and Nvidia in future)
  - Cpu load may be inaccurate for some Cpu's that have a larger core count
  - Python 3 and up required (I used 3.11.9 when making, unsure how it runs on other version due to lack of testing)
------------------------------------------------------------------------------------------------------------------------------------------------------
How it works ->

The script runs once, reading the config.json and the first .txt file as the custom ascii. 
The json file is an important component to the script as its being read for the script to know what to 
output in a terminal or Python IDE. 

Main parts of the json are right underneath a comment, if they are set to 0 then the whole part will be
disabled or parts can be disabled, for example (line by line):

    "_comment1": "This part is for ascii art",
    "asciiArt": 0,                          
    "font": "graffiti",
    "text": "MonkeFetch",
or

    "_comment3":"This part is for OS",
    "osInfo": 1,   
    "osName": 1,
    "osVersion": 1,
    "osRelease": 1,
    "osFullInfo": 1,

------------------------------------------------------------------------------------------------------------------------------------------------------    
Key parts that may be worth noting ->

For ascii art using built in function:
  - 0 = false - turns this function off (set to this if using custom ascii from .txt)
  - graffiti = the style of the text (more styles can be found on http://www.figlet.org/examples.html)
  - Monkefetch = the text being printed
    
For ascii art using .txt file:
  -  Just drop it into the same directory as the main file
  -  Can use one from the presets or make your own
  -  If theres multiple .txt files in the directory, the script will use the first one

For the colours:
  - Any colour changes go after Fore. or Back.
  - Possible colour choices are listed in the json file or can be found on https://github.com/tartley/colorama
------------------------------------------------------------------------------------------------------------------------------------------------------
Screenshot ->
![image](https://github.com/user-attachments/assets/0137147f-aadb-4b77-96c0-72c7752d10bc)


