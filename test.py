def hoge(x: list):
    temp = x.copy()
    print('temp: {}'.format(temp))
    print('x: {}'.format(x))
    temp[0] = 'A'
    temp[1] = 'B'
    temp[3] = 'C'
    print('temp: {}'.format(temp))
    print('x: {}'.format(x))

    return temp


fuga = ['a', 'b', 'c', 'd', 'f']
print('fuga: {}'.format(fuga))
hogedfuga = hoge(fuga)

print('hogedfuga: {}'.format(hogedfuga))
print('fuga: {}'.format(fuga))
