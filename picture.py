# 如何使用这个文件
# 设置虚拟环境：
# sudo pacman -S python-virtualenv
# python -m  virtualenv myenv
# 进入虚拟环境
# source myenv/bin/activate
# python picture.py
# 退出虚拟环境
# deactivate

# 需要使用到的包：
# pip install pillow-avif-plugin
# pip install Pillow

TARGET_PATH = 'ChangePools'

from PIL import Image
import pillow_avif

import os
def func_FilePaser_V2(filepath):
    # TODO: edit to open md? files from file system.
    for filepathe, dirs, fs in os.walk(filepath):
        for f in fs:
            # print(os.path.join(filepathe, f))
            # print(f)

            filepath_temp = os.path.join(filepathe, f)

            imgss = Image.open(filepath_temp)
            imgss.save(filepath_temp + '.AVIF','AVIF')
            os.remove(filepath_temp)
            ...

func_FilePaser_V2(TARGET_PATH)
