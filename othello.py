import xml.etree.ElementTree as et
from copy import deepcopy
from sys import argv


INVAILD_IMG_URL = 'https://raw.githubusercontent.com/temps1101/temps1101/main/images/youcantclickhere.jpg'
INITIALIZED_BOARD = [[{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://github.com/temps1101/temps1101/issues/new?&title=bd3&body=Just+press+[Submit+new+issue]+button+below.%0A+DO+NOT+EDIT+THE+TITLE.+IT+WILL+CAUSE+AN+ERROR&labels=place+stone'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://github.com/temps1101/temps1101/issues/new?&title=bc4&body=Just+press+[Submit+new+issue]+button+below.%0A+DO+NOT+EDIT+THE+TITLE.+IT+WILL+CAUSE+AN+ERROR&labels=place+stone'}, {'status': 2, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 1, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 1, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 2, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://github.com/temps1101/temps1101/issues/new?&title=bf5&body=Just+press+[Submit+new+issue]+button+below.%0A+DO+NOT+EDIT+THE+TITLE.+IT+WILL+CAUSE+AN+ERROR&labels=place+stone'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://github.com/temps1101/temps1101/issues/new?&title=be6&body=Just+press+[Submit+new+issue]+button+below.%0A+DO+NOT+EDIT+THE+TITLE.+IT+WILL+CAUSE+AN+ERROR&labels=place+stone'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}], [{'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}, {'status': 0, 'url': 'https://raw.githubusercontent.com/temps1101/temps1101/dev/images/youcantclickhere.jpg'}]]

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


def get_current_stone_color(markdown: str) -> int:
    target_text = markdown.split('<!--color-->')[1]
    return BLACK if target_text == 'BLACK' else WHITE


def get_statistics(markdown: str) -> dict:
    target_text = markdown.split('<!--stats-->')[1]
    root = et.fromstring(target_text)

    statistics = dict()

    statistics['latest player'] = [root[1][0][1][0].attrib['href'], root[1][0][1][0].text]
    for row in root[1][1:]:
        statistics[row[0].text] = int(row[1].text)

    return statistics


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


def write_current_stone_color(stone_color: int, markdown: str) -> str:
    separated_markdown = markdown.split('<!--color-->')
    separated_markdown[1] = 'BLACK' if stone_color == BLACK else 'WHITE'

    return '<!--color-->'.join(separated_markdown)


def write_statistics(statistics: dict, markdown: str) -> str:
    separated_markdown = markdown.split('<!--stats-->')
    root = et.fromstring(separated_markdown[1])

    root[1][0][1][0].attrib['href'] = statistics['latest player'][0]
    root[1][0][1][0].text = statistics['latest player'][1]

    root[1][1][1].text = str(statistics['placed stones'])
    root[1][2][1].text = str(statistics['played matches'])

    separated_markdown[1] = et.tostring(root, encoding='unicode')

    return '\n<!--stats-->\n'.join(separated_markdown)


def get_reversed_color(color: int) -> int:
    return BLACK if color == WHITE else WHITE if color == BLACK else None


def place_stone(board: list, stone_color: int, stone_position: list) -> None:
    x, y = stone_position
    board[y][x]['status'] = stone_color


def get_stone_color(board: list, stone_position: list) -> list:
    x, y = stone_position
    try:
        return board[y][x]['status']

    except IndexError:
        return None


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


def set_url(board: list, stone_position: list, url: str) -> None:
    x, y = stone_position
    board[y][x]['url'] = url


def create_url(board: list, stone_color: int) -> list:
    board = deepcopy(board)

    for y in range(8):
        for x in range(8):
            position = [x, y]
            if get_stone_color(board, position) != BLANK or len(get_reverse_direction(board, stone_color, position)) == 0:
                url = INVAILD_IMG_URL

            else:
                code = ('b' if stone_color == BLACK else 'w') + \
                    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][position[0]] + \
                    ['1', '2', '3', '4', '5', '6', '7', '8'][position[1]]

                url = f'https://github.com/temps1101/temps1101/issues/new?&title={code}&body=Just+press+[Submit+new+issue]+button+below.%0A+DO+NOT+EDIT+THE+TITLE.+IT+WILL+CAUSE+AN+ERROR'

            set_url(board, position, url)

    return board


def is_reset(board: list) -> bool:
    for y in range(8):
        for x in range(8):
            print(get_stone_color(board, [x, y]), x, y)
            if get_stone_color(board, [x, y]) == BLANK:
                return False

    return True


if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown = f.read()

    board = get_board(markdown)
    current_color = get_current_stone_color(markdown)
    statistics = get_statistics(markdown)

    code = argv[1]

    if len(code) == 3:
        if code[0].lower() == ('b' if current_color == BLACK else 'w'):
            position = list()
            try:
                position.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(code[1]))
                position.append([str(item) for item in list(range(1, 9))].index(code[2]))
            except ValueError:
                print('The position code is incorrect')
                exit()

            if len(get_reverse_direction(board, current_color, position)) != 0:
                reversed_board = reverse_stone(board, current_color, position)
                place_stone(reversed_board, current_color, position)
                reversed_board = create_url(reversed_board, get_reversed_color(current_color))

                statistics['latest player'] = [f'https://github.com/{argv[2]}', argv[2]]
                statistics['placed stones'] += 1
                if is_reset(reversed_board):
                    print("eh")
                    reversed_board = INITIALIZED_BOARD
                    current_color = BLACK
                    statistics['played matches'] += 1

                else:
                    current_color = get_reversed_color(current_color)

                with open("README.md", "w", encoding='utf-8') as f:
                    markdown = write_board(reversed_board, markdown)
                    markdown = write_current_stone_color(current_color, markdown)
                    markdown = write_statistics(statistics, markdown)
                    f.write(markdown)

                print('successfully placed your stone!')

            else:
                print('The position you want to place the stone is unplaceable.')

        else:
            print('The stone color code is incorrect.')

    else:
        print('Your code\'s length is incorrect.')
