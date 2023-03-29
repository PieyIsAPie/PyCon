import sys
import argparse
from functions import *
from Color_Console import *
from globals import *
import pyperclip
import distro, platform, random, datetime

ver = "v1.0"
greetings = ["Do I smell ravioli?", "Duck duck goose!", "G'day mate!", "Pizza?", "Let's watch some TV!"]


def leave(code=0):
    print("Goodbye!")
    sys.exit(code)
def leave_(code=0):
    print("\nGoodbye!")
    sys.exit(code)

cmds = {
    "leave": leave,
    "exit": leave,
    "list": list_files,
    "cd": cd,
    "listfc": list_filecontent,
    "listblk": list_disk,
    "filesum": filesum,
    "tcp": tcpclient,
    "udp": udpclient,
    "print": print,
    "askgpt": askgpt,
    "clipcopy": pyperclip.copy,
    "speak": speak,
    "settings": settings,
    "jss": jss,
    "dec": dec,
    "enc": enc
}

def print_greeting():
    today = datetime.date.today()
    isnewyears = (today.day == "01" and today.month == "01")
    ischristmas = (today.day == "25" and today.month == "12")
    isvalentines = (today.day == "14" and today.month == "02")
    ishalloween = (today.day == "31" and today.month == "10")
    isstpd = (today.day == "17" and today.month == "3")
    isremberanceday = (today.day == "11" and today.month == "11")
    isboxingday = (today.day == "26" and today.month == "12")
    print(f"PyCon {ver}, includes {len(cmds)} commands")
    print(f"on {distro.name()} version {distro.version()}")
    print(f"using Python {platform.python_version()} build {platform.python_build()}")
    print(f"branch {platform.python_branch()} with compiler {platform.python_compiler()}.")
    print("")
    if isnewyears:
        print(random.choice(duck_greetings[1]))
    elif ischristmas:
        print(random.choice(duck_greetings[6]))
    elif isvalentines:
        print(random.choice(duck_greetings[2]))
    elif ishalloween:
        print(random.choice(duck_greetings[4]))
    elif isstpd:
        print(random.choice(duck_greetings[3]))
    elif isremberanceday:
        print(random.choice(duck_greetings[5]))
    elif isboxingday:
        print(random.choice(duck_greetings[7]))
    else:
        print(random.choice(greetings))

# Define a function to parse and execute user input
def process_input(input_str: str):
    if input_str == None:
        return
    args = input_str.split()  # Split input string into command and arguments
    command = args[0].lower()  # Convert command to lowercase
    if command in cmds:
        l = cmds[command](*args[1:])
        if l == None:
            pass
        else:
            print(l)
    else:
        print(f"Unknown command: {command}")

# Main loop to read and process user input
print_greeting()
while True:
    try:
        color(text = "bright white" , bg = "blue" , delay = 0.67 ,repeat = -1 , dict = {})
        input_str = input(f"PyCon - {os.getcwd()}> ")  # Prompt user for input
        process_input(input_str)
    except KeyboardInterrupt:  # Handle Ctrl+C
        leave_(0)
        break