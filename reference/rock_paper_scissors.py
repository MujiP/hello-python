
# We'll make a rock, paper, scissors game
# We'll ask the user for their input, then we'll choose a random choice for the computer.
# Then we'll compare the two and see who wins


user_choice = input('Choose rock, paper, or scissors: ')
# user_choice = user_choice.lower()
print(user_choice)

allowed_choices = ['rock', 'paper', 'scissors']

if user_choice not in allowed_choices:
    print('Invalid choice, please try again')
    exit()

# What does it mean if the code gets here?
