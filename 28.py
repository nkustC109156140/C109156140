ans=list("1234")
user=list(input(""))
a=0
b=0
for i in range(4):
    if (ans[i]==user[i]):
        a=a+1
    else:
        b=b+1
print(a,"A",b,"B")