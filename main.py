"""This program is designed to help understand the paper, and simulate games from,
'Markov Models For The Tipsy Cop And Robber Game On Graphs.' """
__author__ = "Vincent Ciarcia"

import random
from PIL import Image


def header():
    """
    The first function to be run when the program runs.
    """
    print("\n \n This Project is in reference to the", end=" ")
    print("paper titled: \n 'Markov Models For The Tipsy Cop And Robber", end=" ")
    print("Game On Graphs.'")
    main()


def main():
    """
    Main menu
    """
    print("-------------------------------------------------------------")
    print("Please choose from the following options as needed:          |")
    print("1. What is the Tipsy Cop and Robber Game?                    |")
    print("2. What are cycle graphs?                                    |")
    print("3. Can I read the whole paper?                               |")
    print("4. Mathematical Model Predictions.                           |")
    print("5. Simulate games on cycle graphs.                           |")
    print("6. Quit.                                                     |")
    print("-------------------------------------------------------------")
    selection = input("Please Enter Only The Number of Your Selection: ")
    try:
        int(selection)
    except ValueError:
        print("\n \n Please Enter A Valid Selection. \n")
        main()
    if int(selection) == 1:
        desc_game()
    elif int(selection) == 2:
        desc_cycles()
    elif int(selection) == 3:
        whole_paper()
    elif int(selection) == 4:
        math_model()
    elif int(selection) == 5:
        simulate_initialize()
    elif int(selection) == 6:
        print("\n \nThanks! Have a great day!")
        quit()
    else:
        print("\n \n That sure was an integer! Just not a valid one. \n")
        main()


def math_model():
    """
    A description of the mathematical model
    """
    print("\n \n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Mathematical Model Predictions \n")
    print("For the inner workings of the mathematical model of the Tipsy Cop and Robber Game, please see section 4\n"
          "of the paper. A picture will open showing the Expected Game Time 'E(d)' and probability the robber is\n"
          "still free after 7 rounds 'G7(d)' on a Six-Node Cycle Graph, given various values for c, r, and t=0.5.\n"
          "Where d is the distance between the two players at the start of the game. It makes sense that the further\n"
          "apart they start, the longer the game is expected to last and the more likely the robber is to survive at\n"
          "least 7 rounds. \n \n")
    print("So for example, for the G7(3) row and r=0.2, c=0.3 column, the intersection is 0.402. That means given\n"
          "r=0.2 and c=0.3, if the players start 3 spaces away (the maximum available for a six-node cycle graph)\n"
          "there is a 40.2% chance the robber will still be free after 7 rounds.")
    print("For the same column but for the E(2) row, the intersection is 6.98. That means given r=0.2 and c=0.3,\n"
          "if the players start 2 spaces away the game is expected to last on average 6.98 rounds.")
    print("Obviously not every game with those exact conditions will last 6.98 rounds. That is only the expected\n"
          "average number of rounds after playing many games. Fortunately, it seems you've found a program that can\n"
          "simulate these games (or you are Professor Vanselow and you're grading this). Should the math model be\n"
          "accurate, as you simulate more and more games the average length of each game should converge to the\n"
          "prediction made by the math model.")
    print("\n For clarification, 'two spaces away means there exists a single vertex between the players on the\n"
          "shortest path between the players. That way is would take the cop 2 sober turns to catch the robber,\n"
          "one to move to the vertex between them, and one more to move on top of the robber. So, 'three spaces away'\n"
          "means there exists exactly two vertices between the players along the shortest path between the players,\n"
          "and so on...")
    print("----------------------------------------------------------------------------------------------------------")
    try:
        im = Image.open(r"DATA.png")
        im.show()
    except FileNotFoundError:
        print("\n'DATA.png' not found. Make sure it's in the same directory as 'main.py'")
    print("\n \n")
    main()


def whole_paper():
    """
    Information about Markov Models For The Tipsy Cop And Robber Game On Graphs.
    """
    print("\n \n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Of course you can read the whole paper! It's free and available online at: \n"
          "https://arxiv.org/abs/2102.13532")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n \n")
    main()


