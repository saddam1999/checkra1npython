import wget
import os

try:
    os.remove("program.py")
    print("Old checkra1npython removed")
except FileNotFoundError:
    print("No old checkra1npython delete.")

linkToUpdate = "http://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py"
wget.download(linkToUpdate, 'program.py')
print("Update complete, restarting now.")
#if button not being held down dont reboot

os.popen('sudo reboot')