from random import randrange
level=input("Tapez le niveau que vous souhaitez (facile/moyen/difficile) : ")
nb1=0
nb2=0
nb3=0
score=0

if level=="facile":
    for i in range (4) :
        nb1=randrange(1,9)
        nb2=randrange(1,9)
        print("Combien font ",nb1, "+", nb2, "? ")
        qst=int(input(" "))
        
        if qst==(nb1+nb2):
            score=score+1
            
    for i in range (3) :
        nb1=randrange(1,9)
        nb2=randrange(1,9)
        print("Combien font ",nb1, "-", nb2, "? ")
        qst=int(input(" "))
        
        if qst==(nb1-nb2):
            score=score+1
            
    for i in range (3) :
        nb1=randrange(1,9)
        nb2=randrange(1,9)
        print("Combien font ",nb1, "x", nb2, "? ")
        qst=int(input(" "))
        
        if qst==(nb1*nb2):
            score=score+1

if level=="moyen":
    for i in range (3) :
        nb1=randrange(1,19)
        nb2=randrange(1,19)
        print("Combien font ",nb1, "+", nb2, "? ")
        qst=int(input(" "))
       
        if qst==(nb1+nb2):
            score=score+1
            
    for i in range (4) :
        nb1=randrange(1,19)
        nb2=randrange(1,19)
        print("Combien font ",nb1, "-", nb2, "? ")
        qst=int(input(" "))
        
        if qst==(nb1-nb2):
            score=score+1
            
    for i in range (3) :
        nb1=randrange(1,19)
        nb2=randrange(1,19)
        print("Combien font ",nb1, "x", nb2, "? ")
        qst=int(input(" "))
        
        if qst==(nb1*nb2):
            score=score+1

if level=="difficile":
    for i in range (3) :
        nb1=randrange(1,19)
        nb2=randrange(1,19)
        nb3=randrange(1,9)
        print("Combien font ",nb1, "+", nb2, "+" ,nb3, "? ")
        qst=int(input(" "))
        
        if qst==(nb1+nb2+nb3):
            score=score+1
            
    for i in range (3) :
        nb1=randrange(1,19)
        nb2=randrange(1,19)
        nb3=randrange(1,9)
        print("Combien font ",nb1, "-", nb2, "-" ,nb3, "? ")
        qst=int(input(" "))
        
        if qst==(nb1-nb2-nb3):
            score=score+1
            
    for i in range (4) :
        nb1=randrange(1,19)
        nb2=randrange(1,19)
        nb3=randrange(1,9)
        print("Combien font ",nb1, "x", nb2, "x" ,nb3, "? ")
        qst=int(input(" "))
        
        if qst==(nb1*nb2*nb3):
            score=score+1
    
print("Votre score est de", score, "sur 10",".")
