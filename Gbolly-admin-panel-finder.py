#!/usr/bin/python3
# -*- coding: utf-8 -*-
# created by Omotosho Gbolahan
import os
import sys
import requests
import time
import random
import string
from time import sleep


#### colours ####
# B='\033[1;94m'
# R='\033[1;91m'
# G='\033[1;92m'
# W='\033[1;97m'
# S='\033[1;96m'
# P='\033[1;95m'
# Y='\033[1;93m'
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'


Gbolahan ="""\033[1;93m


      
                                                                                     
                            \033[1;94mAdmin+-+Panel+-+Finder 

               👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹👹                                
                                                                                   
                     \033[1;96mCreated by Omotosho Gbolahan Hammed                 
                    
                   👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺

                                                                
                        \033[1;95mFacebook: Gbolahan Omotosho                           
                        \033[1;91mInstagram: _lord_of_hacker                            
                        \033[1;92mWhatsapp: 08022648626                                 
                        \033[1;97mGithub: github.com/Gbolahanomotosho                   
                   😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈                                                              
       



\033[1;93m"""

for i in Gbolahan:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
    


url = input("\033[1;96mEnter target url either with http:// or https:// e.g https://example.com : ")


Gbolly = open("Gbolly.txt","r")


def Gbolly_admin_panel_finder():

    for word in Gbolly:

        response = requests.get(url + word)
        response.status.code = str(request.status_code)
    if response.status.code == 200:
        print(url + admin + "\033[1;92mAdmin panel found")
    elif response.status.code == 403:
        print(url + admin + "\033[1;93m403 Forbidden")
    elif response.status.code == 404:
        print(url + admin + "\033[1;91m404 not found")
    elif  response.status.code == 302:
        print(url + admin + "\033[1;94mRedirecting")

    
Gbolly_admin_panel_finder()
