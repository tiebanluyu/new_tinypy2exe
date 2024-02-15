from share import *


def level1(code: str):
    """
    对于只有一个helloworld的程序，可以直接搬运现有程序
    已经用c语言写好，远小于python版的
    """
    logging.info("level1")

    src = "helloworld.exe"
    shutil.copy2(src, "dist/main.exe")
