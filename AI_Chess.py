import chess
import math

# Piece values used for evaluation
PIECE_VALUES = {
    'p': 1,   
    'n': 3,   
    'b': 3,   
    'r': 5,  
    'q': 9,   
    'k': 0    
}

def evaluate_board(board):
    """
    Evaluates the material score of the board.
    Positive values favor White; negative values favor Black.
    """
    score = 0
    for piece in board.piece_map().values():
        value = PIECE_VALUES[piece.symbol().lower()]
        score += value if piece.color == chess.WHITE else -value
    return score

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    """
    Alpha-Beta Pruning recursive search.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

def get_best_move(board, depth):
    """
    Returns the best move using Alpha-Beta search for the current player.
    """
    best_move = None
    best_value = -math.inf if board.turn == chess.WHITE else math.inf

    for move in board.legal_moves:
        board.push(move)
        board_value = alpha_beta(board, depth - 1, -math.inf, math.inf, not board.turn)
        board.pop()

        if (board.turn == chess.WHITE and board_value > best_value) or \
           (board.turn == chess.BLACK and board_value < best_value):
            best_value = board_value
            best_move = move

    return best_move

# ---- Main Game Loop ----
def play_game():
    board = chess.Board()
    move_count = 1

    while not board.is_game_over():
        print(board, end="\n\n")
        print(f"Move {move_count}: {'White' if board.turn else 'Black'} to move...")
        
        best_move = get_best_move(board, depth=3)
        board.push(best_move)

        print(f"Move played: {best_move}\n{'-'*40}")
        move_count += 1

    print("Game Over!")
    print(f"Result: {board.result()}")

if __name__ == "__main__":
    play_game()
