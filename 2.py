i=int(input("請輸入電費"))
summer=0
nosummer=0
Degree=0
if i>700:
    Degree=i-701
    summer+=Degree*5.63
    nosummer+=Degree*4.50
    i=700
if i>500 and i<701:
    Degree=i-500
    summer+=Degree*4.97
    nosummer+=Degree*4.01
    i=500
if i>330 and i<501:
    Degree=i-330
    summer+=Degree*4.39
    nosummer+=Degree*3.61
    i=330
if i>120 and i<331:
    Degree=i-120
    summer+=Degree*3.02
    nosummer+=Degree*2.68
    i=120
if i<121:
    summer+=i*2.10
    nosummer+=i*2.10
print('Summer month:'+str(summer))
print('noSummer month:'+str(nosummer))
