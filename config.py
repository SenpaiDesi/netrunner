from colorama import Fore
import os
import subprocess
import json
import requests


def start():
    os.system("clear")
    hostname = subprocess.check_output("whoami")
    id = subprocess.check_output("whoami")
    key = input("Please enter your license key: \n")
    response = requests.get(url=f"http://api.dokkcli.codechaos.net/auth?id={str(id)}&license_key={str(key)}&hostname={hostname}")
    response_json = response.json()
    if response_json[0]["Activated"] == "Yes":
        pass
    else:
        os.system("clear")
        print(Fore.RED + "Authentication failed. Some common reasons:\n")
        print("1: License key invalid\n")
        print("2: License key used from another device\n")
        print("3: Piracy\n")
        print("Try again later.")
        os.system("sleep 20")
        exit()
        




if __name__ == "__main__":
    start()