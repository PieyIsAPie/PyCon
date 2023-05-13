import subprocess
import platform

WINDOWS = (platform.system == "Windows")
MAC = (platform.system == "Darwin")
LINUX = (platform.system == "Linux")

if WINDOWS:
    print(subprocess.check_output("pyinstaller src\\terminal.py -F --distpath build-target --workpath temp -y --clean --log-level DEBUG --add-data src\\functions.py --add-data src\\globals.py"))
if LINUX or MAC:
    print(subprocess.check_output("pyinstaller src/terminal.py -F --distpath build-target --workpath temp -y --clean --log-level DEBUG --add-data src/functions.py --add-data src/globals.py"))