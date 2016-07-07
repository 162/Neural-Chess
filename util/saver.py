def prepare(board):
    text = str(board)
    text = text.replace(' ', '')
    text = text.replace('\n', '')
    return text


def save_csv(lines, dest):
    text = 'id,in,out'
    i = 0
    for line in lines:
        text += '\n'+str(i)+','+line[0]+','+line[1]
        i += 1
        if i % 100000 == 0:
            print '|',
    #print 'saving'
    f = open(dest, 'w')
    f.write(text)
    f.close()


def load_array(filename):
    f = open(filename, 'r')
    lines = f.read().split('\n')
    f.close()
    moves = [i.split(',')[1:] for i in lines[1:]]
    return moves


def reshape(filenames, pack_prefix, pack_size):
    moves = []
    no = 1
    for i in range(len(filenames)):
        moves += load_array(filenames[i])
        while len(moves) >= pack_size:
            save_csv(moves[:pack_size], pack_prefix+str(no)+'.csv')
            print 'Formed pack no:', no, 'of', pack_size, 'moves'
            no += 1
            moves = moves[pack_size:]
    if moves:
        save_csv(moves, pack_prefix+str(no)+'.csv')
        no += 1
        print 'Formed pack no:', no, 'of', len(moves), 'moves'
        del moves
    print 'FINISHED'