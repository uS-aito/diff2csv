#!/usr/local/bin/python3
#coding: utf-8

import os
import argparse

class diff2csv(object):
    def diff2csv(self,before_lines,after_lines,csv_filename):
        def break_process(tmp_minus,tmp_plus,before_buff,after_buff):
            before_buff.extend(tmp_minus)
            after_buff.extend(tmp_plus)
            count_sub = len(tmp_minus) - len(tmp_plus)

            if(count_sub > 0):
                for x in range(count_sub):
                    after_buff.append("")
            elif(count_sub < 0):
                for x in range(-count_sub):
                    before_buff.append("")
        def format_output(before_lines,after_lines):
            count_before = 0
            count_after = 0
            output_buff = ""
            
            for (bbuf,abuf) in zip(before_lines,after_lines):
                if bbuf != "":
                    count_before = count_before+1
                if abuf != "":
                    count_after = count_after+1
                output_buff = output_buff + str(count_before) + "," + bbuf.replace("\r","").replace("\n","") + "," \
                    + str(count_after) + "," + abuf.replace("\r","").replace("\n","") + os.linesep

            # デバッグ用    
            print("DEBUG: "+output_buff)
            with open("test.csv","w") as f:
                f.write(output_buff)

        is_minus_flag = 0
        before_buff = []
        after_buff = []
        tmp_minus = []
        tmp_plus = []

        result_list = self.__get_diff_str(before_lines,after_lines)
        for buf in result_list:
            # -に関する特殊処理
            if(buf[0] == "-" or is_minus_flag != 0):
                if(buf[0] == "-"):
                    is_minus_flag = 1
                if(is_minus_flag == 1):
                    if(buf[0] == "-"):
                        tmp_minus.append(buf)
                        continue
                    elif(buf[0] == "+"):
                        tmp_plus.append(buf)
                        continue
                    elif(buf[0] == " "):
                        break_process(tmp_minus,tmp_plus,before_buff,after_buff)
                if(is_minus_flag == 2):
                    if(buf[0] == "+"):
                        tmp_plus.append(buf)
                        continue
                    elif(buf[0] == "-" or buf[0] == " "):
                        break_process(tmp_minus,tmp_plus,before_buff,after_buff)
            # 通常処理
            if(buf[0] == " "):
                before_buff.append(buf)
                after_buff.append(buf)
            elif(buf[0] == "+"):
                before_buff.append("")
                after_buff.append(buf)
        
        format_output(before_buff,after_buff)
            
    def __get_diff_str(self,before_lines,after_lines):
        import difflib
        diff = difflib.Differ()
        result = diff.compare(before_lines,after_lines)
        tmp = []
        for buf in result:
            if buf[0] != "?":
                tmp.append(buf)
        return tmp[1:-1]


def main():
    text1 = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
    eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
    mauris eget magna consequat convallis. Nam sed sem vitae odio
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
    enim. Donec quis lectus a justo imperdiet tempus.
    hoge
    hoge"""
    text1_lines = text1.splitlines()

    text2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
    eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
    tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec
    mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
    hoge
    imperdiet tempus. Suspendisse eu lectus. In nunc. 
    hoge
    hoge"""
    text2_lines = text2.splitlines()
    text3 = """
    hoge
    buff
    ppp
    """
    text3_lines = text3.splitlines()
    text4 = """
    hoge
    hoge
    hoge
    ppp
    """
    text4_lines = text4.splitlines()

    # 引数解析
    parser = argparse.ArgumentParser()
    parser.add_argument("before",help="before file path")
    parser.add_argument("after",help="after file path")
    parser.add_argument("-p","--prefix",help="prefix path to before and after file",default="")
    args = parser.parse_args()

    # ファイルパス作成
    if args.prefix != "":
        if args.prefix[-1] != "/" or args.prefix[-1] != "\\":
            prefix = args.prefix + "/"
        else:
            prefix = args.prefix
        before_file_path = prefix + args.before
        after_file_path = prefix + args.after
    else:
        before_file_path = args.before
        after_file_path = args.after

    # ファイル読み込み
    with open(before_file_path,"r") as f:
        before_lines = f.read()
    before_lines = before_lines.splitlines()
    with open(after_file_path,"r") as f:
        after_lines = f.read()
    after_lines = after_lines.splitlines()

    ### DEBUG ###
    for buf in before_lines:
        print(buf)
    for buf in after_lines:
        print(buf)
    sys.exit()

    d2c = diff2csv()
    d2c.diff2csv(text1_lines,text2_lines,"hoge")

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))