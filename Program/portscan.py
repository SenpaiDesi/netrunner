import subprocess
import sys
from datetime import date, datetime
from socket import *
from threading import Thread
from colorama import Fore
from tqdm import tqdm
import main

def loop():
    """Append values"""
    for value in openports:
        open_ports_formatted = f"{value}, "
def scan():
    global openports
    #Ask for inpute
    remoteServer = input("Enter a remote host to scan: ")
    filename = input("Enter name to give to the file:")
    remoteServerIP = gethostbyname(remoteServer)

    # time and information
    current_time = datetime.now()
    print(Fore.RESET + "\n")

    try:
        # Defining ports using range()
        # Error handeling included

        # will scan ports between 1 to 65,535
        for port in tqdm(range(1,65536), desc=f"Scanning..", unit=" ports"):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(0.1)
         
            # scan
            openports = []
            result = s.connect_ex((remoteServerIP,port))
            if result ==0:
                print(Fore.GREEN + "\nPort {} is open".format(port))
                print(Fore.RESET + "\n")
                openports.append(port)
            s.close()
            with open(f"./Program/scan_res/{filename}.txt", 'w+') as f:
                list_ports = loop()
                f.write(f"Port scan results for {remoteServer}\n\nOpen Ports: {list_ports}\n\n" + "*" * 10 + " Report generated by DokkTX. https://codechaos.net " + "*" * 10)

    except KeyboardInterrupt:
        print("\n Exiting program.")
        sys.exit()
    except gaierror:
        print("\n Hostname could not be resolved.")
        sys.exit()
    except error:
        print("\n Server is not responding.")
        sys.exit()

    #check time again
    current_time_two = datetime.now()

    # Calculate elapsed time
    elapsed_time = current_time_two - current_time
    print(Fore.GREEN + f"Saved the results to Program/scan_res/{filename}")
    main.main()
if __name__ == "__main__":
    scan()