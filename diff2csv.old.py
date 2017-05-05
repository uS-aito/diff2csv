#!/usr/local/bin/python3
# coding: utf-8

import difflib
import os

"""
1.diffを取る
2.解析する
3.ファイルに書き出す
"""

class diff2csv():
    import difflib
    import os
    def convert_diff_result(self,result):
        """
        1.一行読む
        　1-1.行頭が無印なら両方のバッファに保存し1へ戻る
        　1-2.行等が+または-の場合
        　　1-2-1.-のみが続く場合、oldのバッファに保存する。-が続く限り続ける。終わった後、+のバッファに同じ行数分空行を入れる
        　　1-2-2.+のみが続く場合、newのバッファに保存する。+が続く限り続ける。終わった後、-のバッファに同じ行数分空行を入れる
        　　1-2-3.-が続き、+が続く場合、まず-が続く限りoldのバッファに保存し、+が続く限りnewのバッファに保存する。その後、oldとnewの行数の差を、少ない方に空行で入れる
        　1-3.行頭が?の場合
            1-3-1.pass

        """
        tmp = []
        for buf in result:
            if buf[0] != "?":
                tmp.append(buf)
        result = tmp[:-1]
        print("DEBUG: " + str(type(result)))
        print("DEBUG: " + str(len(result)))
        print(result)

        old_buff = []
        old_count = 0
        new_buff = []
        new_count = 0
        before_char = ""
        for buf in result:
            if buf[0] == " " or buf[0] != before_char:
                count_sub = new_count - old_count
                if(count_sub > 0):  # +の行数が-の行数より多い場合=oldバッファに空行を入れる場合
                    for i in xrange(count_sub):
                        old_buff.append(os.linesep)
                elif(count_sub < 0):
                    for i in xrange(-count_sub):
                        new_buff.append(os.linesep)
                old_count = 0
                new_count = 0
                old_buff.append(buf[1:])
                new_buff.append(buf[1:])
            elif buf[0] == "-":
                old_buff.append(buf[1:])
                old_count = old_count + 1
            elif buf[0] == "+":
                new_buff.append(buf[1:])
                new_count = new_count + 1
            before_char = buf[0]

        print(len(old_buff))
        print(len(new_buff))
        for buf in old_buff:
            print buf
        for buf in new_buff:
            print buf

"直前と異なる記号だった場合 or 空白だった場合"


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
    # foo = "hoge\r\nhogehgoe".split()
    # bar = "Hofe\r\nhogehoge".split()
    # htmldiff = difflib.HtmlDiff(tabsize=4)
    # diff = htmldiff.make_table(foo,bar)
    # with open("diff_tbl.html","w") as f:
    #     f.write(diff)

    diff = difflib.Differ()
    result = diff.compare(text1_lines,text2_lines)
    for buf in result:
        if buf[0] != "?":
            print(buf)

    result = diff.compare(text1_lines,text2_lines)
    d2c = diff2csv()
    d2c.convert_diff_result(result)

    # diff = difflib.unified_diff(text1_lines,text2_lines)
    # print(os.linesep.join(list(diff)))
    # for buf in diff:
    #     print(buf)
    #     break


if __name__ == '__main__':
    main()