# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # The general strategy should be to make some moves first as a test to see who the
    # player is playing against. Then, the right strategy should be used to beat each one.
    if prev_play:
        opponent_history.append(prev_play)
    ideal_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

    # Strategy against Kris. At first there is no history, so Kris will use paper,
    # which means that scissors should be used first. On the next move, Kris will use
    # rock, so paper should be used. Afterwards, Kris will use scissors, so rock should
    # be used. Finally, Kris will use paper again, so scissors should be used and then the
    # cycle repeats.

    # Strategy against Abbey. Abbey always starts with paper, just like Kris.
    # To differentiate Abbey from Kris, need the second move. On the second move, Kris will
    # use scissors, but Abbey will use rock.

    # Strategy against Mrugesh. Mrugesh always starts with rock. So, first use paper. His
    # second move will be scissors.

    # Strategy against Quincy. Quincy always starts with rock. So, first use paper. Quincy
    # will then use rock again.

    # On the first move, two of the bots use paper and two use rock, so first move should
    # be paper to make either a win or tie.
    if not opponent_history:
        return 'P'
    elif len(opponent_history) == 1 and opponent_history[0] == 'P':
        # If the move is paper, then the bot is either Kris or Abbey. Kris will use
        # scissors next and Abbey will use rock, so use rock just to be safe.
        return 'R'
    elif len(opponent_history) == 1 and opponent_history[0] == 'R':
        # If the move is rock, the bot is either Mrugesh or Quincy. Quincy will use rock
        # again and Mrugesh will use scissors. So, use rock here to be safe.
        return 'R'
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "PS":
        # This means the bot is Kris, who always counters the opponent's last move. If
        # Kris' last move was paper, then the player played scissors. This means that his
        # third move will be rock, so player should use paper. The sequence is, therefore
        # rock, scissors, paper to win almost every time.
        moveset = ['R', 'S', 'P']
        return moveset[len(opponent_history) % 3]
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "PR":
        # This means the bot is Abbey. 
        pass
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "RR":
        # This means the bot is Quincy.
        pass
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "RS":
        # This means the bot is Mrugesh.
        pass
