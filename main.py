import config
from colorama import Fore
import os

def launch():
    config.start()
    main()

def main():
    global menu_select
    os.system('clear')
    config.print_banner()
    menu_select = input(Fore.GREEN + "[1]    Update.\n[2]    tools and scripts\n[3]    Global Tools\n[4]    To be made\n[5]    Information.\n[0]    Exit\n\n")
    # Showcase menu

    if str(menu_select) == "1":
        config.update()
    elif str(menu_select) == "2":
        os.system('clear')
        config.print_banner()
        hack_menu_select = input(Fore.GREEN + "[1]    Network tools and attacks.\n[2]    Password cracking\n[3]    Page downloader\n[4]    Soon to come.\n[5]    Soon to come.\n[0]    Exit\n\n")
        if str(hack_menu_select) == "1":
            config.hack_menu_one()
    
    elif str(menu_select) == "5":
        config.info_menu()









if __name__ == "__main__":
    launch()