import os
import subprocess

class adb:

    CON_CONNECT_SUCCESS = "already connected to"

    PATH_ADB = os.path.split(os.path.realpath(__file__))[0] + "/adb/adb.exe"

    def connect(mobile_ip):
        res = subprocess.check_output([adb.PATH_ADB, "connect", mobile_ip]).decode('utf-8')
        if res.find(adb.CON_CONNECT_SUCCESS) != -1:
            return True
        return False

    def screen_shot(screen_filename):
        subprocess.call([adb.PATH_ADB, "shell", "screencap", "-p", "/sdcard/screen.png"])
        subprocess.call([adb.PATH_ADB, "pull", "/sdcard/screen.png", screen_filename])

    def click(loc):
        subprocess.call([adb.PATH_ADB, "shell", "input", "tap", "{}".format(loc[0]), "{}".format(loc[1])])