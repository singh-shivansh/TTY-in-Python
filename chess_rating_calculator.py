def elo_rating_calc():
    total_games = int(input('Total number of games: '))
    wins = 0
    loss = 0
    draw = 0
    total_opponent_rating = 0

    for _ in range(total_games):
        opponent_rating = int(input('Opponents rating: '))
        result = str(input('Outcome of the match(win/Loss/Draw): '))
    
        if result == 'win':
            wins = wins + 1
        elif result == 'Loss':
            loss = loss + 1
        else:
            draw = draw + 1
        
        total_opponent_rating = total_opponent_rating + opponent_rating

    elo_rating = int((total_opponent_rating + 400 * (wins - loss)) / total_games)
    print(elo_rating)

elo_rating_calc()