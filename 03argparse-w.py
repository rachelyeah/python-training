#!/usr/bin/env python
import argparse
import os
import time

def list_files():
    for file in os.listdir('.'):
        if not file.startswith('.'):
            print(file.ljust(20), end=' ')


def list_all_files():
    for file in os.listdir('.'):
        print(file.ljust(20), end=' ')


def list_files_in_columns():
    for file in os.listdir('.'):
        if not file.startswith('.'):
            file2 = os.path.abspath(os.path.join('.', file))
            if os.path.isdir(file2):
                one = 'd'
            else:
                one = '-'
            two = time.strftime("%m %d %M：%S", time.gmtime(os.stat(file2).st_mtime))

            print(one, os.stat(file2).st_mode, os.stat(file2).st_nlink, os.stat(file2).st_uid, os.stat(file2).st_gid,
                  os.stat(file2).st_size, two, file)
        else:
            pass

def list_all_files_in_columns():
    for file in os.listdir('.'):
        file2 = os.path.abspath(os.path.join('.', file))
        if os.path.isdir(file2):
            one = 'd'
        else:
            one = '-'

        two = time.strftime("%m %d %M：%S", time.gmtime(os.stat(file2).st_mtime))

        print(one, os.stat(file2).st_mode, os.stat(file2).st_nlink, os.stat(file2).st_uid, os.stat(file2).st_gid,
              os.stat(file2).st_size, two, file)


parser = argparse.ArgumentParser(prog='rabbit')
parser.add_argument('-a', action='store_true')
parser.add_argument('-l', action='store_true')
args = parser.parse_args()

if args.a == True and args.l ==False:
    list_all_files()
elif args.a == False and args.l == False:
    list_files()
elif args.a == False and args.l == True:
    list_files_in_columns()
else:
    list_all_files_in_columns()