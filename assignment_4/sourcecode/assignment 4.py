#RICKY NANEY
#CS101L ASSIGNMENT 4

import random
def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        play = input("Play again? y or n?")
        if play == "YES" or "y":
            return True
            break
        elif play == "NO" or "n":
            play_again
    
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    bank = int(input('What is your wager?\n'))
    while bank >= 0:
        if bank <= 0:
            print('Value too low')
        else:
            break 
    return bank   

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        x = (wager * 10) - wager
    elif matches == 2:
        x = (wager * 3) - wager
    elif matches == 0:
        x = wager - wager - wager
    return wager * -1     
               

def get_slot_results():
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)
    return reel1, reel2, reel3

def get_matches(reel1, reel2, reel3) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    matches = 0
    if reel1 == reel2:
        matches += 2
        if reel1 == reel3:
            matches += 1
    elif reel1 == reel3:
        matches =+ 2
        if reel1 == reel2:
            matches += 1
    elif reel2 == reel3:
        matches += 2
        if reel2 == reel1:
            matches += 1
    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    num = 0
    while num == 0:
        bank=int(input("How many chips?\n"))
        if bank<=0:
            print("Too low, must be more than 0")
        elif bank >100:
            print("Too high, must be less than 100")
        elif bank>0 and bank<=100:
            return bank
            break


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()