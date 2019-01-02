# definitions
EMPTY = '_'
WALL = 'W'
BOX = 'B'
BOX_ON_TARGET = 'BT'
TARGET = 'T'
PLAYER = 'P'


def get_level():
    return [
        '_ _ _ _ W W W W W _ _ _ _ _ _ _ _ _ _'.split(' '),
        '_ _ _ _ W _ _ _ W _ _ _ _ _ _ _ _ _ _'.split(' '),
        '_ _ _ _ W B _ _ W _ _ _ _ _ _ _ _ _ _'.split(' '),
        '_ _ W W W _ _ B W W _ _ _ _ _ _ _ _ _'.split(' '),
        '_ _ W _ _ B _ B _ W _ _ _ _ _ _ _ _ _'.split(' '),
        'W W W _ W _ W W _ W _ _ _ W W W W W W'.split(' '),
        'W _ _ _ W _ W W _ W W W W W _ _ T T W'.split(' '),
        'W _ B _ _ B _ _ _ _ _ _ _ _ _ _ T T W'.split(' '),
        'W W W W W _ W W W _ W P W _ _ _ T T W'.split(' '),
        '_ _ _ _ W _ _ _ _ _ W W W W W W W W W'.split(' '),
        '_ _ _ _ W W W W W W W _ _ _ _ _ _ _ _'.split(' '),
    ]
