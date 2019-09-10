candylist = ["M&M", "Snickers", "Toffee", "Caramel Apple"]
#allowance = 3
candy_cart = []

for candy in candylist:
    index = candylist.index(candy)
    print(f"[{index}]{candy}")


confirm = "y"

while confirm == "y":

    num = int(input("What candy would you like?"))

    candy_cart.append(candylist[num])

    confirm = input("Would you like more candy? ")

    #num = int(input("What candy would you like?"))

    #candy_cart.append(candylist[num])

###candy_cart.append(candylist[num])
print (candy_cart)
