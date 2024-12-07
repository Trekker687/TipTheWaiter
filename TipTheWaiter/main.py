def totalcalc(billamount, tipperc):
    total = billamount*(1+0.01*tipperc)
    total = round(total,2)
    print(f"please pay $ {total}")

n = int(input("Enter bill amount: "))
totalcalc(n,20)