# This is a player function that will be built to defeat each of the four provided bots.
def player(prev_play, opponent_history=[],
           player_history=[],
           play_order=[{
                         "RR": 0,
                         "RP": 0,
                         "RS": 0,
                         "PR": 0,
                         "PP": 0,
                         "PS": 0,
                         "SR": 0,
                         "SP": 0,
                         "SS": 0,
                     }]):
    # The general strategy should be to make some moves first as a test to see who the
    # player is playing against. Then, the right strategy should be used to beat each one.
    if prev_play:
        opponent_history.append(prev_play)
    elif prev_play == "":
        opponent_history.clear()
        player_history.clear()
        for k in play_order[0]:
            play_order[0][k] = 0
    ideal_move = {'R': 'P', 'P': 'S', 'S': 'R'}

    # Strategy against Kris. At first there is no history, so Kris will use paper,
    # which means that scissors should be used first. On the next move, Kris will use
    # rock, so paper should be used. Afterwards, Kris will use scissors, so rock should
    # be used. Finally, Kris will use paper again, so scissors should be used and then the
    # cycle repeats.

    # Strategy against Abbey. Abbey always starts with paper, just like Kris.
    # To differentiate Abbey from Kris, need the second move. On the second move, Kris will
    # use scissors, but Abbey will use paper.

    # Strategy against Mrugesh. Mrugesh always starts with rock. So, first use paper. His
    # second move will be scissors.

    # Strategy against Quincy. Quincy always starts with rock. So, first use paper. Quincy
    # will then use paper.

    # On the first move, two of the bots use paper and two use rock, so first move should
    # be paper to make either a win or tie.
    if not opponent_history:
        player_history.append('P')
        play_order[0]['RP'] += 1
        return 'P'
    
    elif len(opponent_history) == 1 and opponent_history[0] == 'P':
        # If the bot's move is paper, then the bot is either Kris or Abbey. Kris will use
        # scissors next and Abbey will use paper, so use scissors just to be safe.
        player_history.append('S')
        play_order[0]['PS'] += 1
        return 'S'
    
    elif len(opponent_history) == 1 and opponent_history[0] == 'R':
        # If the move is rock, the bot is either Mrugesh or Quincy. Quincy will use paper
        # and Mrugesh will use scissors. So, use scissors here to be safe.
        return 'S'
    
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "PS":
        # This means the bot is Kris, who always counters the opponent's last move. Kris' 
        # last move was scissors, but the player used scissors as well. This means that 
        # his third move will be rock, and the player should use paper. Then, Kris will use
        # scissors, so player should use rock. After, Kris will use paper, so player should
        # use scissors. The sequence is, therefore, rock, scissors, paper.
        moveset = ['R', 'S', 'P']
        return moveset[len(opponent_history) % 3]
    
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "PP":
        # This means the bot is Abbey. On the first move, Abbey assumes the player's
        # imaginary last move is rock. She then looks at possibilities RR, RP, and RS.
        # She compares each possibility to the number of times it appeared in her
        # play_order list, then takes the last move of that possibility and counters it.
        # Therefore, she will first think that the player will choose rock, but the player
        # will choose paper. Then, she will store the RP sequence in her play_order list.
        # She will then look at possibilities PR, PP, PS. To beat her, the player needs to
        # store his own list that reflects what Abbey stores, so make a play_order param.
        # Abbey's next move will be paper again.
        
        potential_plays = [
            player_history[-1] + "R",
            player_history[-1] + "P",
            player_history[-1] + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]
        abbey_response = ideal_move[prediction]
        player_response = ideal_move[abbey_response]
        play_order[0]["".join([player_history[-1], player_response])] += 1
        player_history.append(player_response)
        return player_response
    
    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "RP":
        # This means the bot is Quincy. He is easy to counter because he always plays
        # RPPSR, so the right moves would be PSSRP in that order.
        quincy_counter = ['P', 'S', 'S', 'R', 'P']
        return quincy_counter[len(opponent_history) % 5]

    elif len(opponent_history) > 1 and "".join(opponent_history[0:2]) == "RS":
        # This means the bot is Mrugesh.
        pass
