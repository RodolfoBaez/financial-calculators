
print("Welcome to Financial-Calculators ")
print("What would you like to calulate ")
print("")
print("1. Bank Savings Account Interest ")
print("2. Stock Market Growth Per Year")
print("")


user_choice = input("Input your response ")

if user_choice == "1":
  print("Using the Annual Inflation Rate Of 2.5%, We Will Tell You If Your Beating Inflation")
  initial_deposit = float(input("Ammount Of Initial Deposit "))
  time_for_interest = float(input("How long Are You Going To Save For In (Years) "))
  APY = float(input("What Is Your APY For Your Savings Account "))
  ammount_of_interest = initial_deposit * ((1 + APY/100) ** time_for_interest) - initial_deposit
  print("")
  print("Your Ending Balance In Your Savings Account After " + str(time_for_interest) + " Years Is ")
  print(ammount_of_interest + initial_deposit)
  print("")
  print("You Earned In Interest " + "$" + str(ammount_of_interest))
  print("")
  if 2.50 > APY:
    print("Inflation Beat Your Saving Account Interest, Try To Beat The Inflation Rate Of 2.50% With A Better Savings Account ")
  if 2.50 < APY:
    print("You Beat inflation With Your Saving Account Interest, Great Saving Account You Have ")

elif user_choice == "2":
  print("Using The Annual Returns of the Stock Market Of 10%, We Will Calulate You Investment Gains")
  initial_investment = float(input("How Much Are You Investing In the Stock Market "))
  time = float(input("For How Long Are you Planning To Invest For (Years) "))
  ammount_of_investment = initial_investment * ((1 + 10/100) ** time) - initial_investment
  print("You Gained " + "$" + str(ammount_of_investment))

  
else:
  print("invaild responds")
