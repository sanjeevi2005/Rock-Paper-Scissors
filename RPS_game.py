import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
        elif (p1_play == "P" and p2_play == "R") or \
             (p1_play == "R" and p2_play == "S") or \
             (p1_play == "S" and p2_play == "P"):
            results["p1"] += 1
        else:
            results["p2"] += 1

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    win_rate = results["p1"] / num_games * 100
    print(f"Final results: {results}")
    print(f"Player 1 win rate: {win_rate}%")
    return win_rate

def quincy(prev_play):
    counter = getattr(quincy, "counter", -1)
    quincy.counter = counter + 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[quincy.counter % len(choices)]

def mrugesh(prev_opponent_play, opponent_history=[]):
    # Fix: if it's the first move, just pick a default
    if not prev_opponent_play:
        return "R"
    
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[most_frequent]
def kris(prev_opponent_play):
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prev_opponent_play] if prev_opponent_play else "R"

def abbey(prev_opponent_play, opponent_history=[], play_order=[{}]):
    if not prev_opponent_play: opponent_history.clear()
    opponent_history.append(prev_opponent_play)
    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] = play_order[0].get(last_two, 0) + 1
    potential_next = ["".join([prev_opponent_play, "R"]), "".join([prev_opponent_play, "P"]), "".join([prev_opponent_play, "S"])]
    prediction = max(potential_next, key=lambda key: play_order[0].get(key, 0))[-1]
    return {"P": "S", "R": "P", "S": "R"}[prediction]