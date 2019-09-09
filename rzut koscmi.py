import random

gramy="tak"
rzut=[]
wylosowane=[]
wynik=[]
while gramy=="tak":
    for i in range(1):
        rzut.append(random.randint(1,6))
        wylosowane.append(random.randint(1,6))
    wygrane=0
    przegrane=0
    for z in rzut:
        for j in wylosowane:
            if z > j:
                
                print("Wygrales ")
            else:
                przegrane=przegrane+1
                print("Przegrales ")

    for i in rzut:
        print("Twoj rzut:"+str(i))
    for i in wylosowane:
        print("Rzut przeciwnika:"+str(i))
   
    rzut.clear()
    wylosowane.clear()
    gramy=input("Cz chcesz zagrac jeszcze raz? (tak/nie)")
