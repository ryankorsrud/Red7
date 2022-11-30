import random
import collections
import os
import time

'''
Generate the red7 deck of 49 cards.
Parameter: deck.
returns: deck.
'''
def create_deck(deck):
  for j in colour:
    for i in num:
      deck.append((j, i))
  return deck

'''
Shuffles the red7 deck.
Parameter: deck
Returns: deck
'''
def shuffle(deck):
  while True:
      try:
        shuffle_times = int(input('How many times do you want to shuffle the deck? '))
        break
      except:
        print('Invalid input.')
  for i in range(1000 * shuffle_times):
    index = random.randint(0, len(deck)-1)
    split = deck[index]
    deck.remove(split)
    deck.append(split)
  return deck

'''
Deals cards out to the players.
Parameters: numCards
Returns: cardsDrawn
'''
def draw_cards(cards, numCards):
  cardsDrawn = []
  for x in range(numCards):
    cardsDrawn.append(cards.pop(0))
  return cardsDrawn

'''
Prints the instructions
Parameters: None
Returns: none.
'''
def instructions():
  os.system("clear")
  print("After chosing the number of players and times you want to shuffle, each player will be dealt 7 cards to their hand and one card to their palette. In your each players turn they will add one card to their palette and can choose if they would like to play a card to change the rule. If at the end of their turn, the player isn't winning accourding to the current rule they are out. If a player has no cards to play on their turn they are also out. The player next to the player with the highest card will always start each game.")
  okay = input("Press enter to continue")
  os.system("clear")
  menu()

'''
Prints out the players cards.
Parameters: player, playerHand.
Returns: nothing
'''
def show_hand(rule, out, playerTurn, players):
  print('''Player %s's Turn:
Your Hand''' %(playerTurn+1))
  y = 1
  for card in players[0]["hand"]:
    print("%s) %s %s" %(y, card[0], card[1]))
    y+=1
  x = 1
  print("")
  print("Your Palette")
  for card in players[0]["palette"]:
    print("%s) %s %s" %(x, card[0], card[1]))
    x+=1
  x = 0
  for cards in players:
    y = 1
    if x != 0 and x not in out:
      print("")
      print("Player %s's Palette" %(x+1))
      for card in cards['palette']:
        print("%s) %s %s" %(y, card[0], card[1]))
        y+= 1
    x+=1
  print("")
  print('''Rules/Rank:
1. Red    --> Highest Card
2. Orange --> Most of One Number
3. Yellow --> Most of One Colour
4. Green  --> Most Even Cards
5. Blue   --> Most Different Colours
6. Indigo --> The Largest Run
7. Violet --> The Most Cards Under 4
Current Rule: %s
''' %(rule))

  
'''
Checks if the player can play their desired card.
Parameters: colour, value, playerHand.
Returns: True or False
'''
def canPlay(cardChosen, playerHand):
  return cardChosen in playerHand


'''
Gets specified values from the players palettes.
Parameters: players, vals, out.
Returns: values.
'''
def get_values(players, vals, out):
  values = []
  for i in range(len(players)):
    num = []
    if i not in out:
      for x in range(len(players[i]['palette'])):
        num.append(players[i]["palette"][x][vals])
      values.append(num)
  return values

'''
Checks if the players is winning with the current rule.
Parameter: playerTurn, lst.
Returns: True or False
'''
def winning(playerTurn, lst):
  colours = dict([(y,x) for x,y in enumerate(colour)])
  try:
    sort = sorted(lst, key = lambda x: (x[1], colours[x[0]]), reverse=True)
  except:
    sort = sorted(lst, reverse=True)
  if len(sort) >= 2 and sort[0] == sort[1]:
    return False
  else:
    return sort[0] == lst[playerTurn]




