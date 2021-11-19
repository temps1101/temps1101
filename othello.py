import xml.etree.ElementTree as et


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


def get_next_stone(board: list, position: list, direction: int) -> int:
    x, y = position
    try:
        if direction == DIRECTION_N:
            return board[y - 1][x]['status']
        if direction == DIRECTION_NE:
            return board[y - 1][x + 1]['status']
        if direction == DIRECTION_E:
            return board[y][x + 1]['status']
        if direction == DIRECTION_SE:
            print(x+1, y+1)
            return board[y + 1][x + 1]['status']
        if direction == DIRECTION_S:
            print(y+1, x)
            return board[y + 1][x]['status']
        if direction == DIRECTION_SW:
            return board[y + 1][x - 1]['status']
        if direction == DIRECTION_W:
            return board[y][x - 1]['status']
        if direction == DIRECTION_NW:
            return board[y - 1][x - 1]['status']
    except IndexError:
            return None


def update_position(position: list, direction: int) -> list:
    if direction == DIRECTION_N:
        position[1] -= 1

    if direction == DIRECTION_NE:
        position[0] += 1
        position[1] -= 1

    if direction == DIRECTION_E:
        position[0] += 1

    if direction == DIRECTION_SE:
        position[0] += 1
        position[1] += 1

    if direction == DIRECTION_S:
        position[1] += 1

    if direction == DIRECTION_SW:
        position[0] -= 1
        position[1] += 1

    if direction == DIRECTION_W:
        position[0] -= 1

    if direction == DIRECTION_NW:
        position[0] -= 1
        position[1] -= 1

    return position


def reverse_stone(board: list, placed_status: int, stone_position: list) -> list:
    reversed_status = BLACK if placed_status == WHITE else WHITE
    for direction in range(8):
        reverse_claim = False
        next_stone: int = get_next_stone(board, stone_position, direction)
        temp_position = update_position(stone_position, direction)
        print(direction, next_stone)
        '''
        while next_stone not in [BLANK, None]:
            if next_stone == reversed_status:
                reverse_claim = True
                temp_position = update_position(temp_position, direction)

            if next_stone == placed_status:
                if reverse_claim:
                    temp_position2 = update_position(stone_position, direction)
                    while get_next_stone(board, temp_position2, direction) == reversed_status:
                        x, y = temp_position2
                        board[y][x]['status'] = placed_status
                else:
                    break
        '''

    return board

if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown = f.read()

    board_list = get_board(markdown)

    board_list[4][5]['status'] = BLACK
    board_list = reverse_stone(board_list, BLACK, [5, 4])


    with open("test.md", "w", encoding='utf-8') as f:
        f.write(write_board(board_list, markdown))
