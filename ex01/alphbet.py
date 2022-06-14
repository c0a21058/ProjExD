from random import randint
from this import d
from turtle import Turtle
m=10
kieru=2
count=0
def mozi():
    global m
    mozis=""
    mozis2=""
    for i in range(m):
        num=randint(65,90)
        mozis+=(chr(num)+" ")
        mozis2+=chr(num)
    return mozis,mozis2
def dele(a,b):
    global kieru,m
    kietamozi=[]
    x=[i for i in b]
    for j in range(kieru):
        s=randint(0,m-1)
        m=m-1
        kietamozi.append(x.pop(s))
    return kietamozi ,x
def ans(a,b):
    global count
    c=0
    q=1
    ans_num=input("欠損文字はいくつあるでしょうか？:")
    if ans_num ==kieru:
        q+=1
    for i in range(kieru):
        ans_mozi=input(f"{i+1}文字目を入力してください。")
        for i in a:
            if ans_mozi==i:
                c+=1
    if c+q==kieru+1:
        print("正解")
        return 1
    else:
        print("不正解もう一度")
        count+=1
        return 0
while True:
    mozi=mozi()
    print(mozi[0])
    d=dele(mozi[0],mozi[1])
    print(d[1])
    a=ans(d[0],d[1])
    if a==1 or count>4:
        break
