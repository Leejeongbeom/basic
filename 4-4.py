friends = ['홍길동','김수현','이순신','박순애']
menu = ['1.친구리스트 출력\n','2.친구추가\n','3.친구삭제\n','4.이름변경\n','5.이름순 정렬\n','9.종료\n']
menun = 0
while menun != 9:
   menun = int(input("메뉴를 선택하시오: "))
   if menun == 1:
       print(friends)
   elif menun == 2:
       name = input("이름을 입력하시오: ")
       friends.append(name)
   elif menun == 3:
       name2 = input("이름을 입력하시오: ")
       friends.remove(name2)
   elif menun == 4:
       name2 = input("이름을 입력하시오: ")
       chname = input("변경할 이름을 입력하시오.:")
       index = friends.index(name2)
       friends[index] = chname
   elif menun == 5:
       b=sorted(friends)
       print(b)
   else:
       print("다시 입력하시오.")
print("종료합니다.")