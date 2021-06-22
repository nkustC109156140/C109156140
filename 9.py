str1=input("輸入s1為:")
str2=input("輸入s2為:")
if len(str2.replace(str1, ""))!=len(str2):
    print("YES")
else:
    print("NO")