from minimax_node import MinimaxNode
import chess

def change(color):
    if color == 'white':
        return 'black'
    else:
        return 'white'


class MinimaxTree():
    def __init__(self, board, color, max_depth):
        self.depth = 0
        self.max_id = 0
        self.max_depth = max_depth
        self.nodes = [MinimaxNode(id=0, color=color, board=board)]
        self.levels = [[0]]

    def go_deeper(self):
        current_level = self.levels[-1]
        new_level = []
        for i in current_level:
            legal_moves = self.nodes[i].get_moves(self.max_id)
            for move in legal_moves:
                new_level.append(move[0])
                self.nodes.append(MinimaxNode(id=move[0], color=change(self.nodes[i].color), board=move[1]))
                self.max_id += 1
        self.depth += 1
        self.levels.append(new_level)

    def build_tree(self):
        while self.depth < self.max_depth:
            self.go_deeper()
            print "depth =", self.depth, ', length =', len(self.levels[-1])

    def evaluate(self):
        #print self.levels[-1]
        for i in self.levels[-1]:
            self.nodes[i].value = self.nodes[i].evaluate()
        #    print i, self.nodes[i].value
        for i in range(self.max_depth-1, 0, -1):
            for j in self.levels[i]:
                if self.nodes[j].color == 'black' and self.nodes[j].children:
                    self.nodes[j].value = min([self.nodes[x].value for x in self.nodes[j].children])
                elif self.nodes[j].color == 'white' and self.nodes[j].children:
                    self.nodes[j].value = max([self.nodes[x].value for x in self.nodes[j].children])
                else:
                    self.nodes[j].value = self.nodes[j].evaluate()

    def choose_best_move(self):
        legal_moves = self.nodes[0].get_moves(0)
        #for i in self.nodes:
        #    print i.value,
        #for i in legal_moves:
        #    print i[1]
        #    print self.nodes[i[0]].value
        #    print
        if self.nodes[0].color == 'white':
            best_value = self.nodes[legal_moves[0][0]].value
            best_move = legal_moves[0][2]
            for move in legal_moves:
                if self.nodes[move[0]].value > best_value:
                    best_value = self.nodes[move[0]].value
                    best_move = move[2]
        else:
            best_value = self.nodes[legal_moves[0][0]].value
            best_move = legal_moves[0][2]
            for move in legal_moves:
                if self.nodes[move[0]].value < best_value:
                    best_value = self.nodes[move[0]].value
                    best_move = move[2]
        return best_move