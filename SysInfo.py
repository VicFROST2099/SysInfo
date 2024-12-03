import json                 # Reads config file
import sys                  # https://docs.python.org/3/library/sys.html
import os                   # https://docs.python.org/3/library/os.html
import GPUtil               # https://github.com/anderskm/gputil
import cpuinfo              # https://github.com/workhorsy/py-cpuinfo
import psutil               # https://psutil.readthedocs.io/en/latest/
import platform             # https://docs.python.org/3/library/platform.html
import ctypes               # https://docs.python.org/3/library/ctypes.html
import glob                 # https://docs.python.org/3/library/glob.html
from pyfiglet import Figlet # http://www.figlet.org/examples.html
from colorama import *      # https://github.com/tartley/colorama   
os.system("cls") 
# Config ---------------------------------------------------------------
with open("config.json", "r") as file:
        config = json.load(file)

# Colour ---------------------------------------------------------------
# Foreground Bar Colour
foreColourBar = config.get("foregroundBar", "Fore.RESET")
fCbar = eval(foreColourBar)
# Background Bar Colour
backColourBar = config.get("backgroundBar", "Back.RESET")
bCbar = eval(backColourBar)
# Foreground Text Colour
foreColourText = config.get("foregroundText", "Fore.RESET")
fCtext = eval(foreColourText)
# Background Text Colour 
backColourText = config.get("backgroundText", "Back.RESET")
bCtext = eval(backColourText)

# PrgBar ---------------------------------------------------------------
def print_progress_bar(index, total, label):
    barColourF = fCbar
    barColourB = bCbar
    n_bar = 30  # Progress bar width
    progress = index / total
    sys.stdout.write('\r')
    # progress bar calculation + settings
    filled_length = int(n_bar * progress)
    filled_bar = barColourB + barColourF + "/" * filled_length + Fore.RESET + Back.RESET
    empty_bar = ' ' * (n_bar - filled_length)
    # progress bar print
    sys.stdout.write(f"\t{bCtext}{fCtext}[{filled_bar + empty_bar}{bCtext}{fCtext}] {Fore.RESET}{Back.RESET}{round(float(100 * progress), 2)}%  {label}")
    sys.stdout.flush()
        
# Ascii ---------------------------------------------------------------
if config.get("asciiArt", 1) == 1: 
    def asciiArt():    
        font = config.get("font", "standard")
        t = config.get("text", "example")
        figlet = Figlet(font=font)
        text = figlet.renderText(t)
        return (f"{bCtext}{fCtext}{text}{Fore.RESET}{Back.RESET}")
    print(asciiArt())
else: 
    None

# Custom Ascii --------------------------------------------------------
if config.get("customAscii", 1) == 1:
    def customAscii():
        txt_file = glob.glob("*.txt")
        with open(txt_file[0], "r", encoding="utf-8-sig") as f:
            printOut = f.read()
            return (f"{bCtext}{fCtext}{printOut}{Fore.RESET}{Back.RESET}")
    print(customAscii())
else:
    None

# OS ------------------------------------------------------------------
if config.get("osInfo", 1) == 1:
    def OsInfo(): 
        if config.get("osName", 1) == 1:
            os_name = (f"{bCtext}{fCtext} Operating System: {Fore.RESET}{Back.RESET}{platform.system()}")
            print(os_name)
        else:
            None
        if config.get("osVersion", 1) == 1:
            os_version = (f"{bCtext}{fCtext}\tOS Version: {Fore.RESET}{Back.RESET}{platform.version()}")
            print(os_version)
        else:
            None
    
        if config.get("osRelease", 1) == 1:
            os_release = (f"{bCtext}{fCtext}\tOS Release: {Fore.RESET}{Back.RESET}{platform.release()}")
            print(os_release)
        else:
            None   
        if config.get("osFullInfo", 1) == 1:
            os_info = (f"{bCtext}{fCtext}\tFull OS Info: {Fore.RESET}{Back.RESET}{platform.platform()}")
            print(os_info)
        else:
            None
    OsInfo()
else:
    None

# Uptime --------------------------------------------------------------
if config.get("uptime", 1) == 1:
    def upTime():
        lib = ctypes.windll.kernel32
        time = lib.GetTickCount64()
        time = int(str(time)[:-3])
        mins, sec = divmod(time, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)
        UpTime = (f"{bCtext}{fCtext}Uptime: {Fore.RESET}{Back.RESET}{str(days)} days, {str(hour)} hours, {str(mins)} minutes, {str(sec)} seconds")
        print(UpTime)
    upTime()
else:
    None

# CPU -----------------------------------------------------------------
if config.get("cpuInfo", 1) == 1:
    def CPUinfo():
        cpu_info = cpuinfo.get_cpu_info()
        if config.get("cpuName", 1) == 1:     
            print(f"{bCtext}{fCtext}CPU: {Fore.RESET}{Back.RESET}{cpu_info['brand_raw']}")
        else:
            None
        if config.get("cpuLoad", 1) == 1:
            load = psutil.cpu_percent(interval=1)
            print(f"{bCtext}{fCtext}\tCPU Load: {Fore.RESET}{Back.RESET}{load}%")
        else:
            None
        if config.get("cpuLoadBar", 1) == 1:
            load = psutil.cpu_percent(interval=1)
            print_progress_bar(load, 100.00, "Load")
            print()
        if config.get("cpuCores", 1) == 1:
            print(f"{bCtext}{fCtext}\tNumber of Cores: {Fore.RESET}{Back.RESET}{psutil.cpu_count(logical=False)}")
        else:
            None
        if config.get("cpuThreads", 1) == 1:
            print(f"{bCtext}{fCtext}\tNumber of Threads: {Fore.RESET}{Back.RESET}{psutil.cpu_count(logical=True)}")
        else:
            None
    CPUinfo()
