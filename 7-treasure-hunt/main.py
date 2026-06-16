import random

def play_game():
    print("=" * 40)
    print("     WELCOME TO TREASURE HUNTER!     ")
    print("=" * 40)
    print("Instructions: Move around a 4x4 grid.")
    print("Find the Treasure (T) before hitting a Trap (X).")
    print("Commands: W (Up), S (Down), A (Left), D (Right), Q (Quit)\n")

    # Set up grid boundaries (0 to 3)
    grid_size = 4
    
    # Starting position of the player
    player_x, player_y = 0, 0
    
    # Hide the treasure and traps randomly
    treasure_x, treasure_y = random.randint(0, 3), random.randint(0, 3)
    trap_x, trap_y = random.randint(0, 3), random.randint(0, 3)
    
    # Ensure treasure and trap don't spawn on the player's starting spot
    while (treasure_x == 0 and treasure_y == 0) or (trap_x == 0 and trap_y == 0) or (treasure_x == trap_x and treasure_y == trap_y):
        treasure_x, treasure_y = random.randint(0, 3), random.randint(0, 3)
        trap_x, trap_y = random.randint(0, 3), random.randint(0, 3)

    while True:
        # Print the visual map dashboard
        print(f"Your current position: Grid Square ({player_x}, {player_y})")
        
        # Display hints based on proximity
        distance_to_treasure = abs(player_x - treasure_x) + abs(player_y - treasure_y)
        if distance_to_treasure == 1:
            print("Hint: You feel a warm glow nearby... the treasure is close!")
        elif abs(player_x - trap_x) + abs(player_y - trap_y) == 1:
            print("Warning: You hear a strange clicking sound... a trap is nearby!")
            
        # Get user input
        move = input("Enter your move (W/A/S/D) or Q to quit: ").strip().upper()
        print("-" * 40)

        # Process input logic
        if move == 'Q':
            print("You abandoned the hunt. Safe travels!")
            break
        elif move == 'W': # Move Up
            if player_y < grid_size - 1: player_y += 1
            else: print("Ouch! You hit a boundary wall. Choose another direction.")
        elif move == 'S': # Move Down
            if player_y > 0: player_y -= 1
            else: print("Ouch! You hit a boundary wall. Choose another direction.")
        elif move == 'A': # Move Left
            if player_x > 0: player_x -= 1
            else: print("Ouch! You hit a boundary wall. Choose another direction.")
        elif move == 'D': # Move Right
            if player_x < grid_size - 1: player_x += 1
            else: print("Ouch! You hit a boundary wall. Choose another direction.")
        else:
            print("Invalid command! Use W, A, S, D to move or Q to quit.")
            continue

        # Check win/loss outcomes
        if player_x == treasure_x and player_y == treasure_y:
            print("CONGRATULATIONS! You found the golden treasure chest! You win!")
            break
        elif player_x == trap_x and player_y == trap_y:
            print("BOOM! You stepped on a hidden landmine trap! Game Over.")
            break

if __name__ == "__main__":
    play_game()
