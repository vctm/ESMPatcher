import os
os.system("mode con cols=75 lines=21")
import time
import requests
import colorama
from colorama import Fore, Back
colorama.init()
import webbrowser
import sys
import zlib
from typing import BinaryIO, List, Optional, Tuple

Color_1 = Fore.YELLOW
Color_2 = Fore.RED
Color_3 = Fore.WHITE
Color_7 = Fore.CYAN
Color_4 = Back.YELLOW
Color_5 = Back.RED
Color_6 = Back.WHITE
BackReset = Back.RESET
ForeReset = Fore.RESET

Logo = f"""
  {Color_1}                      ___________ __  ___                
  {Color_2}                     / ____/ ___//  |/  /                
  {Color_1}                    / __/  \__ \/ /|_/ /                 
  {Color_2}                   / /___ ___/ / /  / /                  
  {Color_1}                 _/_____//____/_/__/_/____  ____________ 
  {Color_2}                / __ \/   |/_  __/ ____/ / / / ____/ __ \
  {Color_1}                                / /_/ / /| | / / / /   / /_/ / __/ / /_/ /
  {Color_2}              / ____/ ___ |/ / / /___/ __  / /___/ _, _/ 
  {Color_1}             /_/   /_/  |_/_/  \____/_/ /_/_____/_/ |_|      """

Selections = f"""
  {Color_7}╔═════════════════════════════════════════════════════════════════════╗
       {Color_2}v1.0.1               {Color_5}█{Color_4}Selection Screen{Color_5}█{Color_3}{BackReset}           {Color_2}victim#5787{Color_3}    
  {Color_7}╠═══════════════════════════════════╦═════════════════════════════════╣
  {Color_7}║      {Color_1}1 {Color_7}> {Color_3}Patch SeventySix.esm     {Color_7}║      {Color_1}4 {Color_7}> {Color_3}GitHub Repo            {Color_7}║
  {Color_7}║      {Color_1}2 {Color_7}> {Color_3}Fetch CRC32 Value        {Color_7}║      {Color_1}5 {Color_7}> {Color_3}Changelog              {Color_7}║
  {Color_7}║      {Color_1}3 {Color_7}> {Color_3}Free Hex Edits           {Color_7}║      {Color_1}6 {Color_7}> {Color_3}Exit                   {Color_7}║
  {Color_7}╠═══════════════════════════════════╩═════════════════════════════════╣
  {Color_7}║      {Color_3}Type a number or "{Color_1}CREDITS{Color_3}" / "{Color_1}SETTINGS{Color_3}" and press {Color_1}[ENTER]{Color_3}.     {Color_7}║
  {Color_7}╚═════════════════════════════════════════════════════════════════════╝ {ForeReset}
"""

def Loading():
    time.sleep(1)
    print('  Current Version: v1.0.0')
    pastebin_raw_link = 'https://pastebin.com/raw/Wzrn3Uue'
    response = requests.get(pastebin_raw_link)
    source_code = response.content
    print(source_code.decode('utf-8'))
    time.sleep(1)
    Main()

def Main():
    os.system('cls')
    print(Logo)
    print(Selections)
    choice = input(f'  {Color_7}>{ForeReset} ')
    if choice == '1': # Patch
        print(PatchInstructions)
        # Patcher Here
        time.sleep(30)
        Main()
    if choice == '2': # Fetch CRC32 Value
        # Uses a Pastebin I have to auto-update, find a way to get it locally from fallout76.exe?
        print(f'  {Color_1}Fetching CRC32 Value!{ForeReset}')
        pastebin_raw_link = 'https://pastebin.com/raw/S30ubGbe'
        response = requests.get(pastebin_raw_link)
        source_code = response.content
        print(source_code.decode('utf-8'))
        # CRC32 Stuff Here
        time.sleep(2)
        print(ReturningIn10)
        time.sleep(10)
        Main()
    if choice == '3': # Free Hex Edits
        print(f'  {ForeReset}Thanks to {Color_7}Suchi96{ForeReset} for posting these values publicly!')
        print(f'  {ForeReset}Opening {Color_2}github.com/Suchi96/Fallout-76-Modding{ForeReset} in your browser!')
        webbrowser.open('https://github.com/Suchi96/Fallout-76-Modding', new=2)
        time.sleep(1)
        print(ReturningIn5)
        time.sleep(5)
        Main()
    if choice == '4': # GitHub Repo
        print(f'  {Color_1}Opening GitHub Repo in your browser!')
        webbrowser.open('https://github.com/vctm/ESMPatcher', new=2)
        time.sleep(1)
        print(ReturningIn5)
        time.sleep(5)
        Main()
    if choice == '5': # Changelog
        # Pastebin as used in 2
        pastebin_raw_link = 'https://pastebin.com/raw/nbUT5hNW'
        response = requests.get(pastebin_raw_link)
        source_code = response.content
        print(source_code.decode('utf-8'))
        time.sleep(15)
        Main()
    if choice == '6': # Exit
        print(f'  {Color_2}Exiting!{ForeReset}')
        time.sleep(1)
        exit(0)
    if choice == 'CREDITS': # CREDITS
        print(Credits)
    if choice == 'SETTINGS': # Settings
        print(f'  {Color_1}Coming in a future version!{ForeReset}')
        print('  ')
        print(f'  {ForeReset}3')
        time.sleep(1)
        print(f'  {ForeReset}2')
        time.sleep(1)
        print(f'  {ForeReset}1')
        time.sleep(1)
        # Theme Settings
        # Maybe change filename and CRC32 value?
        # Creative Settings as filler
        Main()
    else:
        print(Invalid_Input)
        time.sleep(1)
        print(f'  Returning to Selection Screen.')
        time.sleep(2)
        Main()

PatchInstructions = f"""
  patch here
"""

ReturningIn10 = f"""
  {Color_1}Returning to menu in 10 seconds.{ForeReset}"""

ReturningIn5 = f"""
  {Color_2}Returning to menu in 5 seconds.{ForeReset}"""

Invalid_Input = f"""
  {Color_2}Error: {ForeReset}Invalid Input!"""

Credits = f"""
  victim#5787
"""

Loading()
