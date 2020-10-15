try:
    age=int(input("Mata in sin ålder : "))
    if 0<age<18 :
        print ("Du är ej myndig")
    elif 18<=age<65 :
        print ("Du är myndig men inte pensionär")
    elif age>65 :
        print ("Du är pensionär")
    else :
        print ("Du har matat in en felaktig ålder")
except Exception :
    print ("Du har matat in en felaktig ålder")
