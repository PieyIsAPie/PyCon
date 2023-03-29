import os
import platform
from pathlib import Path
import configparser
from enum import Enum

DEFAULTCONFIG = """
[Settings.Color]
Back=Blue
Fore=BrightWhite

[Settings.OpenAI-AskGPT]
API_KEY=
model=text-davinci-003
suffix=
max_tokens=150
temperature=1
top_p=
n=1
stream=False
logprobs=None
echo=False
stop=None
presence_penalty=0
frequency_penalty=0
best_of=1
logit_bias=None
user=
"""

scriptdir = os.path.dirname(os.path.realpath(__file__))
WINDOWS = platform.system() == "Windows"
MAC = platform.system() == "Darwin"
LINUX = platform.system() == "Linux"
if WINDOWS:
    configp = f"{os.getenv('appdata')}\\pyconcfg.ini"
elif LINUX or MAC:
    configp = f"{Path.home()}/pyconcfg.ini"

def loadcfg():

    if not os.path.exists(configp):
        open(configp, "w+").write(DEFAULTCONFIG)

    cfg = configparser.ConfigParser()
    cfg.read(configp)
    return cfg

cfg = loadcfg()

class Holiday(Enum):
    NEW_YEARS_DAY = "New Year's Day"
    VALENTINES_DAY = "Valentine's Day"
    ST_PATRICKS_DAY = "St. Patrick's Day"
    GOOD_FRIDAY = "Good Friday"
    EASTER_MONDAY = "Easter Monday"
    VICTORIA_DAY = "Victoria Day"
    CANADA_DAY = "Canada Day"
    LABOUR_DAY = "Labour Day"
    THANKSGIVING = "Thanksgiving Day"
    HALLOWEEN = "Halloween"
    REMEMBRANCE_DAY = "Remembrance Day"
    CHRISTMAS_DAY = "Christmas Day"
    BOXING_DAY = "Boxing Day"
duck_greetings = {
    Holiday.NEW_YEARS_DAY: [
        "Happy New Year! Time to debug your resolutions and quack your way into a fantastic year ahead!",
        "Welcome back! Let's duck dive into the New Year and code up some success!",
        "New Year, new code! Let's waddle into the year ahead with fresh ideas and duck determination!"
    ],
    Holiday.VALENTINES_DAY: [
        "Roses are red, violets are blue, our code is sweet, and so are you! Happy Valentine's Day!",
        "Spread the love like a duck in a pond, and share it with the ones who make your code bond. Happy Valentine's Day!",
        "Happy Valentine's Day! Let's code with love and make our digital world as warm as a duck's embrace!"
    ],
    Holiday.ST_PATRICKS_DAY: [
        "Top o' the morning to ya! May your code be as lucky as a duck on St. Paddy's Day!",
        "You've found the end of the rainbow, now let's code some gold together! Happy St. Patrick's Day!",
        "Happy St. Patrick's Day! Let your code take flight like a duck soaring over fields of green!"
    ],
    Holiday.HALLOWEEN: [
        "Happy Halloween! Don't let your code get spooked, debug it like a duck hunting for treats!",
        "Trick or treat? Let's code some wickedly good software this Halloween and quack up the night!",
        "This Halloween, let's transform our code into a masterpiece, just like a duck dressed up for a night of fun!"
    ],
    Holiday.REMEMBRANCE_DAY: [
        "Lest we forget, let's code in honor of those who made the ultimate sacrifice, like ducks flying in formation.",
        "On Remembrance Day, let's pay tribute to our heroes and write code that makes a difference.",
        "This Remembrance Day, let's commit to creating a better digital world in honor of those who fought for our freedom."
    ],
    Holiday.CHRISTMAS_DAY: [
        "Merry Christmas! May your code be as merry and bright as a duck enjoying a festive winter wonderland!",
        "Season's greetings! Let's code some holiday cheer and make the digital world as jolly as a Christmas duck!",
        "Happy holidays! Let's celebrate the magic of the season by coding together like a flock of festive ducks!"
    ],
    Holiday.BOXING_DAY: [
        "Happy Boxing Day! Unwrap your coding talents like a gift and share them like a generous duck!",
        "Welcome back! Let's make a splash this Boxing Day and code something as delightful as a duck in a pond!",
        "Boxing Day greetings! Dive into the spirit of giving and let's share our code with the world, like a duck spreading joy."
    ]
}