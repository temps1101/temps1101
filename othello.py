import xml.etree.ElementTree as et
from copy import deepcopy


BLANK = 0
BLACK = 1
WHITE = 2

DIRECTION_N = 0
DIRECTION_NE = 1
DIRECTION_E = 2
DIRECTION_SE = 3
DIRECTION_S = 4
DIRECTION_SW = 5
DIRECTION_W = 6
DIRECTION_NW = 7


def get_board(markdown: str) -> list:
    text_board = markdown.split('<!--board-->')[1]
    root = et.fromstring(text_board)
    board = list()
    for table in root[1]:
        table_list = list()
        for piece in table[1:]:
            img_name = piece[0][0].attrib['src']
            color = BLANK if img_name == 'images/blank.png' else BLACK if img_name == 'images/black.png' else WHITE
            try:
                url = piece[0].attrib["href"]
            except KeyError:
                url = None

            table_list.append({
                'status': color,
                'url': url
            })
        board.append(table_list)

    return board


def write_board(board: list, markdown: str) -> str:
    separated_markdown = markdown.split('<!--board-->')
    board_xml = et.fromstring(separated_markdown[1])

    for row_num, row in enumerate(board):
        for column_num, column in enumerate(row):
            status = column['status']
            img_name = 'images/blank.png' if status == BLANK else 'images/black.png' if status == BLACK else 'images/white.png'
            url = column['url']
            board_xml[1][row_num][column_num + 1][0].attrib = {'href': str(url)}
            board_xml[1][row_num][column_num + 1][0][0].attrib = {'src': str(img_name)}

    separated_markdown[1] = et.tostring(board_xml, encoding='unicode')

    return '\n<!--board-->\n'.join(separated_markdown)


def get_reversed_color(color: int) -> int:
    return BLACK if color == WHITE else WHITE if color == BLACK else None


def place_stone(board: list, stone_color: int, stone_position: list) -> list:
    x, y = stone_position
    board[y][x]['status'] = stone_color


def get_stone_color(board: list, stone_position: list) -> list:
    x, y = stone_position
    return board[y][x]['status']


def update_position(position: list, direction: int) -> list:
    position_ = deepcopy(position)

    if direction == DIRECTION_N:
        position_[1] -= 1

    if direction == DIRECTION_NE:
        position_[0] += 1
        position_[1] -= 1

    if direction == DIRECTION_E:
        position_[0] += 1

    if direction == DIRECTION_SE:
        position_[0] += 1
        position_[1] += 1

    if direction == DIRECTION_S:
        position_[1] += 1

    if direction == DIRECTION_SW:
        position_[0] -= 1
        position_[1] += 1

    if direction == DIRECTION_W:
        position_[0] -= 1

    if direction == DIRECTION_NW:
        position_[0] -= 1
        position_[1] -= 1

    return position_


def get_reverse_direction(board: list, stone_color: int, stone_position: list) -> list:
    reversed_stone_color = get_reversed_color(stone_color)
    reverse_directions = list()

    for direction in range(8):
        next_stone_position = update_position(stone_position, direction)
        next_stone_color = get_stone_color(board, next_stone_position)

        while next_stone_color == reversed_stone_color:
            next_stone_position = update_position(next_stone_position, direction)
            next_stone_color = get_stone_color(board, next_stone_position)

            if next_stone_color == stone_color:
                reverse_directions.append(direction)
                break

    return reverse_directions


def reverse_stone(board: list, stone_color: int, stone_position: list) -> list:
    board = deepcopy(board)
    reverse_directions = get_reverse_direction(board, stone_color, stone_position)

    for direction in reverse_directions:
        next_stone_position = update_position(stone_position, direction)
        next_stone_color = get_stone_color(board, next_stone_position)

        while next_stone_color != stone_color:
            place_stone(board, stone_color, next_stone_position)
            next_stone_position = update_position(next_stone_position, direction)
            next_stone_color = get_stone_color(board, next_stone_position)

    return board


def place_from_code(board: list, code: str) -> list:
    color_code = code[0].lower()
    stone_color = WHITE if color_code == 'w' else BLACK

    position = list()
    position.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(code[1]))
    position.append([str(item) for item in list(range(1, 9))].index(code[2]))

    flipped_board = reverse_stone(board, stone_color, position)

    place_stone(flipped_board, stone_color, position)
    return flipped_board


if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown = f.read()

    board = get_board(markdown)

    place_stone(board, WHITE, [4, 2])
    place_stone(board, WHITE, [5, 1])
    place_stone(board, WHITE, [6, 1])
    place_stone(board, WHITE, [6, 2])
    place_stone(board, BLACK, [6, 3])
    place_stone(board, BLACK, [2, 4])
    board = place_from_code('bg1', board)

    with open("test.md", "w", encoding='utf-8') as f:
        f.write(write_board(board, markdown))
