from os import system 
from arsein import Messenger 
from colorama import Fore as f

system("clear")

print(f"""{f.BLUE}███████╗██╗███╗   ██╗██████╗ ██╗   ██╗███████╗███████╗██████╗ 
██╔════╝██║████╗  ██║██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ██║██║   ██║███████╗█████╗  ██████╔╝
██╔══╝  ██║██║╚██╗██║██║  ██║██║   ██║╚════██║██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║██████╔╝╚██████╔╝███████║███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                              
             {f.RED}Creator > {f.BLUE} @GOD_NUM_1                                                
                                 
                                                                               """)

bot = Messenger("#AUTH")
user = str(input(f"{f.YELLOW}Enter Username{f.WHITE}>{f.MAGENTA} "))
print("")

x = bot.checkUserUsername(username=user)['status']
if x == 'OK':
    print(f"""{f.BLUE}Username {f.RED}=> {f.YELLOW}{user}
{f.BLUE}Have an Account {f.RED}=>{f.GREEN} YES""")
elif x == "NO":
    print(f"""{f.BLUE}Username {f.RED}=> {f.YELLOW}{user} 
{f.BLUE}Have an Account {f.RED}=>{f.RED} NO""")

