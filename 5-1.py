infile = open("sales.txt","r")
outfile = open("summary.txt","w")

sum = 0
count = 0

for line in infile:
    totalmoney = int(line)
    sum = sum + totalmoney
    count = count + 1

outfile.write("총매출 ="+ str(sum)+"\n")

outfile.write("평균 일매출 ="+ str(sum/count))

infile.close()
outfile.close()