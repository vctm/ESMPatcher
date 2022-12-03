import os
os.system("mode con cols=75 lines=21")
import time
import colorama
from colorama import Fore, Back
colorama.init()
import webbrowser

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
       {Color_2}v1.0.0               {Color_5}█{Color_4}Selection Screen{Color_5}█{Color_3}{BackReset}           {Color_2}victim#5787{Color_3}    
  {Color_7}╠═══════════════════════════════════╦═════════════════════════════════╣
  {Color_7}║      {Color_1}1 {Color_7}> {Color_3}Patch SeventySix.esm     {Color_7}║      {Color_1}4 {Color_7}> {Color_3}GitHub Repo            {Color_7}║
  {Color_7}║      {Color_1}2 {Color_7}> {Color_3}Fetch CRC32 Value        {Color_7}║      {Color_1}5 {Color_7}> {Color_3}Changelog              {Color_7}║
  {Color_7}║      {Color_1}3 {Color_7}> {Color_3}Free Hex Edits           {Color_7}║      {Color_1}6 {Color_7}> {Color_3}Credits                {Color_7}║
  {Color_7}╠═══════════════════════════════════╩═════════════════════════════════╣
  {Color_7}║       {Color_3}Type a number or "{Color_1}SETTINGS{Color_3}" / "{Color_1}EXIT{Color_3}" and press {Color_1}[ENTER]{Color_3}.       {Color_7}║
  {Color_7}╚═════════════════════════════════════════════════════════════════════╝ {ForeReset}
"""

def Main():
    os.system('cls')
    print(Logo)
    print(Selections)
    choice = input('  > ')
    if choice == '1':
        print(PatchInstructions)
        # Patcher Here
        time.sleep(30)
        Main()
    if choice == '2':
        print('Fetching CRC32 Value!')
        # CRC32 Stuff Here
        time.sleep(3)
        Main()
    if choice == '3':
        print('Thanks to Suchi96 for posting these publicly! Opening in your Browser.')
        webbrowser.open('https://github.com/Suchi96/Fallout-76-Modding', new=2)
        time.sleep(5)
        Main()
    if choice == '4':
        print('Opening GitHub Repo in your browser!')
        webbrowser.open('https://https://github.com/vctm/ESMPatcher', new=2)
        time.sleep(5)
        Main()
    if choice == '5':
        # If smart enough try and use Gists/GitHub more likely just write a new message inside script with each version change.
        time.sleep(3)
        Main()
    if choice == '6':
        print(Credits)
    if choice == 'SETTINGS':
        print('Hello!')
        # Theme Settings
        # Maybe change filename and CRC32 value?
        # Creative Settings as filler
        time.sleep(3)
        Main()
    if choice == 'EXIT':
        print(Exit)
        time.sleep(3)
        exit(0)
    else:
        print(Invalid_Input)
        time.sleep(2)

Invalid_Input = f"""
  {Color_3}Error: Invalid Input!
"""

Exit = f"""
  {Color_2}Exiting!
"""

Credits = f"""
  victim#5787
"""

Main()
