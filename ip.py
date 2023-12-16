import os,time,requests
#----------[basic colors]----------#
green="\033[1;32m";red="\033[1;31m";reset="\033[0m"
#----------[main logo]----------#
def logo():
 os.system("clear");print(f'''{reset} ╦╔═╗  ╦ ╦┌┐┌┬  ┌─┐┌─┐┬┌─
 {red}║╠═╝  ║ ║││││  │ ││  ├┴┐{reset}
 ╩╩    ╚═╝┘└┘┴─┘└─┘└─┘┴ ┴

 Author  : Aadi Malik
 Contact   : +923030605653
{50 * '-'}''')
def ip():
 ip = requests.get("https://api.ipify.org").text
 logo()
 print(f"\n [{red}•{reset}] USE AIRPLANE MODE FOR 5 SEC BEFORE USE . ") 
 input(f" [{red}•{reset}] PRESS ENTER TO START ... ") 
 print(50*'\033[1;97m-')
 print(f" [{red}•{reset}] DETECTING YOUR IP ADDRESS ... ");time.sleep(3)
 print(f" [{red}•{reset}]{green} YOUR IP ADDRESS : {ip} ")
 print(f" {reset}[{red}•{reset}]{green} TRYING TO UNBLOCK YOUR IP ... ");time.sleep(3)
 print(f" {reset}[{green}✓{reset}]{green} YOUR IP UNBLOCK SUCCESSFULLY \n\n ")
 exit() 
ip()