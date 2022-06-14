from random import randint
import time
def main():
    a=mondai()
    print(a)
    ans()
    hantei() 
    time_sta=time.time()
    time.sleep(1)
    time_end=time.time()
    print("タイム："+str(tim))
def mondai():
    mondai=[["サザエさんの旦那の名前は？","マスオ","ますお"],
    ["カツオの妹の名前は？","ワカメ","わかめ"],
    ["タラオはカツオから見てどんな関係","おい","甥","甥っ子","おいっこ"]]
    num=randint(0,2)
    return mondai[num][0]
def ans():
    ans=input("")
    for i in mondai[num]:
        if i==ans:
            a=True
            break
        else:
            a=False
def hantei(a):    
    if a:
        return "やるやん"
    else:
        return "誠に遺憾であります"