def load_games(filename):
    f = open(filename, 'r')
    text = f.readlines()
    f.close()
    games = []
    for i in text:
        if i.startswith('1'):
            games.append(i[:-1])
    del text
    return games


def is_ok(line):
    forbidden = ['{', '}', 'drawn', 'forfeits', 'player', 'ran', 'wins']
    for i in forbidden:
        if line.find(i) > -1:
            return False
    return True



def eat_game(line):
    line = line.split()
    moves = []
    triad = []
    for i in range(len(line)):
        triad.append(line[i])
        if i % 3 == 2:
            moves.append(triad)
            triad = []
    if triad:
        moves.append(triad)
    result = moves[-1][-1]
    if result == '1-0':
        result = 'W'
    elif result == '0-1':
        result = 'B'
    # deleting comments
    if len(moves) > 5:
        if not moves[-1]:
            moves = moves[:-1]
        moves = [i[1:] for i in moves]
        lined_moves = []
        for m in moves:
            lined_moves += m
        #print lined_moves
        for n in range(len(lined_moves)):
            if not is_ok(lined_moves[n]):
                lined_moves = lined_moves[:n]
                break
        #print lined_moves
        lined_moves = [i.rstrip('+#') for i in lined_moves]
        return result, lined_moves
    else:
        return 'failed', []