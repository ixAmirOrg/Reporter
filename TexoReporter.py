#############################################################################################
#  _          _              _       ___            
# (_)_  __   / \   _ __ ___ (_)_ __ / _ \ _ __ __ _ 
# | \ \/ /  / _ \ | '_ ` _ \| | '__| | | | '__/ _` |
# | |>  <  / ___ \| | | | | | | |  | |_| | | | (_| |
# |_/_/\_\/_/   \_\_| |_| |_|_|_|   \___/|_|  \__, |
#                                             |___/  on GitHub : https://github.com/ixAmirOrg 
#############################################################################################

from telethon import TelegramClient
from telethon import functions, types, errors
from os import system
from colorama import Fore as Coloresh
import asyncio#, logging
from requests import get
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)
#logger = logging.getLogger(__name__)

async def banner(a):
    if a:
        system("clear")
        system('figlet -c "TexoTm"| lolcat -a -d -p 10')
        system('echo Texo Reporter V1.02 | lolcat -a -d 30')
        system("echo hTtPs://t.Me/TexoTm | lolcat")
        system("echo Using Free Version To Upgrade Contact In Telegram | lolcat")
        system("date | lolcat")
    if not a:
        system("clear")
        system('figlet -c "TexoTm"| lolcat -a -d -p 5')
        system('echo Texo Reporter V1.02 | lolcat -a -d 15')
        system("echo hTtPs://t.Me/TexoTm | lolcat")
        system("echo Using Free Version To Upgrade Contact In Telegram | lolcat")
        system("date | lolcat")
        

