# age = 15
# name = "jairo"
# print(name) 
# print(age)
# fruit="apple"
# print (fruit)
# city="london"
# print(city)
# firstmove="e4"
# print(firstmove)
# secondmove="e5"
# print(secondmove)
# thirdmove="c3"
# print(thirdmove)
# adultage=37
# userage=17
# print(adultage+userage)
# def bark():
#   print("woo")

# bark()
# fourthmove="f6"
# print(fourthmove)
# def hello():
#   print("hello")

# hello()
# def e4():
#   print("e5")

# def d4():
#   print("d5")

# def Nf3():
#   print("d5")

# Nf3()

def determine_best_move(opponent_move):
  # ============ first famliy of moves ==================
  if opponent_move == "e4":
    recommended_move = "e5" 
  elif opponent_move == "nf3":
    recommended_move = "Nc6"
    
  elif opponent_move == "d4":
    recommended_move = "exd4"
      
  elif opponent_move == "nxd4":
    recommended_move = "Nxd4"
      
  elif opponent_move =="qxd4":
    recommended_move = "d6"
      
  elif opponent_move == "bf2":
    recommended_move = "Be6"
      
  elif opponent_move == "ba4":
    recommended_move = "Bb5"
      
  elif opponent_move == "nc3":
    recommended_move = "Nf6"
      
  elif opponent_move == "be3":
    recommended_move = "Bc4"
      
  elif opponent_move == "bxc4":
    recommended_move = "Nf6"
      
  elif opponent_move == "e5":
    recommended_move = "dxe5"
    print ("You should be ready to enjoy the game. Goodbye")
    
  else:
    recommended_move = "not available"
  print("recomended move is " + recommended_move)
  return recommended_move



print("hello welcome to chess opening tutorial")
print("this is a tutorial that will help you to play against the Scotch Game\n\n")

condition = True
while condition:
  opponent_move=input("what move did your opponent make?: \n").lower()
  move = determine_best_move(opponent_move)
  print(move)
  if move == "dxe5":
    condition = False
# ============ Second famliy of moves ==================


# elif responce1== "e4":
#     print("e5")
#     input()
# elif responce1== "nf3" or "Nf3":
#     print ("Nc6")
#     input()
# elif responce1=="d4"or "D4":
#     print ("exd4")
#     input()
# elif responce1=="nxd4"or "Nxd4":
#     print ("Nxd4")
#     input()
# elif responce1=="Qxd4"or "qxd4":
#     print ("d6")
#     input()
# elif responce1("nc3"or "Nc3"):
#     print ("Nf6")
#     input()
# elif responce1==("f3"or "F3"):
#     print ("Be3")
#     input()
# else:
#     print('unknown move')

