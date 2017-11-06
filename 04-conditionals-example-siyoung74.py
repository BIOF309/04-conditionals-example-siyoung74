# 04-conditionals-example-siyoung74
seq=input("input your seq ")
total=len(seq)
g=seq.count("g")
c=seq.count("c")
percent=(g+c)/total*100
if percent <50:
    print ("GC content is less than 50%", "total GC is", percent, "%")
elif percent > 70:
    print ("GC content is more than 70%", "total GC is", percent, "%")
else:
    print ("GC content is between 50-70%", "total GC is", percent, "%")