def desc_cycles():
    """
    Description of Cycle Graphs
    """
    print("\n \n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Cycle Graphs are essentially the perimeter of any regular polygon. \n"
          "That is, a cycle graph with three nodes is the perimeter of a regular triangle where there vertices of the\n"
          "graph are the vertices of the triangle. Similarly, a cycle graph with six nodes is the set of vertices of\n"
          "a regular hexagon. A picture should open with examples of a six-node cycle graph and the players at\n"
          "various vertices. Cop = Blue, Robber = Red.")
    print("----------------------------------------------------------------------------------------------------------")
    try:
        im = Image.open(r"SixNodeGraph.JPG")
        im.show()
    except FileNotFoundError:
        print(" \n'SixNodesGraph.JPG' not found. Make sure it's in the same directory as 'main.py'")
    print("\n \n")
    main()


def desc_game():
    """
    Description of the tipsy cop and robber game
    """
    print("\n \n")
    print("----------------------------------------------------------------------------------------------------------")
    print("The Tipsy Cop and Tipsy Robber Game on Graphs goes as follows: \n")
    print("Two players, a cop and a robber are placed on a graph, this graph could be a gird, or the perimeter of\n"
          "a regular polygon, or any set of vertices. The cop is trying to catch the robber and the robber is\n"
          "trying to evade the cop. The cop and robber can only move to adjacent vertices. Yet, they're both a\n"
          "little tipsy, so a certain portion of their moves will be entirely at random. To determine this\n"
          "portion, prior to start of the game, three variables are set. The first, 'c' is the percentage OF ALL\n"
          "MOVES IN THE GAME that will be SOBER cop moves, and when the cop moves soberly they move to best catch\n"
          "the robber. Next, 'r' is the percentage OF ALL MOVES IN THE GAME that will be SOBER robber moves,\n"
          "and when the robber moves soberly they move to best evade the cop (which is sometimes not to move at\n"
          "all). Finally, 't' is the percentage OF ALL MOVES IN THE GAME that are TIPSY RANDOM MOVES by EITHER PLAYER\n"
          "is set to be 1 - c -r. The reason a single variable is sufficient to cover both players has to do with the\n"
          "game only being played on something called 'vertex transitive graphs' the definition of which is\n"
          "essentially: no matter where you stand in the graph, it always looks the same. That part isn't so\n"
          "important as much as trusting us that t=0.2 means the next move has a 20% chance to be a tipsy RANDOM move\n"
          "by either player. Similarly, r=0.5 means the next move has a 50% chance of being a SOBER robber move,\n"
          "and c=0.3 means the next move has a 30% chance of being a SOBER cop move. The user is free to set these\n"
          "variables to any values they like, but they must sum to 1. The last important rule is that when either\n"
          "player is moving tipsily they have to move; they can't not move.")
    print("----------------------------------------------------------------------------------------------------------")
    print("\n \n ")
    main()


