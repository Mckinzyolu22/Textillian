from room import Room
from character import Enemy, Friend, Character
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
# I removed kitchen.describe() right before linking
dining_hall = Room("Dining Hall")
dining_hall.set_description("A room with four-legged Chiefs being fed every 6 hours or so.")

bedroom = Room("Bedroom")
bedroom.set_description("You get to live your dreams here.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(bedroom, "west")
bedroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hey, what's up?")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
bedroom.set_item(cheese)

#Add new character

catrina = Character("Catrina", " A friendly Skeleton" )

catrina.set_conversation("Why hello there!" )

esu = Enemy("Esu", "The devil himself,weak at heart but appears to be evil")
esu.set_conversation("Who wants to die today?")
esu.set_weakness("love")
bedroom.set_character(esu)

love = Item("love")
love.set_description("Couples are expected to have it, the world needs it")
dining_hall.set_item(love)



# Removed dining_hall.get_details() after adding def move(...) in room.py

current_room = kitchen
# Adding a backpack to store items
backpack = []

#bringing in dead, changed while True to while dead to ensure the game will only continue while we're not dead

dead =  False


while dead == False:
  
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
 # Add item description if present in the room 
  item = current_room.get_item()
  if item is not None:
    item.describe()
  
  command = input("> ")
 # check whether a direction was typed 
  if command in ["north", "south", "east", "west"]:
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
  elif command == "fight":
    if inhabitant is not None:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      
      # Do I have this item?
      if fight_with in backpack:
      
        if inhabitant.fight(fight_with) == True:
          # What happens if you win?
          print("Hooray, you won the fight!")
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Congratulations, you have vanquished the enemy!")
            dead = True
        else:
          # What happens if you lose?
          print("Boomerang! you lost the fight")
          print("That's the end of the game, you could try again; I'm gonna punch you in the gut next time..hahaha")
          dead = True
      else:
        print("You don't have a " + fight_with)
    else:
      print("There is no one here to fight with")
  elif command == "take":
    #Take the item and put it in the backpack
    if item is not None:
        
       print("You put the " + item.get_name() + " in your backpack")
       backpack.append(item.get_name())
       current_room.set_item(None)
    else:
      print("There's nothing here to take!")
  else:
    print("I don't know how to " + command)
    
  
