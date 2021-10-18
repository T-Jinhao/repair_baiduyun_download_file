#!/usr/bin/python3
# -*- encoding:utf8 -*-

import os
import sys
import re

def replace_suffix(dirpath, match_suffix='.baiduyun.p.downloading', replace_suffix=''):
    g = os.walk(dirpath)
    for path,dir_list,file_list in g:
        for file_name in file_list:
            if re.search(match_suffix, file_name):
                match_file = os.path.join(path, file_name)
                new_filename = match_file.replace(match_suffix, replace_suffix)
                if os.path.exists(new_filename):
                    os.remove(new_filename)   # 删除空白文件
                os.rename(match_file, new_filename)
                print(match_file + ' ==> ' + new_filename)

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        replace_suffix(path)
    except:
        print('usage: python3 run.py dir_path')
