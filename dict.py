#! /usr/local/bin/python3

d = {'jcw':26, 'jxr': 10, 'yyr': 10}

print('d["jcw"]:', d["jcw"])

print('d["yyr"]:', d.get("yyr"))

d.pop("yyr")

#print('d["yyr"]:', d["yyr"])

print('d["yyr"]:', d.get("yyr"))