else:
    None

# GPU -----------------------------------------------------------------
if config.get("gpuInfo", 1) == 1:
    def GPUinfo():
        gpus = GPUtil.getGPUs()
        if gpus:                                
            for gpu in gpus:
                if config.get("gpuName", 1) == 1:                 
                    print(f"{bCtext}{fCtext}GPU: {Fore.RESET}{Back.RESET}{gpu.name}")
                else: 
                    None
                if config.get("gpuRam", 1) == 1:                 
                    print(f"{bCtext}{fCtext}\tTotal Memory: {Fore.RESET}{Back.RESET}{gpu.memoryTotal:.2f} MB")
                else: 
                    None 
                if config.get("gpuLoad", 1) == 1:                 
                    print(f"{bCtext}{fCtext}\tLoad: {Fore.RESET}{Back.RESET}{gpu.load * 100:.2f}%")
                else:
                    None
                if config.get("gpuLoadBar", 1) == 1: 
                    print_progress_bar(gpu.load, 100.00, "Load")
                    print()
                else: 
                    None 
                if config.get("gpuTemp", 1) == 1:                 
                    print(f"{bCtext}{fCtext}\tTemperature: {Fore.RESET}{Back.RESET}{gpu.temperature} °C")
                else: 
                    None             
        else:                                   
            print("No GPU available")
    GPUinfo()
else:
    None

# RAM -----------------------------------------------------------------
if config.get("ramInfo", 1) == 1:
    def RAMinfo():
        ram = psutil.virtual_memory() 
        if config.get("ramTotal", 1) == 1:
            total_ram = ram.total / (1024 ** 3) 
            print(f"{bCtext}{fCtext}Total RAM: {Fore.RESET}{Back.RESET}{total_ram:.2f} GB") 
        else: 
            None
        if config.get("ramUsage", 1) == 1:
            ram_usage_percentage = ram.percent 
            print(f"{bCtext}{fCtext}\tRAM Usage: {Fore.RESET}{Back.RESET}{ram_usage_percentage}%") 
        else: 
            None
        if config.get("ramUsageBar", 1) == 1:
            ram_usage_percentage = ram.percent 
            print_progress_bar(ram_usage_percentage, 100.00, "RAM Usage")
            print()
        else:
            None
        if config.get("ramUsed", 1) == 1:
            used_ram = ram.used / (1024 ** 3) 
            print(f"{bCtext}{fCtext}\tUsed RAM:{Fore.RESET}{Back.RESET} {used_ram:.2f} GB") 
        else: 
            None
        if config.get("ramLeft", 1) == 1:
            available_ram = ram.available / (1024 ** 3) 
            print(f"{bCtext}{fCtext}\tAvailable RAM:{Fore.RESET}{Back.RESET} {available_ram:.2f} GB")  
        else: 
            None
    RAMinfo()
else:
    None

# Storage -------------------------------------------------------------
if config.get("storageInfo", 1) == 1:
    def StorageInfo():
        partitions = psutil.disk_partitions() 
        for partition in partitions: 
            if config.get("disk", 1) == 1:
                print(f"{bCtext}{fCtext}Device: {Fore.RESET}{Back.RESET}{partition.device}")
            else: 
                None
            if config.get("mountpoint", 1) == 1:
                print(f"{bCtext}{fCtext}\tMountpoint: {Fore.RESET}{Back.RESET}{partition.mountpoint}")
            else: 
                None
            if config.get("fileType", 1) == 1:
                print(f"{bCtext}{fCtext}\tFile System Type: {Fore.RESET}{Back.RESET}{partition.fstype}")
            else:
                None

            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                total = partition_usage.total / (1024 ** 3) 
                used = partition_usage.used / (1024 ** 3)  
                free = partition_usage.free / (1024 ** 3) 
                percent_used = partition_usage.percent
                
                if config.get("totalSize", 1) == 1:
                    print(f"{bCtext}{fCtext}\tTotal Size: {Fore.RESET}{Back.RESET}{total:.2f} GB")
                else: 
                    None
                if config.get("totalUsage", 1) == 1:
                    print(f"{bCtext}{fCtext}\tUsage: {Fore.RESET}{Back.RESET}{percent_used}%")
                else: 
                    None
                if config.get("totalUsageBar", 1) == 1:
                    print_progress_bar(percent_used, 100.00, "Used")
                    print()
                else: 
                    None
                if config.get("totalUsed", 1) == 1:
                    print(f"{bCtext}{fCtext}\tUsed: {Fore.RESET}{Back.RESET}{used:.2f} GB")
                else: 
                    None
                if config.get("totalFree", 1) == 1:
                    print(f"{bCtext}{fCtext}\tFree: {Fore.RESET}{Back.RESET}{free:.2f} GB")
                else: 
                    None
            except PermissionError:
            # sometimes when a drive is used for dual-boot it may show errorS
                print("\tPermission denied for this partition.")
    StorageInfo()
else:
    None