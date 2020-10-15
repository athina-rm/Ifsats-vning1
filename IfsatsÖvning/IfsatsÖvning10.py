money=int(input("Hur mycket pengar har du?"))
rabatt = input("Har du rabatt (J/N) : ")
if 15<=money<=25 :
    if rabatt=="N" :
        print ("Du kan köpa en liten hamburgare")
    elif rabatt=="J" :
        print ("Du kan köpa en liten hamburgare och en pommes frites")
elif 25<money<=50 :
    if rabatt=="N" :
        print ("Du kan köpa en stor hamburgare")
    elif rabatt=="J" :
        print ("Du kan köpa en stor hamburgare och en pommes frites")
elif money>60 or (50<money<=60 and rabatt=="J") :
    print ("Du kan köpa ett meal med dryck")