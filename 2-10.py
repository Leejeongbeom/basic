from random import randint

a=input("안내면 진다 가위 바위 보: ")
number=randint(0,2)
if number == 0:
    computer = '가위'
elif number == 1:
    computer = '바위'
else:
    computer = '보'

print("나는:",a, "컴퓨터:",computer)
if (a==computer):
    print("비겼습니다.")
elif (a=='가위') and (computer =='바위'):
    print(" 졌습니다.")
elif (a=='가위') and (computer =='보'):
    print(" 이겼습니다.")
elif (a=='바위') and (computer =='보'):
    print(" 졌습니다.")
elif (a=='바위') and (computer =='가위'):
    print(" 이겼습니다.")
elif (a=='보') and (computer =='가위'):
    print(" 졌습니다.")
elif (a=='보') and (computer =='바위'):
    print(" 이겼습니다.")