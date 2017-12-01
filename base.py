import os
import subprocess

def commands():
    files = list()
    for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if file.endswith(".py"):
            files.append(file)

    for file in files:
        exit()

#clears the console window, but does not delete imports or variables
def clear():
    subprocess.call("clear")

#runs a pip install with the specified module
def install(module):
    subprocess.call("pip.exe install " + module)

###allows to call exit() and quit() without parentheses
class exit(object):
    exit = exit # original object
    def __repr__(self):
        self.exit() # call original
        return ''

quit = exit = exit()
