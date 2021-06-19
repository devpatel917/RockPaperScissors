


def win(UserPoints,betAmount,ComputerPoints):
   UserPoints = UserPoints + betAmount
   ComputerPoints = ComputerPoints - betAmount
   print("User Points: ", UserPoints, "Computer Points: ", ComputerPoints)

def loss(UserPoints,betAmount,ComputerPoints):
   UserPoints = UserPoints - betAmount
   ComputerPoints = ComputerPoints + betAmount
   print("Player 1 Points: ", UserPoints, "Player 2 Points: ", ComputerPoints)
def tie(UserPoints,betAmount,ComputerPoints):
   UserPoints = UserPoints - betAmount
   print("Player 1 Points: ", UserPoints, "Player 2 Points: ", ComputerPoints)

def RockPaperScissor():
   import random
   options = ["paper", "rock", "scissor"]
   UserWins = 0
   UserTies = 0
   UserLosses = 0
   AmountPlayed = 0
   rock = 0
   paper = 0
   scissor = 0
   gameType = input("Do you want to play OnePlayer or TwoPlayer. Type either one or two")
   UserPoints = 0
   ComputerPoints = 0

   if gameType == "one":
       while (UserLosses < 3 and UserWins < 3):
           x = (random.randrange(0, 3))
           computerOption = options[x]
           AmountPlayed = AmountPlayed + 1
           if AmountPlayed >= 2:
               hint = input("do you want a hint, but this will cause a loss of some points. Answer yes or no")
               if hint == "yes":
                   print("These are previous Computer Picks. ", "Rock : ", rock, "/", AmountPlayed, "Paper: ", paper,
                         "/",
                         AmountPlayed, "Scissor: ", scissor, "/", AmountPlayed)
                   UserPoints = UserPoints - 30

           # This makes sense because previous Computer picks can only happen after the 2nd round because in the 1st round, you already know what the computer has picked, so it's not that useful
           # print(computerOption)

           userOption = input("enter your choice")
           betAmount = input("how many points do you want to bet that you have won. ")
           betAmount = int(betAmount)

           if userOption == "rock" and computerOption == "paper":
               UserLosses = UserLosses + 1
               paper=paper+1
               loss(UserPoints, betAmount, ComputerPoints)
               print("Games lost by User: ", UserLosses)

           if userOption == "rock" and computerOption == "rock":
               UserTies = UserTies + 1
               rock=rock+1
               tie(UserPoints, betAmount, ComputerPoints)
               print("Games Tied: ", UserTies)
           if userOption == "rock" and computerOption == "scissor":
               win(UserPoints, betAmount, ComputerPoints)
               UserWins = UserWins + 1
               scissor=scissor+1
               print("Games Won by User: ", UserWins)

           if userOption == "paper" and computerOption == "paper":
               UserTies = UserTies + 1
               paper = paper + 1
               tie(UserPoints, betAmount, ComputerPoints)
               print("Games Tied: ", UserTies)

           if userOption == "paper" and computerOption == "rock":
               UserWins = UserWins + 1
               rock = rock + 1
               win(UserPoints, betAmount, ComputerPoints)
               print("Games Won by User: ", UserWins)

           if userOption == "paper" and computerOption == "scissor":
               UserLosses = UserLosses + 1
               scissor = scissor + 1
               loss(UserPoints, betAmount, ComputerPoints)
               print("Games lost by User: ", UserLosses)

           if userOption == "scissor" and computerOption == "rock":
               UserLosses = UserLosses + 1
               rock = rock + 1
               loss(UserPoints, betAmount, ComputerPoints)
               print("Games lost by User: ", UserLosses)

           if userOption == "scissor" and computerOption == "paper":
               UserWins = UserWins + 1
               paper = paper + 1
               win(UserPoints, betAmount, ComputerPoints)
               print("Games Won by User: ", UserWins)

           if userOption == "scissor" and computerOption == "scissor":
               UserTies = UserTies + 1
               scissor = scissor + 1
               tie(UserPoints, betAmount, ComputerPoints)
               print("Games Tied: ", UserTies)

       # use returns for defs
       # shorten the amount of (ifs)
   # in order to not create more variables and limit the amount of variables i need, i just let computerOption (which was already in onePlayer) as player 2 in twoPlayer, so i wouldn't have to create another variable)
   if gameType == "two":
       while (UserLosses < 3 and UserWins < 3):
           computerOption = input("player 1 put in ur guess")
           AmountPlayed = AmountPlayed + 1

           # This makes sense because previous Computer picks can only happen after the 2nd round because in the 1st round, you already know what the computer has picked, so it's not that useful
           # print(computerOption)

           userOption = input("player 1, enter your choice")
           betAmount = input("how many points do you want to bet that you have won. ")
           betAmount = int(betAmount)
           if AmountPlayed >= 2:
               hint = input("do you want a hint, but this will cause a loss of some points. Answer yes or no")
               if hint == "yes":
                   print("These are previous Computer Picks. ", "Rock : ", rock, "/", AmountPlayed, "Paper: ", paper,
                         "/",
                         AmountPlayed, "Scissor: ", scissor, "/", AmountPlayed)
                   UserPoints = UserPoints - 30

           if userOption == "rock" and computerOption == "paper":
               paper = paper + 1
               UserLosses = UserLosses + 1
               loss(UserPoints,betAmount,ComputerPoints)

               print("Games lost by User: ", UserLosses)
           if userOption == "rock" and computerOption == "rock":
               UserTies=UserTies+1
               rock = rock + 1
               tie(UserPoints, betAmount, ComputerPoints)


               print("Games Tied: ", UserTies)
           if userOption == "rock" and computerOption == "scissor":
               UserWins = UserWins + 1
               scissor = scissor + 1
               UserPoints = UserPoints + betAmount
               win(UserPoints, betAmount, ComputerPoints)
               print("Games Tied: ",UserTies)

           if userOption == "paper" and computerOption == "paper":
               UserTies = UserTies + 1
               paper = paper + 1
               tie(UserPoints, betAmount, ComputerPoints)
               print("Games Tied: ", UserTies)

           if userOption == "paper" and computerOption == "rock":
               UserWins = UserWins + 1
               rock = rock + 1
               win(UserPoints, betAmount, ComputerPoints)
               print("Games Won by User: ", UserWins)

           if userOption == "paper" and computerOption == "scissor":
               UserLosses = UserLosses + 1
               scissor = scissor + 1
               loss(UserPoints, betAmount, ComputerPoints)
               print("Games lost by User: ", UserLosses)

           if userOption == "scissor" and computerOption == "rock":
               UserLosses = UserLosses + 1
               rock = rock + 1
               loss(UserPoints, betAmount, ComputerPoints)
               print("Games lost by User: ", UserLosses)

           if userOption == "scissor" and computerOption == "paper":
               UserWins = UserWins + 1
               paper = paper + 1
               win(UserPoints, betAmount, ComputerPoints)
               print("Games Won by User: ", UserWins)

           if userOption == "scissor" and computerOption == "scissor":
               UserTies = UserTies + 1
               scissor = scissor + 1
               tie(UserPoints, betAmount, ComputerPoints)
               print("Games Tied: ", UserTies)
RockPaperScissor()


