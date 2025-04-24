import random
# rock paper scissor game
def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'you won 🎉🎉'
    
    return 'you lost! 💀💀'

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
def main():
    print(play())

if __name__ == "__main__":
    main()



    

