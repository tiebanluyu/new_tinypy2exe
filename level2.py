from share import *

b64_of_launch="""
-----BEGIN CERTIFICATE-----
TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAgAAAAA4fug4AtAnNIbgBTM0hVGhpcyBwcm9ncmFtIGNhbm5v
dCBiZSBydW4gaW4gRE9TIG1vZGUuDQ0KJAAAAAAAAABQRQAATAECAAAAAAAAAAAA
AAAAAOAADwMLAQYAAAAAAAAAAAAAAAAAQBAAAAAQAAAAIAAAAABAAAAQAAAAAgAA
BAAAAAAAAAAEAAAAAAAAAAAwAAAAAgAAAAAAAAMAAAAAABAAABAAAAAAEAAAEAAA
AAAAABAAAAAAAAAAAAAAACAgAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAABIIAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC50ZXh0AAAA
4AAAAAAQAAAAAgAAAAIAAAAAAAAAAAAAAAAAACAAAGAuZGF0YQAAANAAAAAAIAAA
AAIAAAAEAAAAAAAAAAAAAAAAAABAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVieWB7AAAAACQuAAgQABQ
6KMAAACDxAS4AQAAAOkAAAAAycMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
VYnlgewUAAAAkLgAAAAAiUXsuAAAAwBQuAAAAQBQ6F0AAACDxAi4AQAAAFDoVwAA
AIPEBI1F7FC4AAAAAFCNRfRQjUX4UI1F/FDoQQAAAIPEFItF9FCLRfhQi0X8UOhd
////g8QMiUXwi0XwUOgmAAAAg8QEycMA/yVIIEAAAAD/JUwgQAAAAP8lUCBAAAAA
/yVUIEAAAAD/JVggQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAHN0YXJ0IC93YWl0IC9iIG1haW4uYmF0AAAAAAAAAAAA
YCAAAAAAAAAAAAAAeCAAAEggAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIMgAACMIAAA
mSAAAKogAAC6IAAAAAAAAIMgAACMIAAAmSAAAKogAAC6IAAAAAAAAG1zdmNydC5k
bGwAAABzeXN0ZW0AAABfY29udHJvbGZwAAAAX19zZXRfYXBwX3R5cGUAAABfX2dl
dG1haW5hcmdzAAAAZXhpdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
-----END CERTIFICATE-----
"""
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
    with open("dist/main.txt","w") as f:
        f.write(b64_of_launch)
    #breakpoint()    
    os.system("certutil -f -decode dist/main.txt dist/main.exe ")
    os.system("del /S main.txt")


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
