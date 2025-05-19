#  SPIN SLOT MACHINE 
import random


def spin():
    items = ['cherry', 'lemon', 'orange', 'plum', 'bell', 'bar']
    return random.choice(items)

def main():
    while True:
        spins = [spin() for _ in range(3)]
        print("Spun:", spins)
        
        if spins[0] == spins[1] == spins[2]:
            print("Triple price!")
        elif spins[0] == spins[1] or spins[1] == spins[2] or spins[0] == spins[2]:
            print("Double price!")
        else:
            print("Remain same.")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
