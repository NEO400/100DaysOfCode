# Band Name Generator

print("Welcome to the Band Name Generator.")

# 1. Greet the user and ask for their name
name = input("Hello, what's your name? ")
print("Hello " + name + ", Welcome to the Band Name generator!")

# 2. Ask the user for the city they grew up in
city = input("Which city did you grow up in?\n")

# 3. Ask the user for the name of a pet
pet = input("What is the name of a pet?\n")

# 4. Combine the city and pet names to generate a band name
band_name = city + " " + pet
print("Your band name could be: " + band_name)
