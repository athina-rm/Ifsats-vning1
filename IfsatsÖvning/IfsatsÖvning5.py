person = input("Vilken kategori Vuxen/Pensionär/Student ? Mata in V/P/S : ")
if person=="V" :
    print ("Resan kostar 30kr")
elif person=="P" or person == "S" :
    print ("Resan kostar 20kr")
else :
    print ("Du har angett en felaktig kategori")
