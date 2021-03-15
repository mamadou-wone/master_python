#  _       ______  _   ________
# | |     / / __ \/ | / / ____/
# | | /| / / / / /  |/ / __/
# | |/ |/ / /_/ / /|  / /___
# |__/|__/\____/_/ |_/_____/

from pyfiglet import Figlet
import os

text = Figlet(font="slant")
os.system("cls")
os.system("mode con: cols=75 lines=75")
print(text.renderText("WONE"))