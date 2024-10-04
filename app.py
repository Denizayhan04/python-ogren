""" print("asd")
print(123)

isim = "asd"
isim2= 123
print(isim , isim2)
print(30%12)
print(2*2)
print(2**3)
print(40/6)
print(40//6)
print(round(40/6))

isimstring = "birikiüc"
print(isimstring[0:4])
print(isimstring[0:4:1])
print(isimstring[0:4:2])
print("tr \" asd"f)
print("tr \nasd")
print("trasd" * 3 )
print("trasd".upper())
print("trASD".lower())
print("asdasdasd".count("a"))
print("asdasdasdaaaaa".count("a"))
print("asdasdasdaaaaasa".find("sa"))
print("aahaa".index("h"))

degisken1 = "           aaa        "
print(degisken1.lstrip())
print(degisken1.rstrip())
print(degisken1.replace("aaa","bbb"))

print("Ben {} digeri {}".format("1","2")) """
""" array """

""" insan = ["a","b",23,"asd"]
print(insan)
print(insan[0:4])
insan[0] = "degisen"
print(insan)
insan[2] = [1,2,3]
print(insan, "\n" , insan[2][2])
print(len(insan))
print(insan[-1])
insan.append("yeni")
insan.pop()
insan.pop(1)
yenii = insan.copy()
print(yenii)

a=[1,2,3]
b=[4,5,6]
print(a+b)

a.extend(b)
print(a)


b.insert(1,"asd")
print("bura",
      b)
print(insan) """


""" kimlik = {
    "isim":"ali",
    "soyisim":"Veli",
    "tc":15163534531
}
print(kimlik.items())
print(kimlik.get("isim"))
print(kimlik.update({"isim":"yok"}))
print(kimlik)
 """
""" dizi = [1,2,3,4]
print(2 in dizi)
print(8 in dizi)
print(8  not in dizi)
sifre = input("sifre gir:\n")
print("sifren {}".format(sifre))

if True:
    pass """

"""x = 0

while x<21:
    x+=1
    if x == 16:
      continue
    print(x)"""

"""x=[1,2,3,4,5,6,7,8,9]


for sayi in x:
    print(sayi)"""
"""
def alan (r,pi):
    return(r*r*pi)


print(alan(2,3.14))"""

""" print("123","456",sep="/",end="?") """

def kimlik(isim,soyisim,yas,tc):
    print("isim :{} , soyisim :{} , yaş :{} , tckno :{}".format(isim,soyisim,yas,tc))

def kimlik2(isim="Boş",soyisim="Boş",yas="Boş",tc="Boş"):
    print("isim :{} , soyisim :{} , yaş :{} , tckno :{}".format(isim,soyisim,yas,tc))

kimlik("ali","keser",25,19127754288)
kimlik2("ali","keser",25)
kimlik2(soyisim="keser",tc=25)