'''
Gets the largest card from a list.
Parameters: lst.
Returns: sort[0]
'''
def max_num(lst):
  colours = dict([(y,x+1) for x,y in enumerate(colour)])
  sort = sorted(lst, key = lambda x: (x[1], colours[x[0]]), reverse=True)
  return sort[0]
  
'''
Gets the highest card from a players palette.
Parameters: i, count
Returns: max_num(i)
'''
def highest(i, count):
  return max_num(i)

'''
Gets the most common number from a players palette
Parameters: i, count
Returns: collections.Counter([j for j in i]).most_common(1)[0][1]
'''
def one_num(i, count):
  return collections.Counter([j for j in i]).most_common(1)[0][1]

'''
Checks what the most common colour in a players palette is.
Parameters: i, count.
Returns: collections.Counter([j for j in i]).most_common(1)[0][1]
'''
def one_colour(i, count):
  return collections.Counter([j for j in i]).most_common(1)[0][1]

'''
Gets the number of even cards in a players palette.
Parameters: playerTurn
Returns: count
'''
def even_cards(i, count):
  for j in i:
    if j % 2 == 0:
      count += 1
  return count

'''
Checks how many different colours their is in a players palette
Parameters: i, count.
Returns: len(set(i))
'''
def different_colours(i, count):
  return len(set(i))

'''
Finds the largest run in a players palette.
Parameters: i, count.
Returns: count
'''
def largest_run(i, count):
  for x in i:
    if x-1 not in i:
      streak = 0
      while x in i:
        x+=1
        streak+=1
        count = max(count,streak)
  return count

'''
Finds the number of cards under four in a players palette.
Parameters: i, count.
Returns: count
'''
def under_four(i, count):
  for x in i:
    if x < 4:
      count += 1
  return count

'''
Checks to see if whoevers turn it is is winning with the current rule.
Parameters: rule, players, out, playerTurn.
Returns: winning(playerTurn, final_nums)
'''
def rules(rule, players, out, playerTurn):
  nums = get_values(players, r[rule][1], out)
  final_nums = []
  for i in nums:
    count = 0
    final_nums.append(r[rule][0](i, count))
  return winning(playerTurn, final_nums)

'''
Asks the user how many players they want.
Parmaeters: none.
Returns: numPlayers.
'''
def num_of_players():
  while True:
      try:
        numPlayers = int(input("How many players? "))
        if 2 <= numPlayers and numPlayers <= 4:
          break
        else:
          print("Invalid choice. Pick a number between 2-4.")
      except:
        print("Invalid choice. Pick a number.")
  return numPlayers
  
'''
Asks the user to pick which card they want to play.
Parameters: none.
Returns: cardChosen.
'''
def pick_card(players):
  while True:
    try:
      colour, num = input('Pick a card ').split()
      cardChosen = tuple([colour, int(num)])
      if canPlay(cardChosen, players[0]["hand"]):
        break
      else:
        print("Invalid input.")
    except:
      print("Invalid input.")
  return cardChosen

'''
Finds which cards the ai player should play and plays them.
Parameters: rule, playerTurn.
Returns: rule or new_rule
'''
def ai(rule, out, playerTurn, players):
  for i in players[playerTurn]['hand']:
    players[playerTurn]['palette'].append(i)
    if rules(rule, players, out, playerTurn):
      players[playerTurn]['hand'].remove(i)
      time.sleep(1)
      os.system('clear')
      show_hand(rule, out, playerTurn, players)
      print("Player %s added %s %s to their palette." %(playerTurn+1, i[0], i[1]))
      confirm = input("Press enter to continue...")
      return players, rule
    else:
      players[playerTurn]['palette'].remove(i)

  for i in players[playerTurn]["hand"]:
    for x in players[playerTurn]['hand']:
      if i != x:
        players[playerTurn]['palette'].append(x)
        if rules(i[0], players, out, playerTurn):
          time.sleep(2)
          print("Player %s added %s %s to their palette." %(playerTurn+1, x[0], x[1]))
          players[playerTurn]['hand'].remove(i)
          time.sleep(2)
          print("Player %s changed the rule to %s." %(playerTurn+1, i[0]))
          players[playerTurn]['hand'].remove(x)
          confirm = input("Press enter to continue...")
          return players, i[0]
        else: 
          players[playerTurn]['palette'].remove(x)

  players[playerTurn]['palette'].append(players[playerTurn]['hand'][0])
  players[playerTurn]['hand'].pop(0)
  return players, rule

