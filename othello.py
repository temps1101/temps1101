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
            return board[y + 1][x + 1]['status']
        if direction == DIRECTION_S:
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
    x, y = position
    updated_position = list()

    if direction == DIRECTION_N:
        updated_position.append(x)
        updated_position.append(y - 1)

    if direction == DIRECTION_NE:
        updated_position.append(x + 1)
        updated_position.append(y - 1)

    if direction == DIRECTION_E:
        updated_position.append(x + 1)
        updated_position.append(y)
        updated_position[0] += 1

    if direction == DIRECTION_SE:
        updated_position.append(x + 1)
        updated_position.append(y + 1)

    if direction == DIRECTION_S:
        updated_position.append(x)
        updated_position.append(y + 1)

    if direction == DIRECTION_SW:
        updated_position.append(x - 1)
        updated_position.append(y + 1)
        updated_position[0] -= 1
        updated_position[1] += 1

    if direction == DIRECTION_W:
        updated_position.append(x - 1)
        updated_position.append(y)

    if direction == DIRECTION_NW:
        updated_position.append(x - 1)
        updated_position.append(y - 1)

    return updated_position


def reverse_stone(board: list, placed_status: int, stone_position: list) -> list:
    board_dst = board.copy()
    reversed_status = BLACK if placed_status == WHITE else WHITE
    for direction in range(8):
        next_stone: int = get_next_stone(board_dst, stone_position, direction)
        next_stone_position = update_position(stone_position, direction)

        while next_stone == reversed_status:
            next_stone = get_next_stone(board_dst, next_stone_position, direction)

            if next_stone == placed_status:
                next_stone_position2 = update_position(stone_position, direction)

                while next_stone_position2 != next_stone_position:
                    x, y = next_stone_position2
                    board_dst[y][x]['status'] = placed_status
                    next_stone_position2 = update_position(next_stone_position2, direction)

                x, y = next_stone_position2
                board_dst[y][x]['status'] = placed_status

            next_stone_position = update_position(next_stone_position, direction)

    return board_dst


def place_from_code(code: str, board_list: list) -> list:
    '''
    code format: '[COLOR (W|B)][X (A-H)][Y (1-8)]'
    examples:
        - to place black stone in position b2, the code will be 'BB2'
    returns:
        {
            'exit code': 0 | 1,
            'board_list': board_list
        }
    '''

    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    number_list = [str(item) for item in list(range(1, 9))]
    error = {'exit code': 1, 'board_list': list()}

    if len(code) != 3:
        return error

    if code[0].lower() == 'w':
        status_color = WHITE

    elif code[0].lower() == 'b':
        status_color = BLACK

    else:
        return error

    position = [0, 0]
    if code[1].lower() in char_list:
       position[0] = char_list.index(code[1])

    else:
        return error

    if code[2] in number_list:
        position[1] = number_list.index(code[2])

    else:
        return error

    flipped_board = reverse_stone(board_list, status_color, position)

    if flipped_board != board_list:
        flipped_board[position[1]][position[0]] = status_color
        return {'exit code': 0, 'board_list': flipped_board}

    else:
        return error

        
if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown = f.read()

    board_list = get_board(markdown)

    print(place_from_code('bd3', board_list))
    #board_list[2][2]['status'] = WHITE
    #board_list[1][1]['status'] = BLACK
    #board_list[5][5]['status'] = BLACK
    #board_list = reverse_stone(board_list, BLACK, [1, 1])
    #board_list[2][5]['status'] = WHITE
    #board_list[2][5]['status'] = WHITE
    #board_list[5][2]['status'] = WHITE
    #board_list = reverse_stone(board_list, WHITE, [2, 5])


    with open("test.md", "w", encoding='utf-8') as f:
        f.write(write_board(board_list, markdown))
