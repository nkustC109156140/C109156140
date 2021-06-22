a=int(input("輸入第一行正整數為: "))
b=input("第二行中數列中的數字為:").split()
if len(set(b)) == a: 
    print("每個數字剛好只出現1次")
else:
    i=1
    while True:
        for j in list(set(b)): b.remove(j)
        i+=1
        if len(b) == 1: 
            print("最大出現次數的數字為:"+b[0])
            print("出現次數為:"+str(i))
            break
