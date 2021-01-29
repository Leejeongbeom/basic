na1 = input("원본파일")
na2 = input("복사파일")

infile = open(na1,"rb")
outfile = open(na2,"wb")

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)
    
infile.close()
outfile.close()
print(na1+"를"+na2+"로 복사하였습니다.")