import pygeoip
from colorama import Fore
import os
import main
gi = pygeoip.GeoIP('./geo.dat')

def track():
    try:
        tgt = input("Please provide the ip adress:")
        filename = input("Please provide the name for the file to save the results to.")
        rec = gi.record_by_addr(tgt)
        city = rec['city']
        country = rec['country_name']
        postal_code = rec['postal_code']
        areacode = rec['area_code']
        long = rec['longitude']
        lat = rec['latitude']
        dma_code = rec['dma_code']
        region_code = rec['region_code']
        timezone = rec['time_zone']
        print(f"[*] Target found {tgt}")
        print(Fore.RED + f"Information: \nCity: {city}\nArea code: {areacode}\nCountry: {country}\nPostal Code: {postal_code}\nLongtitude: {long}\nLatitude: {lat}\nDma code: {dma_code}\nTimezone: {timezone}\nRegion Code: {region_code} ")
        print(Fore.GREEN + "Writing output to file.......")
    except OSError:
        print(Fore.RED + "THAT IS NOT A VALID IP ADDRESS. Please use a different one!\n")
        os.system('sleep 10')
        main.main()
    except TypeError:
        print(Fore.RED + "THAT IS NOT A VALID IP ADDRESS. Please use a different one!\n")
    try:
        with open(f"ProgramFiles/iptrack-{filename}.txt", 'w+') as f:
            f.write(f"IP tracker results for {tgt}\n\nCity: {city}\nCountry: {country}\nPostal Code: {postal_code}\nArea Code: {areacode}\nLongtitude: {long}\nLatitude: {lat}\nDMA Code: {dma_code}\nRegion Code: {region_code}\nTimezone: {timezone}\n" + "*" * 10 + "Generated by DokkTX. https://codechaos.net" + "*" * 10)
            print(Fore.GREEN + "Done.")
            os.system("sleep 10")
            main.main()
    except Exception as e:
        print(e)