m=int(input("Mata in antal minuter : "))
if m<60 :
    print (f"Det är {m} minuter")
elif 60<=m<(24*60) :
    print (f"Det är {int(m/60)} timmar och {m%60} minuter")
elif (24*60)<=m :
    print (f"Det är {int(m/(24*60))} dygn, {int((m%(24*60))/60)} timmar och {(m%(24*60))%60} minuter")