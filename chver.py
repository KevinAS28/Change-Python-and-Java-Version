#!/usr/bin/python3

import sys
import os
import time

def spab(x):
 for abc in range(x):
  print(' ')
print('''pengubah versi bahasa programming

1.python

2.java

by kevin A ''')

spab(5)
pilih = input('angka: ')
pilih = int(pilih)
spab(5)
skr = os.getcwd()
print('anda sekarang ada di ' + skr)
spab(5)
dirs = '/root/programming/python_saya'
if (str(skr)) != (str(dirs)):
 print('sedang tidak di python_saya')
 time.sleep(0.5)
 print('merubah ke python_saya')
 os.chdir('/root/programming/python_saya')
 eko = os.getcwd()
 print('dan sekarang ada di ' + eko)


if pilih == 1:
 script = """update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
update-alternatives --config python
"""
 os.system(script)

if pilih == 2:
 os.system('sudo update-alternatives --config java') 
 os.system('sudo update-alternatives --config javac')
 spab(5)
 os.system('java -version')



