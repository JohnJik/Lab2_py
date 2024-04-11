def check_winner():
    for i in range(0, 3):
        if play_map[i] == play_map[i + 3] == play_map[i + 6] != def_map_value:
            return True
        if play_map[i * 3] == play_map[i * 3 + 1] == play_map[i * 3 + 2] != def_map_value:
            return True
    if play_map[0] == play_map[4] == play_map[8] != def_map_value or play_map[2] == play_map[4] == play_map[
        6] != def_map_value:
        return True
    return False


def check_tie():
    return def_map_value not in play_map


v_line = "|"
h_line = "___________________\n"
def_value = "."
def_map_value = "_"
row = f"{v_line}  {def_value}  {v_line}  {def_value}  {v_line}  {def_value}  {v_line}  \n"
cells = f"{h_line}{row}"
board = 3 * cells + h_line
X = 'X'
O = '0'
play_map = [def_map_value, def_map_value, def_map_value, def_map_value, def_map_value, def_map_value, def_map_value,
            def_map_value, def_map_value]
players = ['X', '0']
index = [0, 0, 0, 0, 0, 0, 0, 0, 0]
b = 0
for i in range(len(board)):
    if board[i] == def_value:
        index[b] = i
        b = b + 1

while True:
    for current_player in players:
        print(board)
        print("Гравець", current_player)
        value = int(input("Введіть номер 1 - 9")) - 1

        if 0 <= value <= 8 and play_map[value] == def_map_value:
            play_map[value] = X if current_player == 'X' else O
            board = board[:index[value]] + play_map[value] + board[index[value] + 1:]
            if check_winner():
                print(board)
                print("Гравець", current_player, "Перемагає!")
                exit()
            elif check_tie():
                print(board)
                print("Нічия!")
                exit()
        else:
            print("Некоректний ввід. Спробуйте ще раз.")