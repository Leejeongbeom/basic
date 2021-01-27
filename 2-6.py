str=input("문자열을 입력하세요: ")
length = len(str)

if length%2 == 1:
    print("중앙 글자는",str[length//2])
else:
    print("중앙 글자는",str[length//2],str[(length//2)-1])