async def main():
    await banner(True)
    global client
    api_id = 0000000
    api_hash = ""
    client = TelegramClient("data", api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
    	q = True
    	phone = input(Coloresh.RED+"[?] "+Coloresh.LIGHTGREEN_EX+"Enter "+Coloresh.LIGHTMAGENTA_EX+"YOUR "+Coloresh.YELLOW+"Phone"+Coloresh.RED+" Number "+Coloresh.LIGHTGREEN_EX+"=> "+Coloresh.LIGHTMAGENTA_EX)
    	send = await client.send_code_request(phone)
    	code = input(Coloresh.RED+"[?]"+Coloresh.BLUE+"Please Enter The"+Coloresh.YELLOW+" Code => "+Coloresh.LIGHTMAGENTA_EX)
    	
    	try:
    	    await client.sign_in(phone, code)
    	except errors.SessionPasswordNeededError:
    	    passwd = input(Coloresh.RED+"[?]"+Coloresh.LIGHTGREEN_EX+"Enter Your Account "+Coloresh.LIGHTMAGENTA_EX+"Password => "+Coloresh.YELLOW)
    	    await client.sign_in(password = passwd)
    	try:
    		await client(functions.channels.JoinChannelRequest(channel='TexoTm'))
    	except:
    	    pass
    	if q == True:
    	    await banner(False)
    	else:
    	    pass
    #print (Coloresh.RED+"[☆] "+Coloresh.LIGHTGREEN_EX+"SuCceSsfuL "+Coloresh.LIGHTMAGENTA_EX+"ConneCtinG "+Coloresh.YELLOW+":)"+Coloresh.BLUE)

    a = client.is_connected()
    if a == True:
        print ("\n"+Coloresh.RED+"[☆] "+Coloresh.LIGHTGREEN_EX+"SuCceSsfuLy "+Coloresh.LIGHTMAGENTA_EX+"ConneCtEd "+Coloresh.YELLOW+":)"+Coloresh.BLUE)
    elif a == False:
        print("\n"+Coloresh.RED+"[!!]"+Coloresh.YELLOW+"Not Connected ! Please Check "+ Coloresh.LIGHTMAGENTA_EX+ "Your Connection And "+Coloresh.LIGHTGREEN_EX+"Retry ♡"+ Coloresh.GREEN)
    #print(Coloresh.RED+"\n[?] "+Coloresh.BLUE+"DrAnDrOiD "+Coloresh.RED+"Reporter "+Coloresh.YELLOW+"V1.01")
    try:
    	feshar = int(input(Coloresh.RED+"[?] "+Coloresh.LIGHTGREEN_EX+"Enter "+Coloresh.RED+"Number "+Coloresh.GREEN+"Of "+Coloresh.LIGHTCYAN_EX+"Report "+Coloresh.GREEN+"Bemola"+Coloresh.MAGENTA+"--> "+Coloresh.LIGHTGREEN_EX))
    except:
    	print(Coloresh.RED+"[!] "+Coloresh.YELLOW+"Eshteba zadi"+Coloresh.LIGHTGREEN_EX+ "dash adad"+Coloresh.LIGHTMAGENTA_EX+" bezan bemola")
    	exit()
    if feshar == "" or feshar == " ":
    	print(Coloresh.RED+"[!] "+Coloresh.BLUE+"Eshteba zadi"+Coloresh.LIGHTGREEN_EX+"dash"+Coloresh.MAGENTA)
    	exit()
    if feshar < 5:
    	print(Coloresh.RED+"[!] "+Coloresh.YELLOW+"dash fesharesh "+Coloresh.RED+"kheili "+Coloresh.LIGHTGREEN_EX+"kame dardesh "+Coloresh.YELLOW+"nemiad"+Coloresh.BLUE)
    	exit()
    username = input(Coloresh.RED+"[?] "+Coloresh.LIGHTGREEN_EX+"Send "+Coloresh.GREEN+"Target "+Coloresh.YELLOW+"Channel / Group "+Coloresh.LIGHTCYAN_EX+"UserName "+Coloresh.BLUE+"(Without @) "+Coloresh.MAGENTA+"=> "+Coloresh.LIGHTGREEN_EX)
    if username == "" or username == " " or " " in username:
    	print(Coloresh.RED+"[!] "+Coloresh.BLUE+"dash eshteba zadi "+Coloresh.MAGENTA+"bemola ke"+Coloresh.YELLOW)
    	exit()
    try:
    	username = username.replace('@', '')
    except:
    	pass
    r = get("https://t.me/"+username)
    if not "Preview channel" in r.text:
        if not "online" in r.text:
            print(Coloresh.RED+"[!] "+Coloresh.LIGHTGREEN_EX+"channel is "+Coloresh.RED+"invalid !"+Coloresh.RED)
            exit()
    message_id = input(Coloresh.RED+"[?] "+Coloresh.LIGHTGREEN_EX+"Send "+Coloresh.GREEN+"Target "+Coloresh.YELLOW+"Channel / Group "+Coloresh.LIGHTCYAN_EX+"Post "+Coloresh.BLUE+"Id "+Coloresh.MAGENTA+"=> "+Coloresh.LIGHTGREEN_EX)
    try:
        rsn = int(input(Coloresh.LIGHTGREEN_EX+"[?] "+Coloresh.LIGHTGREEN_EX+"choose reason "+Coloresh.YELLOW+"for report :\n1."+Coloresh.RED+"porn\n2"+Coloresh.MAGENTA+".spam\n3."+Coloresh.LIGHTMAGENTA_EX+"Copyright  "+Coloresh.LIGHTGREEN_EX+"=> "+Coloresh.LIGHTGREEN_EX))
    except:
        print(Coloresh.RED+"[!]"+Coloresh.MAGENTA+"dash fagat bayad "+Coloresh.YELLOW+"addad bezani "+Coloresh.BLUE+"bemola ke !"+Coloresh.LIGHTGREEN_EX)
        exit()
    msg = input(Coloresh.LIGHTGREEN_EX+"[?]"+Coloresh.MAGENTA+"Enter a Message"+Coloresh.BLUE+" to report the "+Coloresh.RED+"channel / group => "+Coloresh.YELLOW)
    if rsn == 1:
        rsn = types.InputReportReasonPornography()
    elif rsn == 2:
        rsn = types.InputReportReasonSpam()
    elif rsn == 3:
        rsn = types.InputReportReasonCopyright()
    else:
        print(Coloresh.RED+"[!]"+Coloresh.LIGHTGREEN_EX+"dash fagat as "+Coloresh.YELLOW+"list entekhab"+Coloresh.BLUE+" kon !"+Coloresh.LIGHTMAGENTA_EX)
        exit()
    i = 0
    print(Coloresh.RED+"[☆]"+Coloresh.LIGHTGREEN_EX+"Starting "+Coloresh.YELLOW+"Please wait"+Coloresh.BLUE+"...."+Coloresh.LIGHTMAGENTA_EX)
    while True:
        if i == feshar:
            print(Coloresh.RED+"[✅] "+Coloresh.LIGHTGREEN_EX+"SuCcEssfulLy "+Coloresh.CYAN+"Finished "+Coloresh.RED+"Sending Requests "+Coloresh.LIGHTMAGENTA_EX+"Sended =>  "+Coloresh.YELLOW+str(i))

            break
        
        a = await client(functions.messages.ReportRequest(
            peer='@'+username,
            id=[int(message_id)],
            reason=rsn,
            message = msg
        ))
        b = await client(functions.account.ReportPeerRequest(
            peer='@'+username,
            reason=rsn,
            message = msg
        ))
        if a == True:
            print(Coloresh.RED+"[?] "+Coloresh.LIGHTGREEN_EX+"SuCcEssfulLy "+Coloresh.CYAN+"Send "+Coloresh.RED+"Request "+Coloresh.LIGHTMAGENTA_EX+"Sended =>  "+Coloresh.YELLOW+str(i), end = "\r")
            i += 1
        if i == feshar:

            print(Coloresh.RED+"[✅] "+Coloresh.LIGHTGREEN_EX+"SuCcEssfulLy "+Coloresh.CYAN+"Finished "+Coloresh.RED+"Sending Requests "+Coloresh.LIGHTMAGENTA_EX+"Sended =>  "+Coloresh.YELLOW+str(i))

            break
        if b == True:
            print(Coloresh.RED+"[?] "+Coloresh.LIGHTGREEN_EX+"SuCcEssfulLy "+Coloresh.CYAN+"Send "+Coloresh.RED+"Request "+Coloresh.LIGHTMAGENTA_EX+"Sended =>  "+Coloresh.YELLOW+str(i), end = "\r")
            i += 1
        if i == feshar:
            print(Coloresh.RED+"[✅] "+Coloresh.LIGHTGREEN_EX+"SuCcEssfulLy "+Coloresh.CYAN+"Finished "+Coloresh.RED+"Sending Requests "+Coloresh.LIGHTMAGENTA_EX+"Sended =>  "+Coloresh.YELLOW+str(i))
            break



asyncio.run(main())

