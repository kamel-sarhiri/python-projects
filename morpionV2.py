# fonction pour le morpion

def lependu(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# fonction pour afficher le score
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCORE             ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# fonction pour vérifier si le playeur a gagné
def check_win(player_pos, cur_player):
 
    # les combinaisons gagnantes
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True si un joueur a gagné la partie
            return True
    # Return False si aucun des joueurs a fait rentré une des combinaison gagnée      
    return False       
 
# focntion pour vérifier si cr'est un match nul
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# focntion pour un jeu
def single_game(cur_player):
 
    values = [' ' for x in range(9)]
     
    player_pos = {'X':[], 'O':[]}
     
    while True:
        lependu(values)
         
        try:
            print("Joueur ", cur_player, " tour. Quelle case? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Mauvaise entrée!!! Réessaye")
            continue
 
        if move < 1 or move > 9:
            print("Mauvaise entrée!!! Réessaye")
            continue
 
        if values[move-1] != ' ':
            print("Place déjà remplie. Réessaye!!")
            continue
 
        values[move-1] = cur_player
 
        player_pos[cur_player].append(move)
 
        if check_win(player_pos, cur_player):
            lependu(values)
            print("Joueur ", cur_player, " a gagné la partie!!")     
            print("\n")
            return cur_player
 
        if check_draw(player_pos):
            lependu(values)
            print("Match nul")
            print("\n")
            return 'D'
 
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Joueur 1")
    player1 = input("Entrer le nom : ")
    print("\n")
 
    print("Joueur 2")
    player2 = input("Entrer le nom : ")
    print("\n")

    cur_player = player1
 
    player_choice = {'X' : "", 'O' : ""}
 
    # ça enregistre les options
    options = ['X', 'O']
 
    # stocker le score
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # loop pour le jeu
    # la loop continue jusqu'a ce que le joueur choisit quitter
    while True:
 
        # joueur choisi le symbole pour jouer
        print("Le tour pour choisir pour ", cur_player)
        print("Entrer 1 pour X")
        print("Entrer 2 pour O")
        print("Entrer 3 pour quitter")
 
        
        try:
            choice = int(input())   
        except ValueError:
            print("Mauvaise entrée!!! Réessaye\n")
            continue
 
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Le score final")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Mauvais choix!!!! Réessaye\n")
 
        
        winner = single_game(options[choice-1])
         
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # switcher entre les joueurs
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1