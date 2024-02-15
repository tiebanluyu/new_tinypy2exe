from share import *


def level2(code: str) -> None:
    """
    很多程序有循环，分支，类。
    但是没有input open等函数
    一开始就确定了输出，可简化

    """
    logging.info("level2")
    text = execute_code(code)
    lines = text.split("\n")
    prefixed_lines = ["echo " + line for line in lines]
    text = "@echo off\n" + "\n".join(prefixed_lines)[0:-5]  # 前面加echo off 删去最后面的echo
    with open("dist/main.bat", "w+") as file:
        file.write(text)
    src = "lv2.exe"
    shutil.copy2(src, "dist/main.exe")


def execute_code(code: str) -> str:
    """
    试运行目标程序，将输出返回
    """

    # 创建一个类用于收集输出
    class StringIO:  # chatgpt告诉我用第三方库，但用不了，我便自己写一个，可行
        def __init__(self):
            self.text = ""

        def write(self, text):
            # 确实在exec中调用了这个函数
            self.text = self.text + text

        def getvalue(self):
            return self.text

        def close(self):
            pass

    # 试运行待打包程序，将输出收集到text中
    output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = output
    exec(code)
    text = output.getvalue()
    sys.stdout = old_stdout
    output.close()

    return text
