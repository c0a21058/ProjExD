from random import randint
import time
time_sta=time.time()
time.sleep(1)
time_end=time.time()
a=True
mondai=[["サザエさんの旦那の名前は？","マスオ","ますお"],
["カツオの妹の名前は？","ワカメ","わかめ"],
["タラオはカツオから見てどんな関係","おい","甥","甥っ子","おいっこ"]]
num=randint(0,2)
print(mondai[num][0])
ans=input("")
for i in mondai[num]:
    if i==ans:
        a=True
        break
    else:
        a=False
if a:
    print("やるやん")

else:
    print("誠に遺憾であります")
time.sleep(1)
time_end=time.time()
tim=time_end-time_sta
print("タイム："+str(tim))