'''
Makes the user play a card, and choose to change the rule for their turn.
Parameters: rule
Returns: rule or cardChosen[0].
'''
def plr(rule, out, playerTurn, players):
  cardChosen = pick_card(players)
  players[0]["hand"].remove(cardChosen)
  players[0]["palette"].insert(0, cardChosen)
  os.system("clear")
  show_hand(rule, out, playerTurn, players)
  print("You added %s %s to your palette." %(cardChosen[0], cardChosen[1]))
  changeRule = input("Would you like to change the rule? y/n ")
  while changeRule.lower() != 'y' and changeRule.lower() != 'n':
    changeRule = input("Invalid input. Would you like to change the rule? y/n ")
  if changeRule.lower() == 'y':
    cardChosen = pick_card(players)
    players[0]["hand"].remove(cardChosen)
    rule = cardChosen[0]
  return players, rule


'''
Controls the flow of the game.
Parameters: none.
Returns none.
'''
def play():
  os.system("clear")
  rule = "Red"
  cards = create_deck([])
  players = []
  out = []
  numPlayers = num_of_players()
  shuffle(cards)
  p = [plr]
  for player in range(numPlayers):
    hand = draw_cards(cards, 7)
    palette = draw_cards(cards, 1)
    players.append({"hand": hand, "palette": palette})
    if(player > 0):
      p.append(ai)
  nums = []
  for i in range(len(players)):
    nums.append(players[i]["palette"][0])
  playerTurn = nums.index(max_num(nums)) + 1
  if playerTurn == len(players):
    playerTurn = 0
  os.system("clear")

  while True:
    os.system("clear")
    show_hand(rule, out, playerTurn, players)
    if len(players[playerTurn]["hand"]) <= 1:
      out.append(playerTurn)
    else:
      players, rule = p[playerTurn](rule, out, playerTurn, players)
    if rules(rule, players, out, playerTurn) == False:
      out.append(playerTurn)

    playerTurn += 1
    if playerTurn in out:
      playerTurn += 1
    if playerTurn > len(players)-1:
      playerTurn = 0
    elif playerTurn > len(players):
      playerTurn = 1

    if len(out)+1 == len(players):
      print("Player %s wins!" %(playerTurn+1))
      play_again = input('Do you want to play again?y/n ')
      while play_again.lower() != 'y' and play_again.lower() != 'n':
        print("Please choose either 'y' or 'n'")
        play_again = input('Do you want to play again?y/n ')
      if play_again.lower() == 'n':
        break
      else: 
        menu()

'''
Creates the main menu and asks the user what they want to do.
Parameters: none. 
Returns: none.
'''
def menu():
  print('''-------------------------- MENU --------------------------
1. Play Game
2. Instructions
3. Quit''')
  while True:
    choice = input('Please enter an option[1-3]: ')
    try:
      choice = int(choice)
      if 3>= choice >= 1:
        break
      else:
        print("Pick a number between 1-3")
    except:
      print("Invalid Choice")
  if choice == 1:
    play()
  elif choice == 2:
    instructions()

num = [1, 2, 3, 4, 5, 6, 7]
colour = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
r = {
  "Red": [highest, slice(0, 2)],
  "Orange": [one_num , 1],
  "Yellow": [one_colour, 0],
  "Green": [even_cards, 1],
  "Blue": [different_colours, 0],
  "Indigo": [largest_run, 1],
  "Violet": [under_four, 1]
}

menu()
