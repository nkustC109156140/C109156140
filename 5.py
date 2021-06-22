m=int(input("請輸入階層值M:"))
N=0
x=1
while x<m:
    N+=1
    x*=N
print("超過M為",m,"的最小階層N值為",N)
