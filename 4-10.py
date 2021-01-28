import os.path

outfile = open("phones.txt","w")

if os.path.isfile("phones.txt"):
    
    outfile.write("홍길동 010-1424-5678")
    
    outfile.write("김철수 010-1423-5678")
    
    outfile.write("홍길술 010-1411-5678")
    
outfile.close()