## 4. Implementing Binary Search: Part 1 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    # We need to format our name appropriately for successful comparison
    name = format_name(name)
    # First guess halfway through the list
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[first_guess_index][0])
    # Check where we should continue searching
    if name < first_guess:
        return 'earlier'
    elif name > first_guess:
        return 'later'
    else:
        return 'found'

johnson_odom_age = player_age("Darius Johnson-Odom")
young_age = player_age("Nick Young")
adrien_age = player_age("Jeff Adrien")   
    

## 5. Implementing Binary Search: Part 2 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    # We need to format our name appropriately for successful comparison
    name = format_name(name)
    # Initial bounds of the search
    upper_bound = length - 1
    lower_bound = 0
    # Index of first split
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[first_guess_index][0])
    # If the name comes before our guess
        # Adjust the bounds as needed
    # Else if the name comes after our guess
        # Adjust the bounds as needed
    # Else
        # Player found, so return first guess
    # Set the index of the second split
    # Find and format the second guess
    # Return the second guess
    if name < first_guess:
        upper_bound = first_guess_index - 1
        
    elif name > first_guess:
        
        lower_bound = first_guess_index + 1   
    else:
        return first_guess
    second_guess_index = math.floor((upper_bound+lower_bound)/2)
    second_guess = format_name(nba[second_guess_index][0])
    return second_guess
gasol_age = player_age("Pau Gasol")
pierce_age = player_age("Paul Pierce")

## 7. Implementing Binary Search: Part 3 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    # We need to format our name appropriately for successful comparison
    name = format_name(name)
    # Bounds of the search
    upper_bound = length - 1
    lower_bound = 0
    # Index of first split. It's important to understand how we compute this
    index = math.floor((upper_bound + lower_bound) / 2)
    # First, guess halfway through the list
    guess = format_name(nba[index][0])
    # Keep guessing until it finds the name. Use a while loop here.
    while name != guess:
        if name < guess:
            upper_bound = index-1
        else:
            lower_bound = index +1
        index = math.floor((upper_bound + lower_bound) / 2)
    # First, guess halfway through the list
        guess = format_name(nba[index][0])  
    return 'found'
carmelo_age = player_age('Carmelo Anthony')
        # Check where our guess is in relation to the name we're requesting,
        #     and adjust our bounds as necessary (multiple lines here).
        #     If we have found the name, we wouldn't be in this loop, so
        #     we shouldn't worry about that case
        # Find the new index of our guess
        # Find and format the new guess value
    # When our loop terminates, we have found the right NBA player's name

## 8. Implementing Binary Search: Part 4 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    name = format_name(name)
    # Set the initial upper bound of the search
    upper_bound = length-1
    # Set the initial lower bound of the search
    lower_bound = 0
    # Set the index of the first split (remember to use math.floor)
    index = math.floor(length/2)
    # First guess at index (remember to format the guess)
    guess = format_name(nba[index][0])
    # Run search code until the name is equal to the guess, or upper bound is less than lower bound
    while name != guess and upper_bound >= lower_bound:
                  
        # If name comes before the guess
        if name < guess:
            upper_bound = index-1
            # Change the appropriate bound
        # Else (name comes after the guess)
        else:
            lower_bound = index +1
            # Change the appropriate bound
        # Set the index of our next guess (remember to use math.floor)
        index = math.floor((upper_bound+lower_bound)/2)
        guess = format_name(nba[index][0])
        # Retrieve and format our next guess
        
    ### Now that our loop has terminated, we must find out why ###
    # If the name is equal to the guess
    if name == guess:
        return nba[index][2]
        # Return the age of the player at index (column index 2 in data set)
    else:
        return -1
    # Else
        # Return -1, because the function didn't find our player
curry_age = player_age("Stephen Curry")
griffin_age = player_age("Blake Griffin")
jordan_age = player_age("Michael Jordan")