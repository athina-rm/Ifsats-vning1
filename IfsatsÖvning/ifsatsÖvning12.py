money=int(input("Beloppet som ska betalas : "))
if 500<=money :
    print(f"Det är {int(money/500)} 500 lappar, {int((money%500)/100)} 100 lappar och {money%100} kronor")
elif money>=100 :
    print(f"Det är {int(money/100)} 100 lappar, och {money%100} kronor")
else :
    print(f"Det är {money} kronor")