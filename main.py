print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
area = input("You're at area 51. Do you stay by going left or leave by going right and explore the dessert? (l or r)\n ")
area51 = area.lower()
if area51 == "l":
  alien = input("You have been abducted by aliens. Do you run or try to make peace with them? (r or p)\n ")
  aliens = alien.lower()
  if aliens == "p":
    universe_wish = input("They say that they can tell you the secrets of the universe or make your wish come true by rubbing a lamp. universe or lamp? (u or l)\n " )
    universe_or_wishes = universe_wish.lower()
    if universe_or_wishes == "u":
      print("You learned everything about the universe and became god and helped everyone through space and time but you did not get the treasure. YOU WIN.")
    elif universe_or_wishes == "l":
      print("You fulfilled your wishes, found the treasure, and became happy forever. YOU WIN.")
  else:
    print("The aliens stole your soul and left. GAME OVER.")
else:
  print("You got lost in the dessert and died of dehydration. GAME OVER.")
