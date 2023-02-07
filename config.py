from colorama import Fore
import os
import subprocess
import json
import requests
import main
from Program import iptrack, portscan, information

# testx

def print_banner():
    print(Fore.RESET + "\n")
    print("Welcome to Netrunner. Please pick an option below:\n")
        


# update menu
def update():
    os.system("apt-get update -y")
    os.system("apt-get upgrade -y")
    os.system("pkg install python3")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pygeoip")
    os.system('pip install tqdm')
    os.system("clear")
    print(Fore.GREEN + " Netrunner dependencies update success!\n")
    os.system("sleep 5")
    main.main()

# hack menus

def hack_menu_one():
    os.system('clear')
    print_banner()
    menu_select = input(Fore.GREEN + "[1]    ipinfo.\n[2]    Port Scanner\n[3]    Phone number info\n[4]    Soon to come.\n[5]    Soon to come\n[6]    Soon to come.\n\n")
    if str(menu_select) == "1":
        iptrack.track()
    if str(menu_select) == "2":
        os.system('clear')
        portscan.scan()




# Information menu

def info_menu():
    os.system('clear')
    information.information()
    os.system('sleep 20')
    main.main()


def close_menu():
    os.system('clear')
    print_banner()
    print(Fore.RED +  ".\nStay safe out there runner.")
    os.system('sleep 15')
    exit()