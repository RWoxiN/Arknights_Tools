import time

from Base.mobile import *
from discern import *

class arknights_constant:
    AK_CLICK_UI_NAME_返回 = "return"
    AK_CLICK_UI_NAME_仓库 = "storehouse"
    AK_CLICK_UI_NAME_终端 = "terminal"
    AK_CLICK_UI_NAME_基建 = "base"

class arknights_click:
    SCREEN_FILENAME = os.path.split(os.path.realpath(__file__))[0] + "/images/screen.png"

    def click(ui_name):
        adb.screen_shot(arknights_click.SCREEN_FILENAME)
        click_loc = discern.find_ui(ui_name)
        adb.click(click_loc)
        time.sleep(3)
