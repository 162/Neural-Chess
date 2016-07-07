from minimax.minimax_node import MinimaxNode
from minimax.minimax_tree import MinimaxTree, change
import chess


def play(board, move):
    print move
    board.push(move)
    if board.is_check():
        print "CHECK"
    print board

b = chess.Board()
#move = raw_input() # #if player is white
#play(b, move)
color = 'white'
while not b.is_game_over():
    tree = MinimaxTree(board=b, color=color, max_depth=4)
    tree.build_tree()
    tree.evaluate()
    move = tree.choose_best_move()
    play(b, move)
    move = raw_input('your turn:  ')
    move = chess.Move.from_uci(move)
    play(b, move)
