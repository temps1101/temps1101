import xml.etree.ElementTree as et


BLANK = 0
BLACK = 1
WHITE = 2


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


if __name__ == '__main__':
    with open('README.md', 'r') as f:
        markdown = f.read()

    board_list = get_board(markdown)
    board_list[0][0]['status'] = 1
    board_list[0][0]['url'] = 'google.com'

    print(write_board(board_list, markdown))
