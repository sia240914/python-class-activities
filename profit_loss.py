buying_price=float(input("enter buying price "))
selling_price=float(input("enter selling price "))

if(buying_price<selling_price):
    print("profit")

else:
    print("loss")

profit =(selling_price-buying_price)
print(profit)

percent=(profit*100)/buying_price
print(percent,"%")
