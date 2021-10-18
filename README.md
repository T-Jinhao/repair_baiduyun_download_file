### 功能
使用百度云盘下载项目时，会出现`.baiduyun.p.downloading`文件，即出现`test.exe`及`test.exe.baiduyun.p.downloading`两个文件，前者为空，后者才为实际文件，需要手动更改后缀名。  
本脚本代替此繁琐操作，能遍历文件夹中的该类文件并修复。  

使用方法：  
`python3 run.py 目标文件夹`