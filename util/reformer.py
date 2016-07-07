def common_prefix(a, b):
    i = 1
    prefix = ''
    while a[:i] == b[:i]:
        prefix = a[:i]
        i += 1
    return prefix


def common_suffix(a, b):
    i = -1
    suffix = ''
    while a[i:] == b[i:]:
        suffix = a[i:]
        i -= 1
    return suffix


def get_move(start, end):
    pref = common_prefix(start, end)
    suff = common_suffix(start, end)
    fig = '0'*len(pref)+'1'+'0'*(63-len(pref))
    dest = '0'*(63-len(suff))+'1'+'0'*len(suff)
    return fig, dest


def reform(board):
    '''prnbqkPRNBQK'''
    rules = {'p': '100000000000',
             'r': '010000000000',
             'n': '001000000000',
             'b': '000100000000',
             'q': '000010000000',
             'k': '000001000000',
             'P': '000000100000',
             'R': '000000010000',
             'N': '000000001000',
             'B': '000000000100',
             'Q': '000000000010',
             'K': '000000000001',
             '.': '000000000000'}
    out = ''
    for i in board:
        out += rules[i]
    return out