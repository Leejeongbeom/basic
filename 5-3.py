filename = input("파일 이름을 입력하시오: ")
infile = open(filename)
spaces = 0
tabs = 0
for line in infile:
    spaces = spaces + line.count(' ')
    tabs = tabs + line.count('\t')
infile.close()

print("스페이스 수 = %d, 탭의 수 = %d"%(spaces,tabs))