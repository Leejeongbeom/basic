year=int(input("연도를 입력하시오."))
a=year%4
b=year%100
c=year%400

if a==0:
    if (b==0) and (c==0):
        print("%s년은 윤년입니다" %year)
    else:
        print("%s년은 윤년입니다" %year))
else:
    print("윤년이 아닙니다.")