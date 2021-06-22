a=input("輸入一整數序列為: ").split()
b=set(a)
if len(b) > (len(a)+1)//2:
    print("NO")
else: 
    while len(a) > 1: 
        for i in list(set(a)): a.remove(i)
    print(a[0])
