import requests
import sys
from colorama import Fore, Style
ports={'node-exporter':"9100",'grafana':"3000",'cadvisor':"9092",'promtail':"9081",'alertmanager':"9093",'prometheus':"9090",'loki':"3100"}

if len(sys.argv) > 2:
  for i in range(2, len(sys.argv)):
      url = "http://"+sys.argv[1]+":"+sys.argv[i]

      resp = requests.get(url)
      if resp.status_code == 200:
         print(Fore.GREEN + "service on address:",sys.argv[1],"on port:",sys.argv[i],"is OK with code",resp.status_code)
      elif resp.status_code == 404 and sys.argv[i] == "3100":
         print(Fore.GREEN + "service on address:",sys.argv[1],"on port:",sys.argv[i],"is OK with code",resp.status_code)
      elif resp.status_code > 400:
         print(Fore.RED + "service on address:",sys.argv[1],"on port:",sys.argv[i],"is UNHEALTHY with code",sys.argv[i],resp.status_code)


elif len(sys.argv) == 2:
     print (Fore.YELLOW + "Using default ports")
     for key in ports.keys():
         url = "http://"+sys.argv[1]+":"+ports[key]
         resp = requests.get(url)
         if resp.status_code == 200:
            print(Fore.GREEN + key,"service is READY with code:", resp.status_code)
         elif resp.status_code == 404 and key == "loki":
            print(Fore.GREEN + key,"service is OK with code:", resp.status_code)
         elif resp.status_code > 400:
            print(Fore.RED + key,"service is UNHEALTHY with code:", resp.status_code)
