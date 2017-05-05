#coding: utf-8

# hoge = []

# def test(foo):
#     foo = foo + ["func_test"]

# hoge.append("foo")
# print(hoge)
# test(hoge)
# print(hoge)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("before",help="before file path")
parser.add_argument("after",help="after file path")
parser.add_argument("-p","--prefix",help="prefix path to before and after file",default="")
args = parser.parse_args()
print("before: "+args.before)
print("after: "+args.after)
print("prefix: "+args.prefix)