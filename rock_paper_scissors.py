import random
import os

# --- CONFIGURATION & PERSISTENCE ---
# File path where the highest win streak is permanently stored
HISTORY_FILE = "max_streak.txt"

# Initialize or load the historical max streak on game startup
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as file:
        try:
            # Read and convert the stored high score to an integer
            max_streak = int(file.read().strip())
        except ValueError:
            # Fallback to 0 if the text file contains corrupted or empty data
            max_streak = 0
else:
    # Set to 0 if the file does not exist yet (first-time players)
    max_streak = 0

# --- GAME ASSETS & GAMEPLAY RULES ---
# Visual mapping for cleaner UI terminal prints
emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}

# Tuple containing valid input options for the computer and validation
choices = ('r', 'p', 's')

# Dictionary mapping mapping each player choice to the exact move it defeats
winning_rules = {'r': 's', 'p': 'r', 's': 'p'}

# Initialize the current session's live score tracking
win_streak = 0

# --- MAIN GAME LOOP ---
while True:
    # Print a visual separator for better readability between game rounds
    print('-' * 100)
    
    # Prompt user for their choice and normalize the text input to lowercase
    user_choice = input(f"Enter r ({emojis['r']} ), p ({emojis['p']}), s ({emojis['s']} ), or q (quit): ").lower()
    
    # Check for the exit command
    if user_choice == 'q':
        print("Thanks for playing!")
        break
        
    # Input validation: Reject strings that are not part of the game choices
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    # Let the computer randomly select its move
    computer_choice = random.choice(choices)

    # Output the visually formatted selections to the user
    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')

    # --- ROUND EVALUATION LOGIC ---
    if user_choice == computer_choice:
        print("It's a tie! 🔵")
        
    elif winning_rules[user_choice] == computer_choice:
        print('You win! 🟢')
        win_streak += 1
        print(f"Current streak: {win_streak}")
        
        # Check and update the historical record dynamically if broken
        if win_streak > max_streak:
            max_streak = win_streak
            print(f"🔥 NEW ALL-TIME RECORD: {max_streak}!")
            
    else:
        print('You lose! 🔴')
        print(f'Your win streak is: {win_streak}') 
        print(f"The all-time record remains: {max_streak}")
        
        # Reset current session streak upon losing
        win_streak = 0 
        
        # Open file and permanently save the current high score before exiting
        with open(HISTORY_FILE, "w") as file:
            file.write(str(max_streak))
        break
