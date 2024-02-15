from level1 import level1
from level2 import level2
from level3 import level3
from level4 import level4
from share import *

# 导入
logging.basicConfig(level=20)


if __name__ == "__main__":

    path: str = sys.argv[1]  # 第一个参数是目标文件的地址
    try:
        des = sys.argv[2]  # 第二个参数是打包后的文件的地址，默认为dist
    except:  # 为了可维护性，打包时统一用dist，完成后再将其移动到目标位置
        des = "dist"
    path=os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as file:
        code = file.read()
        code = remove_comments(code)
    # 删除文件夹，再次创建
    
    os.system("rmdir /s /q dist_temp")    
    os.system("rmdir /s /q dist")
    logging.warning("Rebuild dist")
    os.system("md dist")

    if "import" in code:
        level4(code)
    else:
        if code == 'print("helloworld")' or code == 'print("helloworld")\n':
            level1(code)
        elif ("input" in code) or ("open" in code):
            level3(code)
        else:  # level2
            level2(code)
    logging.info("Build done")
    if des != "dist":
        shutil.move("dist", des)
        logging.info("File move successfully")
    logging.info("Build successfully")

