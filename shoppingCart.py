foods =[ ]
prices = []
total=0



while True:
    food = input("enter a food to buy or press q to quit ")
    if food.lower() == "q" :
        break
    else:
        price = float(input(f"Enter the price of the {food} : R"))
        food.append(food)
        prices.append(price)
    
    print("***************** your cart************* ")
    

    for food in foods:
        print(food )



    for price in prices:
        total += price

    print(f"Your total is : R{total}")

        

