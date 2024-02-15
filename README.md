# tinypy2exe
## 功能
这个软件可以获得空间更加小的pyinstaller包
## 如何使用
python main.py (your-python-file) [name]
比如：
看到test开头的文件了吗    
python main.py test1.py file  
然后程序就会调用pyinstaller，获得可执行程序，
放在file目录下  
删去不必要的东西（level3）  
如果可行，使用c语言进行重写程序，在这种情况下  
程序会很小，不到正常python包的10%（level1和level2）  

## 和pyinstaller的关系
本程序由pyinstaller作为核心，
自己不提供打包方式，
更不能替代pyinstaller。

## 怎么运作的
先删去注释
再分析文章内容
如果就是helloworld那就使用现成的
如果没有import那就删除所有库
否则正常打包

