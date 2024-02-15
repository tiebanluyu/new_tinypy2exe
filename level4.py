from share import *
from PyInstaller import __main__ as pyinstaller

def level4(code: str) -> None:
    """
    没有任何可压缩的地方，pyinstaller打包
    只用代码压缩
    """
    logging.info("level4")
    with open("dist/main.py", "w", encoding="utf-8") as f:  # 我也不知道，反正加入utf-8才能正常运行
        f.write(code)
    old_directory=sys.path[0]
    os.chdir(old_directory+"\\dist")
    #os.system("pyinstaller main.py")
    pyinstaller.run(["main.py"])

    # 删除文件和移动文件
    shutil.copytree("main", "../dist_temp")
    os.chdir(old_directory)
    os.system("rmdir /s /q dist")
    os.system("ren dist_temp dist ")

    os.system("rmdir /S /Q build")
    os.system("del main.spec")

