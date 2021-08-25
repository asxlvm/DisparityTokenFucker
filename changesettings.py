import json, sys
import colorama
colorama.init()
from colorama import Fore, Back, Style
from pprint import PrettyPrinter
from pyfiglet import Figlet
f = Figlet(font="poison")
pp = PrettyPrinter(indent=2)
def getSettings():
    with open("settings.json", "r") as f:
        return json.load(f)
def mainMenu():
    settings = getSettings()
    print(Fore.RED + f.renderText("Settings"))
    print("\nCurrent Settings:")
    pp.pprint(settings)
    print(Style.RESET_ALL)
    done = False
    while done == False:
        try:
            print("\n" + Fore.RED + "[1] Server Name\n[2] Server Count\n[3] Accent Color (banner)\n[4] Bio (About Me)\n[5] Exit")
            inp = int(input("What would you want to change?"))
            if inp == 1:
                done = True
                changeSettings("server_name")
            elif inp == 2:
                done = True
                changeSettings("server_count")
            elif inp == 3:
                done = True
                changeSettings("accent_color")
            elif inp == 4:
                done = True
                changeSettings("bio")
            elif inp == 5:
                done = True
                sys.exit()
            else:
                continue
        except:
            continue

def changeSettings(val):
    settings = getSettings()
    try:
        typeInput = getattr(__builtins__, type(settings[val]).__name__)
    except Exception as e:
        print(Fore.RED + f"{e}")
        mainMenu()
    try:
        inp = typeInput(input(Fore.RED + f"What do you want to change {val} to?"))
    except Exception as e:
        print(Fore.RED + f"{e}")
        mainMenu()
    try:
        if type(inp).__name__ == type(settings[val]).__name__:
            pass
        else:
            print(Fore.RED + f"{val} is a type of {type(settings[val]).__name__} not {type(val).__name__}, going in main menu" + Style.RESET_ALL)
            mainMenu()
            return
    except Exception as e:
        print(Fore.RED + f"An exception occured, exiting | {e}" + Style.RESET_ALL)
        sys.exit()
#    typeInput = getattr(__builtins__, type(val).__name__)
#    inp = typeInput(input(Fore.RED + f"What do you want to change {val} to?"))
#    print(inp)
#    print(settings)
#    print(settings[val])
#    print(type(settings))
    settings[val] = inp
    with open("settings.json", "w") as f:
        json.dump(settings, f)
    return mainMenu()

mainMenu()
