def tip(bill,perc):
    total_amount=bill*(1+0.01*perc)
    total_amount=round(total_amount,2)
    return total_amount
bill=float(input("enter bill amount"))
perc=float(input("enter the tip percentage"))
ans=tip(bill,perc)
print(ans)
