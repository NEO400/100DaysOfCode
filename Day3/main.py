  # "Treasure Island" Game Style 
  
  # Prompt the user to enter their name
name = input("Enter your name: ")
print('''⠀⠀⠀⠀
       ⢀⣤⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀                       
⠀⠀⢀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣷⡀⠀
⠀⢸⣿⡿⠋⠁⠀⠀⠀⠉⠉⠀⠀⠀⠀⠈⢹⣿⡇⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀
⠀⢸⣿⣠⣤⣶⣶⣶⣦⣀⣀⣴⣶⣶⣶⣤⣄⣿⡇⡀
⣿⣿⣿⠻⣿⣿⣿⣿⣿⠟⠻⣿⣿⣿⣿⣿⠟⣿⣿⣿
⣿⣿⣿⠀⠈⠉⠛⠋⠉⠀⠀⠉⠙⠛⠉⠁⠀⣿⣿⣿
⠙⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠃
⠀⠸⣿⣧⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⣼⣿⠇⠀
⠀⠀⠙⢿⣷⣄⠀⠈⠉⠉⠉⠉⠁⠀⣠⣾⡿⠃⠀⠀
⠀⠀⠀⢸⣿⣿⣷⣤⣀⣀⣀⣀⣤⣾⣿⣿⡅⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠻⠿⠿⠿⠿⠿⠿⠷⠴⠿⠿⠿⠿⠿⠿⠇⠀⠀
''')

  # Print the introductory message to the user
print(f"Wake up, {name}...\nThe Matrix has you...")
print(f"Follow the white rabbit.\nKnock, Knock, {name}. ")

  # Ask the user if they want to open the door
open_door_prompt = input("Would you like to open the door? \nyes or no? ")

  # Convert the response to lowercase for easier comparison
lower_case_string_1 = open_door_prompt.lower()

  # Check if the user wants to open the door
if lower_case_string_1 == "yes": 
  # Ask the user for the answer to a question
  Q1 = input("What's 10 x 10 x 1? \n")
  
  # Check if the user got the answer correct
  if Q1 == "101":
    # Print the continuation of the story
    print(f"I know why you're here, {name}.\nIt's the question that brought you here.\nYou know the question just as I did.\n")
    
    # Ask the user for the question
    Q2 = input("What would be the question? Hint: Don't forget to use '?'\n")
    
    # Convert the response to lowercase for easier comparison
    lower_case_string_2 = Q2.lower()
    
    # Check if the user entered the correct question
    if lower_case_string_2 == "what is the matrix ?": 
      # Print the continuation of the story
      print("Let me tell you why you're here.\nYou're here beacuse you know something.\nWhat you know, you can't explain, but you felt it your entire life.\nThat there's something wrong with the world, you don't know what it is but it's there like a splinter in your mind, drving you mad.\n")
     
      # Ask the user if they know what the speaker is talking about
      Q3 = input("Do you know what I'm talking about?\n")
      
      # Convert the response to lowercase for easier comparison
      lower_case_string_3 = Q3.lower()
      
      # Check if the user knows what the speaker is talking about
      if lower_case_string_3 == "the matrix": 
        # Print the continuation of the story
        print("You have to see it for yourself\nTo be continued...")
    else: 
      # Print the game over message if the user answered incorrectly
      print("You'll never escape it\nGame Over.")
  else: 
    # Print the game over message if the user answered incorrectly
    print("You'll never escape it\nGame Over.")
else:
  # Print the game over message if the user declined to open the door
  print("You'll never find answers\nGame Over.")

  
 
  
  
