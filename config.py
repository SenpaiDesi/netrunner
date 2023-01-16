from colorama import Fore
import os
import subprocess
import json
import requests
import main
from ProgramFiles import iptrack

def print_banner():
    print(Fore.RED + "+-+-+-+-+-+-+\n|d|o|k|k|T|X|\n+-+-+-+-+-+-+\n")
    print(Fore.RESET + "\n")
    print("Welcome to DokkTX, the termux adaptation of DokkCLi. \n")
        
def start():
    os.system("clear")
    hostname = subprocess.check_output("whoami")
    id = subprocess.check_output("whoami")
    key = input("Please enter your license key: \n")
    response = requests.get(url=f"http://api.dokkcli.codechaos.net/auth?id={str(id)}&license_key={str(key)}&hostname={hostname}")
    response_json = response.json()
    if response_json[0]["Activated"] == "Yes":
        os.system("clear")

    else:
        os.system("clear")
        print(Fore.RED + "Authentication failed. Some common reasons:\n")
        print("1: License key invalid\n")
        print("2: License key used from another device\n")
        print("3: Piracy\n")
        print("Try again later.")
        os.system("sleep 10")
        exit()


# update menu
def update():
    os.system("apt-get update -y")
    os.system("apt-get upgrade -y")
    os.system("pkg install python3")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install subprocess")
    os.system("pip install pygeoip")
    os.system("clear")
    print(Fore.GREEN + "Update successfull!\n")
    os.system("sleep 10")
    main.main()


def hack_menu_one():
    os.system('clear')
    print_banner()
    menu_select = input(Fore.GREEN + "[1]    ipinfo.\n[2]    Remote shell\n[3]    Port Scanner\n[4]    Show networks and info\n[5]    Soon to come\n[6]    Soon to come.\n\n")
    if str(menu_select) == "1":
        iptrack.track()
    if str(menu_select) == "2":
        os.system('clear')

