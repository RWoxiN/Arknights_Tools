import time

from Base.mobile import *
from discern import *
from arknights import *

MOBILE_IP = "127.0.0.1:12283"

if not adb.connect(MOBILE_IP):
    print("cannot connect to " + MOBILE_IP)
    exit(-1)

arknights_click.click(arknights_constant.AK_CLICK_UI_NAME_基建)

arknights_click.click(arknights_constant.AK_CLICK_UI_NAME_返回)