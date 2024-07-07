import csv
import os
from realproj import *

while True:
    f=input('Path of file:')
    f2=open(f,'a+')
    fcontent=f2.read()
    print(fcontent)
    usr_choose=input('Command:')
    if usr_choose=='F':
        finduser()
    if usr_choose=='A':
        useradd()
    if usr_choose=='L':
        listusers()
    if usr_choose=='D':
        userdel()
    elif usr_choose=='Q':
        break