def simulate_initialize():
    """
    Collects input from user to set variables.
    """
    print("\n \n")
    print("----------------------------------------------------------------------------------------------------------")
    print("c - % of all moves that are sober cop moves \nr - % of all moves that are sober robber moves")
    print("t - % of all moves that are tipsy random moves by either player.")
    print("t = 1 - c - r")
    print("It must be that: 0 <= c+r <= 1")
    print("----------------------------------------------------------------------------------------------------------")
    robber = input("Enter a decimal value for r: ")
    cop = input("Enter a decimal value for c: ")
    nodes = input("Enter a positive whole number value for the number of nodes in the cycle graph: ")
    print("Selecting y to the following implies only one game will be simulated:")
    turn_by_turn = input("Do you want a description of what happened at each turn? (y/n) ")
    if turn_by_turn == "y":
        num_games1 = 1
    elif turn_by_turn == "n":
        num_games1 = input("Enter a positive whole number to be the number of games to simulate: ")
        try:
            int(num_games1)
            if int(num_games1) < 1:
                print("\n \n Must be a positive whole number")
                simulate_initialize()
        except ValueError:
            print("\n \n Must be a positive whole number")
            simulate_initialize()
    else:
        print("\n \n Please enter either 'y' or 'n' only.")
        simulate_initialize()
        num_games1 = 1
    try:
        tipsy = 1 - float(cop) - float(robber)
        if int(nodes) < 3:
            print("\n \n Number of Nodes must be at least 3. \n \n")
            simulate_initialize()
        if tipsy < 0:
            print("\n \n It must be that c + r <= 1 \n \n")
    except ValueError:
        print("\n \n One or More Invalid Entries")
        simulate_initialize()
    print("Possible Starting Distances: 0-", int(nodes) // 2, sep='', end=' ')
    print("Must be a whole number.")
    start_distance = input("Please enter the starting distance between the players: ")
    try:
        if int(start_distance) < 0 or int(start_distance) > int(nodes) // 2:
            print("\n \n Starting Distances Must Be: 0-", int(nodes) // 2, sep='', end="\n \n")
            simulate_initialize()
    except ValueError:
        print("Must be a whole number from 0 through", int(nodes) // 2)
        simulate_initialize()
    robber_start_position = 0
    cop_start_position = robber_start_position + int(start_distance)  # Set start positions
    simulate_games(float(cop), float(robber), int(nodes), turn_by_turn, int(num_games1), robber_start_position,
                   cop_start_position)
    # Time to simulate!


def simulate_games(c, r, n, turn_by_yn, num_games, robber_start_pos, cop_start_pos):
    """
    Where simulation of the game happens.
    :parameter c - (Float) % of moves that will be sober cop moves
    :parameter r - (Float) % of moves that will be sober robber moves
    :parameter n - (INT) value of number of nodes in cycle graph
    :parameter turn_by_yn - (String) 'y' or 'n' referring to turn descriptions
    :parameter num_games - (INT) number of games to simulate
    :parameter robber_start_pos - (INT) value of node robber starts on
    :parameter cop_start_pos - (INT) value of node cop starts on
    """

    cap = 1000  # This variable is basically the "fineness" of the random number generation.
    #            Higher is better, MUST BE A MULTIPLE OF 10.
    if cap % 10 != 0:
        print(" \n \nSorry, a programmer made a mistake. Tell them to fix it and that they should feel bad. I mean,\n"
              "did they not see the caps lock in the comments on line 220?")
        quit()
    total_time = 0  # Total number of rounds played
    dis_pos = []  # Initialization of list that will later hold all possible distances
    if turn_by_yn == "y":
        turn_desc = True
    else:
        turn_desc = False

    for i in range(1, num_games + 1, 1):
        game_time = 0  # Reset current round counter
        cop_current_pos = cop_start_pos  # Reset Cop Current position
        robber_current_pos = robber_start_pos  # Reset Robber Current position
        # New Game
        dis = 1  # just making it > 0 so the next game will start
        while dis > 0:
            robber_current_negative = robber_current_pos - n  # Set Robber Current position (negative)
            cop_current_negative = cop_current_pos - n  # Set Cop Current position (negative)
            dis_pos.append(abs(cop_current_pos - robber_current_pos))  # 1st distance possibility
            dis_pos.append(abs(cop_current_negative - robber_current_pos))  # 2nd distance possibility
            dis_pos.append(abs(robber_current_negative - cop_current_pos))  # 3rd distance possibility
            # Lines 230 through 234 determine which of the three possible distances is the smallest
            minn = dis_pos[0]
            for ii in range(1, 3, 1):
                if dis_pos[ii] < minn:
                    minn = dis_pos[ii]
            dis = minn  # Setting distance
            if turn_desc and game_time == 0:
                print("Starting distance is: ", dis)
            dis_pos = []  # Reset distance possibilities list
            if turn_desc and game_time > 0:
                print("Distance:", dis, "\n---------------")
            if dis == 0:  # Game over
                print("Game", i, " lasted:", game_time, "rounds.")
                total_time += game_time
                break
            game_time += 1
            # Moving on to the next round
            # choose c r or t
            x = random.randint(1, cap)  # Choose a random number
            if x <= cap * c:  # Sober Cop Move
                if dis == n / 2:  # Move randomly as any move is beneficial
                    y = random.randint(1, cap)
                    if y <= 0.5 * cap:
                        cop_current_pos = (cop_current_pos + 1) % n
                    else:
                        cop_current_pos = (cop_current_pos - 1) % n
                else:
                    # Decide which way is the shortest path to the robber
                    test_dis = (cop_current_pos + dis) % n  # Test moving forward
                    if test_dis == robber_current_pos:  # Do you land on the robber?
                        cop_current_pos = (cop_current_pos + 1) % n  # If yes, move forward
                    else:  # Otherwise,
                        cop_current_pos = (cop_current_pos - 1) % n  # Move backwards
                if turn_desc:
                    print("Cop moves soberly to", cop_current_pos)

            elif cap * c < x <= cap * c + cap * r:  # Sober robber move
                if dis == n / 2:  # Do not move as any move is hurtful
                    robber_current_pos = robber_current_pos
                else:
                    # decide which way to go
                    test_dis = (robber_current_pos + dis) % n  # Test moving forward
                    if test_dis == cop_current_pos:  # Do you land on the cop?
                        robber_current_pos = (robber_current_pos - 1) % n  # if yes, move backwards.
                    else:  # otherwise,
                        robber_current_pos = (robber_current_pos + 1) % n  # move forward.
                if turn_desc:
                    print("Robber moves soberly to", robber_current_pos)
            else:
                y = random.randint(1, cap)  # Tipsy move by either player, choose another random number
                if y <= 0.5 * cap:  # decide who to give the move to
                    # give to robber
                    test_dis = (robber_current_pos + dis) % n  # Calculate test moving forward
                    mover = "Robber"  # note who is moving
                    if y <= 0.25 * cap:  # make the tipsy move good for the robber
                        # Note: this is essentially a sober robber move. Unless the robber is on n/2, as the optimal
                        # move is to not move, but since the robber is tipsy, they have to move per the rules of
                        # the game.
                        if n % 2 == 0:
                            favor = "Cop"
                        else:
                            favor = "Robber"
                        if test_dis == cop_current_pos:  # Test moving forward, land on cop?
                            robber_current_pos = (robber_current_pos - 1) % n  # If yes, move backwards
                        else:
                            robber_current_pos = (robber_current_pos + 1) % n  # otherwise move forward
                    else:  # make robber move in favor of cop
                        favor = "Cop"
                        if test_dis == cop_current_pos:  # Test moving forward. land on cop?
                            robber_current_pos = (robber_current_pos + 1) % n  # If yes, move forward.
                        else:
                            robber_current_pos = (robber_current_pos - 1) % n  # otherwise move backward
                else:
                    # give to cop
                    mover = "Cop"  # note who is moving
                    test_dis = (cop_current_pos + dis) % n
                    if y <= 0.75 * cap:  # Make cop move in their favor
                        favor = "Cop"
                        if test_dis == robber_current_pos:
                            cop_current_pos = (cop_current_pos + 1) % n
                        else:
                            cop_current_pos = (cop_current_pos - 1) % n
                    else:
                        favor = "Robber"  # Make cop move in favor of robber
                        if test_dis == robber_current_pos:
                            cop_current_pos = (cop_current_pos - 1) % n
                        else:
                            cop_current_pos = (cop_current_pos + 1) % n
                if turn_desc:
                    if mover == "Cop":
                        moved = cop_current_pos
                    else:
                        moved = robber_current_pos
                    print("Tipsy", mover, "moved in favor of", favor, "to", moved)
    # OUT OF THE FOR LOOP
    print("\n Finished!")
    print("Conditions: r =", r, "| c =", c, " | t =", 1 - r - c)
    print(total_time, "rounds simulated over", num_games, "games.")
    print("Average length of each game:", calc_average(total_time, num_games), "rounds.")
    main()


def calc_average(total_time, num_games):  # This is pretty much just to show I understand value returning functions
    """Calculate Average length of each game"""
    avg = total_time / num_games
    return avg


header()
