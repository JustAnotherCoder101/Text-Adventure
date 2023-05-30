def tshop(Coins):
  print("You reach the blacksmith's")
  print("BlackSmith:Sorry Kid,this sword is the only thing available today")
  print("You Great!")
  input()
  while True:
    if input("press 1 to buy the sword for 5 coins."):
      Coins =- 5
      print("Sword bought!")
      print("you now have "+str(Coins)+" coins")
      return
    else:
      print("Sorry, that was not a available input")
      print()
