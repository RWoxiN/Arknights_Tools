import os
import cv2
import numpy
from matplotlib import pyplot

class discern:

    IMG_DIR = os.path.split(os.path.realpath(__file__))[0] + "/images/"
    IMG_SCREEN_FILENAME = IMG_DIR + "screen.png"
    TEMPLATE_DIR = IMG_DIR + "template/"
    TEMPLATE_UI_DIR = TEMPLATE_DIR + "ui/"

    UI_TEMPLATE_METHOD = {
        "return": cv2.TM_CCOEFF_NORMED,
        "storehouse": cv2.TM_CCOEFF_NORMED,
        "base": cv2.TM_CCOEFF_NORMED,
    }

    def find_ui(ui_name):
        screen = cv2.imread(discern.IMG_SCREEN_FILENAME, 0)
        template = cv2.imread(discern.TEMPLATE_UI_DIR + ui_name + ".png", 0)
        h, w = template.shape[:2]

        res = cv2.matchTemplate(screen, template, discern.UI_TEMPLATE_METHOD[ui_name])
        # res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if discern.UI_TEMPLATE_METHOD[ui_name] in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            click = [min_loc[0] + w/2, min_loc[1] + h/2]
        else:
            click = [max_loc[0] + w/2, max_loc[1] + h/2]
        # click = [max_loc[0] + w/2, max_loc[1] + h/2]
        return click

    # def test_find_ui(ui_name):
    #     screen = cv2.imread(discern.IMG_SCREEN_FILENAME, 0)
    #     template = cv2.imread(discern.TEMPLATE_UI_DIR + ui_name + ".png", 0)
    #     h, w = template.shape[:2]

    #     methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #     'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    #     for meth in methods:
    #         img2 = screen.copy()

    #         # 匹配方法的真值
    #         method = eval(meth)
    #         res = cv2.matchTemplate(screen, template, method)
    #         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    #         # 如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED，取最小值
    #         if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #             top_left = min_loc
    #         else:
    #             top_left = max_loc
    #         bottom_right = (top_left[0] + w, top_left[1] + h)

    #         # 画矩形
    #         cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    #         pyplot.subplot(121), pyplot.imshow(res, cmap='gray')
    #         pyplot.xticks([]), pyplot.yticks([])  # 隐藏坐标轴
    #         pyplot.subplot(122), pyplot.imshow(img2, cmap='gray')
    #         pyplot.xticks([]), pyplot.yticks([])
    #         pyplot.suptitle(meth)
    #         pyplot.show()

    def find_resource(resource_name):
        