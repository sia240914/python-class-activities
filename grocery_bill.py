def calculate(quantity,priceperunit):
    billamount=quantity*priceperunit
    return billamount

print("apple=Rs.100","per kg")
print(" chocolates=Rs.15")
print("chips=Rs.20")
apples=float(input("how much apples do you want?"))
chocolates=int(input("how much chocolates do you want?"))
chips=int(input("how much chips packet do you want?"))
priceapple=calculate(apples,100)
pricechocolates=calculate(chocolates,15)
pricechips=calculate(chips,20)
total_bill=priceapple+pricechips+pricechocolates
print ( "the total bill is ",total_bill)