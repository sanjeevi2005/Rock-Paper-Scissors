def player(prev_play, opponent_history=[], play_order={}):
    # 1. Reset state for a new match
    if not prev_play:
        opponent_history.clear()
        play_order.clear() 
        return "R"

    opponent_history.append(prev_play)
    
    # We need n moves to start building a pattern
    n = 3 
    prediction = "R" # Default

    if len(opponent_history) > n:
        # Define the current pattern (the moves leading up to now)
        pattern = "".join(opponent_history[-n:])
        
        # Define the previous pattern (the moves leading up to the previous turn)
        # We record what the opponent played (prev_play) after that previous pattern
        prev_pattern = "".join(opponent_history[-(n+1):-1])
        
        # Store the occurrence in the dictionary
        play_order[prev_pattern + prev_play] = play_order.get(prev_pattern + prev_play, 0) + 1
        
        # Now, look at the current pattern and find which of R, P, or S 
        # is most likely to follow it based on our history
        potential_next = [pattern + "R", pattern + "P", pattern + "S"]
        
        # Select the predicted move with the highest frequency
        prediction = max(potential_next, key=lambda key: play_order.get(key, 0))[-1]

    # 2. Counter the prediction
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    return ideal_response[prediction]