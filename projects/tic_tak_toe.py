
def main():
    squares = [' ']*9
    players = 'XO'
    board = '''
      0   1   2
      {0} | {1} | {2}
     -----------
    3 {3} | {4} | {5} 5
     -----------
      {6} | {7} | {8}
      6   7   8
    '''
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    def check_win(player):
        for a, b, c in win_conditions:
            if {squares[a], squares[b], squares[c]} == {player}:
                return True

    while True:
        print(board.format(*squares))
        if check_win(players[1]):
            print(f'{players[1]} is the winner.')
            break
        if ' ' not in squares:
            print("Its a tie!")
            break
        move = input(f'{players[0]} to move from 0-8 > ')

        if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
            print("Invalid move!")
            continue
        squares[int(move)] = players[0]
        players = players[::-1]
    play_again()

def play_again():
    play_again = input("Do you want to continue the game? (y/n) : ")
    if play_again.lower() == 'y':
        main()
    else:
        print("Goodbye!")

def welcome():
    print("Welcome to Tic Tac Toe!\n")
    print("Kindly bring your friend to play with you.\n")
    print("Let's start the game. choose (s) to start the game.\n")
    choice = input("Enter (s) to start the game: ")
    if choice.lower() == 's':
        main()
    else:
        print("Invalid choice enter only (s).\n\n")
        welcome()


welcome()
    

