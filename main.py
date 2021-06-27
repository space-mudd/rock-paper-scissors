import random



def game () :
  def calculate_game (player,ai):
    print("You played: " + player)
    print("The computer played: " + ai)

    if player == 'p' and ai == 'r' or player == 's' and ai == 'p' or player == 'r' and ai == 's':
      print("You win")


    if player == 'r' and ai == 'p' or player == 'p' and ai == 's' or player == 's' and ai == 'r':
      print("You lost")

    if player == ai:
      print("Tie")

  rps = input("choose r for rock choose p for paper choose s for scissors\n")



  # 1 = rock
  # 2 = paper
  # 3 = scissors

  dictionary = {
    1 : "r",
    2 : "p",
    3 : "s"
  }

  rand = random.randint(1,3)

  ai_rps = dictionary[rand]

  calculate_game(rps, ai_rps)
  
while(True):
  game()
  