# input income
while True:
  balance = input("What is your income each month?: ")
  if balance.isdigit():
    balance = int(balance)
    if balance > 0:
      print("Your Balance is:", balance)
      break
  else:
    print("Invalid input")

# input rent/mortage
while True:
    rent = input("How much do you spend on rent/mortage monthly: ")
    if rent.isdigit():
       rent = int(rent)
       if rent > 0:
        balance2 = balance - rent
        print("Your balance after food is:", balance2)
        break
    else:
      print("Invalid input")

# input food spend
while True:
    food = input("On average how much do you spend on food monthly: ")
    if food.isdigit():
        food = int(food)
        if food > 0:
          balance3 = balance2 - food
          print("Your balance after food is:", balance3)
          break
    else:
      print("Invalid input")

# want spends
while True:
    wants = input("How much do you spend on nonessentials: ")
    if wants.isdigit():
      wants = int(wants)
      if wants > 0:
        balance4 = balance3 - wants
        print("Your balance after unessentials is:", balance4)
        break
    else:
        print("Invalid input")

# ending balance
print("Your ending balance is:", balance4)