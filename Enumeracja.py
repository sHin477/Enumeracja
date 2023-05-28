import pyfiglet
import os
import subprocess

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

class IP:
    def __init__(self, in1, in2): 
        self.ip1 = in1
        self.ip2 = in2

in1 = input("""\nProsze podaj jaki typ skanu wykonac
                1)  OS skan
                2)  Vuln Skan
                3)  Enum4linux
                4)  Dirb/Dirbuster
                5)  WPScan
                6)  SNMPWalk\n""")
print("You have selected option:", in1)

if in1 == '1':
    in1 = input("Tu wpisz IP: ")
    # Opcja skanowania OS
    def scan1(ip):
        print(f"Skanowanie {ip}, To moze troche potrwac...")
        command = ["nmap", "-F", "-Pn", "-sV", "--stats-every", "1s", in1]
        nmap_output = subprocess.run(command, capture_output=True, text=True).stdout
        print(nmap_output)
        with open("wynik_skanu.txt", "w+") as f:
            f.write(nmap_output)

    if in1:
        scan1(in1)

elif in1 == '3':
    in1 = input("Tu wpisz IP: ")
    # Opcja enum4linux
    enum4linux_command = ["enum4linux", in1]
    enum4linux_output = subprocess.run(enum4linux_command, capture_output=True, text=True).stdout
    print(enum4linux_output)

elif in1 == '4':
    in1 = input("Tu wpisz adres URL: ")
    # Opcja Dirb/Dirbuster
    dirb_command = ["dirb", in1]
    dirb_output = subprocess.run(dirb_command, capture_output=True, text=True).stdout
    print(dirb_output)

elif in1 == '5':
    in1 = input("Tu wpisz adres URL: ")
    # Opcja WPScan
    wpscan_command = ["wpscan", "--url", in1]
    wpscan_output = subprocess.run(wpscan_command, capture_output=True, text=True).stdout
    print(wpscan_output)

elif in1 == '6':
    in1 = input("Tu wpisz IP: ")
    # Opcja SNMPWalk
    snmpwalk_command = ["snmpwalk", "-v2c", "-c", "public", in1]
    snmpwalk_output = subprocess.run(snmpwalk_command, capture_output=True, text=True).stdout
    print(snmpwalk_output)

print("Skanowanie ukonczone!")
