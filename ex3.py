import re

def replace(txt):
    x=re.sub(r"\s","-", txt)
    return  x


txt=str(input("write a txt: "))
x=replace(txt)
print(x)