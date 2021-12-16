import re
import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style
init()

def banner():
    banner="""
     _                       _           ___      _ _           _             
  __| | ___  _ __ ___   __ _(_)_ __     / __\___ | | | ___  ___| |_ ___  _ __ 
 / _` |/ _ \| '_ ` _ \ / _` | | '_ \   / /  / _ \| | |/ _ \/ __| __/ _ \| '__|
| (_| | (_) | | | | | | (_| | | | | | / /__| (_) | | |  __/ (__| || (_) | |   
 \__,_|\___/|_| |_| |_|\__,_|_|_| |_| \____/\___/|_|_|\___|\___|\__\___/|_|   
                             By: CyberGuy & BadBot                                           
        """
    print(banner)

isfile=False

def usage():
    usage="""

[+] Welcome to Domain Collector tool, it's a python based tool to get the domains from the crt.sh using the organization name
    [-] python3 domainCollector.py "Org+Inc" => Searching for single organization domains
    [-] python3 domainCollector.py <orgList> => Searching for multiple organizations domains
    """
    print(usage)
    exit()

def collect(org):
    
    print(Fore.YELLOW+ f"\nCollecting [" + Fore.RED + f"{org}" + Fore.YELLOW + "] domains\n")
    
    domains=[]
    
    filename=org.replace(" ", "_")+".txt"

    url="https://crt.sh/?O=%25."

    req=requests.get(url+org)

    soup = BeautifulSoup(req.text, "html.parser")

    td=soup.find_all("td")

    for dom in td:

        domain = re.search('([\w+\d+\-]*)\.(\w+)\.?(jp|es|ar|eu|ca|gov|is|edu|net|it|cn|eg|us|tw|au|sa|info|tr|kr|co.*|com.*)?$', dom.text.strip())

        if domain:
            domain = re.sub(r'^\.', '', domain.group(0))
            domains.append(domain.lower())

    x=set(domains)

    with open(filename, "a") as out:
        for i in x:
            print(Fore.RED + "[+] Collected [ "+ Fore.CYAN + i + Fore.RED + " ]")
            out.write(i+"\n")
        out.close()
    
    print(Fore.RED + f"\nFound => [" + Fore.CYAN + f"{len(x)}" + Fore.RED + "] domains")
    print(Fore.RED + f"\nSaved in => [" + Fore.CYAN + f"{filename}" + Fore.RED + "] file")
    domains=[]

def main():
    if len(sys.argv)==2:
        if os.path.isfile(sys.argv[1]):
            isfile=True
            with open(sys.argv[1]) as orgs:
                for org in orgs:
                    collect(org.strip())
        else:
            collect(sys.argv[1])
    else:
        usage()
if __name__=="__main__":
    banner()
    main()
    print(Fore.WHITE + f"\nHappy Hacking " + Fore.RED + ";)")
