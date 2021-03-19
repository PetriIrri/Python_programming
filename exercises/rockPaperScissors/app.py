from humanPlayer import HumanPlayer
from cpuPlayer import CPUPlayer

def main():
    print("Welcome to rock paper scissors!")
    # Ask player for name and create player object
    player = HumanPlayer(input("Please give your name: "))
    # Crete cpu object
    cpu = CPUPlayer("Tietokone")
    # Store the moves as string list
    moves = ["Rock", "Paper", "Scissors"]
    
    while True:
        # Ask the player for his choise and generate one for cpu
        playerChoice = player.play()
        cpuChoice = cpu.play()
        # Print the moves
        print(player.name, moves[playerChoice - 1])
        print(cpu.name, moves[cpuChoice - 1])
        # check who won
        if playerChoice == cpuChoice:
            print("Draw!")
        # Check if player lost. 1 = Rock, 2 = Paper, 3 = Scissors
        elif playerChoice + 1 == cpuChoice or playerChoice - 2 == cpuChoice:
            print("You lost!")
        else:
            print("You win!")

        if input("Continue? y / n\n") == "n":
            break
    print("The game has ended.")

if __name__ == "__main__":
  main()