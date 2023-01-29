from math import *
from random import *

#0

#while True:
#    try:
#        print("Tere tulemast! See on EhoSushi")
#        print("Me võime pakkuda mitut sorti sushit.")
#        print()
#        print("Mida te soovite?")
#        print()
#        Philadelphia_Classic=int(input("Philadelphia Classic (Tellite-1 või Ei telli-0): "))
#        Lumekrabi_tempura=int(input("Lumekrabi tempura (Tellite-1 või Ei telli-0):"))
#        New_Azuma=int(input("New Azuma (Tellite-1 või Ei telli-0):"))
#        Alaska=int(input("Alaska (Tellite-1 või Ei telli-0):"))
        
#        if Philadelphia_Classic==1 and Lumekrabi_tempura==0 and New_Azuma==0 and Alaska==0:
#            Philadelphia_Classic=11,90        
#            Lumekrabi_tempura=0             
#            New_Azuma=0         
#            Alaska=0          
#            q=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",q )

#        elif Philadelphia_Classic==0 and Lumekrabi_tempura==1 and New_Azuma==0 and Alaska==0:
#            Philadelphia_Classic=0        
#            Lumekrabi_tempura=11,50         
#            New_Azuma=0         
#            Alaska=0          
#            w=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",w )

#        elif Philadelphia_Classic==0 and Lumekrabi_tempura==0 and New_Azuma==1 and Alaska==0:
#            Philadelphia_Classic=0        
#            Lumekrabi_tempura=0             
#            New_Azuma=13,50     
#            Alaska=0          
#            e=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",e )

#        elif Philadelphia_Classic==0 and Lumekrabi_tempura==0 and New_Azuma==0 and Alaska==1:
#            Philadelphia_Classic=0        
#            Lumekrabi_tempura=0             
#            New_Azuma=0        
#            Alaska=9,90          
#            r=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",r )

#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==1 and New_Azuma==0 and Alaska==0:
#            Philadelphia_Classic=11,90       
#            Lumekrabi_tempura=11,50         
#            New_Azuma=0         
#            Alaska=0          
#            t=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",t )
         
#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==0 and New_Azuma==1 and Alaska==0:
#            Philadelphia_Classic=11,90        
#            Lumekrabi_tempura=0            
#            New_Azuma=13,50         
#            Alaska=0          
#            y=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",y )

#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==0 and New_Azuma==0 and Alaska==1:
#            Philadelphia_Classic=11,90       
#            Lumekrabi_tempura=0        
#            New_Azuma=0         
#            Alaska=9,90          
#            u=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",u )

#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==1 and New_Azuma==1 and Alaska==0:
#            Philadelphia_Classic=11,90       
#            Lumekrabi_tempura=11,50         
#            New_Azuma=13,50     
#            Alaska=0          
#            i=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",i )

#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==1 and New_Azuma==1 and Alaska==1:
#            Philadelphia_Classic=11,90       
#            Lumekrabi_tempura=11,50         
#            New_Azuma=13,50     
#            Alaska=9,90          
#            a=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",a )

#        elif Philadelphia_Classic==0 and Lumekrabi_tempura==1 and New_Azuma==1 and Alaska==0:
#            Philadelphia_Classic=0      
#            Lumekrabi_tempura=11,50         
#            New_Azuma=13,50     
#            Alaska=0          
#            s=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",s )

#        elif Philadelphia_Classic==0 and Lumekrabi_tempura==1 and New_Azuma==0 and Alaska==1:
#            Philadelphia_Classic=11,90       
#            Lumekrabi_tempura=11,50         
#            New_Azuma=0         
#            Alaska=9,90          
#            d=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",d )

#        elif Philadelphia_Classic==0 and Lumekrabi_tempura==1 and New_Azuma==1 and Alaska==0:
#            Philadelphia_Classic=0      
#            Lumekrabi_tempura=11,50         
#            New_Azuma=13,50     
#            Alaska=0          
#            s=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa:",s )    

#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==0 and New_Azuma==1 and Alaska==1:
#            Philadelphia_Classic=11,90      
#            Lumekrabi_tempura=0         
#            New_Azuma=13,50     
#            Alaska=9,90          
#            g=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa: ",g )

#        elif Philadelphia_Classic==1 and Lumekrabi_tempura==1 and New_Azuma==0 and Alaska==1:
#            Philadelphia_Classic=11,90      
#            Lumekrabi_tempura=11,50         
#            New_Azuma=0    
#            Alaska=9,90          
#            m=Philadelphia_Classic+Lumekrabi_tempura+New_Azuma+Alaska
#            print("Tellimuse summa: ",m )

#        if Philadelphia_Classic==0 and Lumekrabi_tempura==0 and New_Azuma==0 and Alaska==0: 
#            print("Te ei tellinud midagi. ")   
#        print()
#        c=input("Kuidas soovite tasuda sularahas või kaardiga: ")
#        if c.lower()=="sularaha":
#            print("Anna raha")

#        if c.lower()=="kaardiga":
#            n=int(input("Sisestaga kaardi number: "))
#            print(n,"Selle kaardiga on tehtud maksa ")
            
#    except:    
#         print("")




snäkid = ["Kartulikrõpsud", "Šokolaadikommid", "Närimiskumm", "Küpsised"]
hind = [1.50, 0.75, 0.50, 1.00]

kokku = 0

while True:
    print("Tere tulemast see snäk masin")
    print("Palun valige snack:")
    for i, snäk in enumerate(snäkid):
        print(f"{i + 1}: {snäk} - €{hind[i]}")
    valik = int(input("Sisesta oma valik (1-4): "))
    if valik == 0:
        break
    if valik > 0 and valik <= len(snäkid):
        snäk = snäkid[valik - 1]
        kulud = hind[valik - 1]
        kokku += kulud
        print(f"Naudi oma {snäk}! Teie kogusumma on €{kokku}")
    else:
        print("Vigane valik. Proovi uuesti.")
    break




#20 1 valik

#print("Sa pead sisestama 4 numbrit ja neist programm valib kõige suurema ja kõige väiksema")
#num1 = float(input("Sisesta esimene number: "))
#num2 = float(input("Sisesta teine number: "))
#num3 = float(input("Sisesta kolmas number: "))
#num4 = float(input("Sisesta neljas number: "))

#nums = [num1, num2, num3, num4]

#print("Kõige rohkem on: ", max(nums))
#print("Väikseim arv on: ", min(nums))




#20


#numbers = []

#for i in range(4):
#    num = int(input("Sisesta number {}: ".format(i + 1)))
#    numbers.append(num)

#print("Kõige rohkem on: ", max(numbers))
#print()
#print("Väikseim arv on: ", min(numbers))

#20 2


#while True:
#  numbers = []
#  print("Sisesta number:")
#  for i in range(4):
#    number = int(input())
#    numbers.append(number)

#  rohkem = max(numbers)
#  väiksem = min(numbers)
#  print("Kõige rohkem on: ", rohkem)
#  print("Väikseim arv on: ", väiksem)
#  break
