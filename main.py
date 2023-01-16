import config
from colorama import Fore
import os

def launch():
    config.start()
    main()

def main():
    global menu_select
    print(Fore.RED + "+-+-+-+-+-+-+\n|d|o|k|k|T|X|\n+-+-+-+-+-+-+\n")
    print(Fore.RESET + "\n")
    print("Welcome to DokkTX, the termux adaptation of DokkCLi. \n\n")
    menu_select = input(Fore.GREEN + "[1]    Update.\n[2]    tools and scripts\n[3]    Global Tools\n[4]    To be made\n[5]    Information.\n[0]    Exit\n\n")
    # Showcase menu

    if str(menu_select) == "1":
        config.update()
    elif str(menu_select) == "2":









if __name__ == "__main__":
    launch()