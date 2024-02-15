"""
只干一件事，从网络上下载upx，并将其安装到path下
"""
import os
 # 获取所有环境变量
env_vars = os.environ
 # 获取特定环境变量的值
path_value = env_vars.get('PATH')
 # 打印环境变量的值
#print(path_value)
path_list = path_value.split(";")
for path in path_list:
    if os.path.exists(os.path.join(path, "upx.exe")):
        exit()
#print(path_list[-1])
import urllib.request
url = "https://tiebanluyu.github.io/download/upx.exe"
urllib.request.urlretrieve(url, path_list[-1]+"upx.exe")