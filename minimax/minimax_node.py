import chess


PRICES = {'p': -1,
          'r': -5,
          'n': -3,
          'b': -3,
          'q': -10,
          'P': 1,
          'R': 5,
          'N': 3,
          'B': 3,
          'Q': 10}


def get_targets(mask):
    targets = []
    for i in range(64):
        if i in mask:
            targets.append(i)
    return targets


def get_symbols(board, positions):
    raw_figures = [board.piece_at(j) for j in positions]
    figures = []
    for fig in raw_figures:
        if fig is None:
            figures.append('.')
        else:
            figures.append(fig.symbol())
    return figures


def get_all_attacks(board):
    attacks = []
    for i in range(64):
        figure = board.piece_at(i)
        if figure is None:
            pass
        else:
            figure = figure.symbol()
            targets = get_symbols(board, get_targets(board.attacks(i)))
            for t in targets:
                if figure not in 'Kk' and t not in 'Kk':
                    attacks.append([figure, t])
    return attacks


class MinimaxNode():
    def __init__(self, id, color, value=0, board=None):
        self.id = id
        self.color = color
        self.value = value
        self.board = board
        self.children = []

    def get_moves(self, max_id):
        self.children = []
        id = max_id+1
        to_create = []
        for i in self.board.legal_moves:
            new_board = self.board.copy()
            new_board.push(i)
            to_create.append([id, new_board, i])
            self.children.append(id)
            id += 1
        return to_create

    def evaluate(self, prices=PRICES, count_figures=True, count_attacks=True, count_pos=True):
        value = 0
        if count_figures:
            text = str(self.board)
            text = text.replace(' ', '')
            text = text.replace('\n', '')
            for fig in prices:
                value += prices[fig]*text.count(fig)

        if count_attacks:
            attacks = get_all_attacks(self.board)
            for attack in attacks:
                figure, target = attack
                clr = prices[figure]/abs(prices[figure])
                if count_pos and target == '.':
                    value += 0.5 #*clr*abs(prices[figure])**0.5
                elif target != '.':
                    if abs(prices[figure]) <= abs(prices[target]):
                        value += abs(prices[target])*clr


        if self.board.is_check():
            if self.color == 'white':
                value -= 10
            else:
                value += 10

        if self.board.is_stalemate():
            value = 0

        if self.board.is_checkmate():
            if self.color == 'white':
                value = -1000
            else:
                value = 1000
        return value