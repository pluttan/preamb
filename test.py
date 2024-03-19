from time import time
from urllib.parse import quote
import requests
from sys import argv
from PyPDF2 import PdfReader


def decrypt():
    res = ""
    for i in str(round(time())):
        res += chr(ord('A') + int(i))
    return res


a = argv[1].replace('"', '').replace("'", '"')

resp = int(str(requests.get(f'http://95.163.235.193:5050/?c=1&key={decrypt()}&path={quote(a)}')).replace("<Response [", "")
           .replace("]>", ""))
if resp == 418:
    f = open(a.replace(".tex", ".log"))
    er = f.read()
    io = er.index("\nl.") + 1
    while er[io] != "\n":
        io += 1
    io += 1
    while er[io] != "\n":
        io += 1
    print(er[:io])
else:
    p = '"'
    print(
        f"Compiled! ({str(len(PdfReader(a.replace('.tex', '.pdf').replace(p,'')).pages))} pages)", end="")
