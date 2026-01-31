def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        opponent_history.clear()
        play_order.clear() # This is the "Abbey-fix"
        return "R"

    opponent_history.append(prev_play)
    prediction = "P" # Default
    
    # n=2 or 3 works best to keep enough data samples for Abbey
    n = 3

    if len(opponent_history) > n:
        pattern = "".join(opponent_history[-n:])
        last_sequence = "".join(opponent_history[-(n+1):-1])
        play_order[last_sequence + prev_play] = play_order.get(last_sequence + prev_play, 0) + 1
        
        potential_next = [pattern + "R", pattern + "P", pattern + "S"]
        prediction = max(potential_next, key=lambda key: play_order.get(key, 0))[-1]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]