print("*** M�NGUD ARVETEGA ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = (abs(int(input("Sisesta t�isarv  =>" ))))
        break
    except ValueError:
         print("See pole t�isarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga pole m�tet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("M��rake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:
            if b % 2 == 0:
                    paaris =+ 1
            else:
                    paaritu =+ 1
            b = b // 10
    
    print("Numbrite arv:", paaris)
    print("Paaritu arv:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*P��rake �mber* sisestatud arv")
    print()
    b=0
    while a > 0:
        number == a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*P��ratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse h�poteesi")
    print()
    if c % 2 == 0:
        print("c - paarisarv. Jagame 2.")
    else:
        print("c - paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")
    while c != 1:
            if c % 2 == 0:
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(c, end="  ")
    print()
    print("H�potees on �ige")
