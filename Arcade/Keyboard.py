# Класс клавиатуры для библиотеки arcade:

class Keyboard:
    def __init__(self):
        # Клавиши:
        self.keys = [
            {1: False}, {2: False}, {4: False}, {8: False}, {16: False}, {32: False}, {64: False}, {128: False},
            {256: False}, {65288: False}, {65289: False}, {65290: False}, {65291: False}, {65293: False},
            {65293: False}, {65299: False}, {65300: False}, {65301: False}, {65307: False}, {65360: False},
            {65361: False}, {65362: False}, {65363: False}, {65364: False}, {65365: False}, {65366: False},
            {65367: False}, {65368: False}, {65535: False}, {65376: False}, {65377: False}, {65378: False},
            {65379: False}, {65381: False}, {65382: False}, {65383: False}, {65384: False}, {65385: False},
            {65386: False}, {65387: False}, {65406: False}, {65406: False}, {65362: False}, {65363: False},
            {65364: False}, {65361: False}, {1: False}, {2: False}, {3: False}, {4: False}, {65366: False},
            {65365: False}, {5: False}, {6: False}, {65288: False}, {65535: False}, {65407: False}, {65408: False},
            {65417: False}, {65421: False}, {65425: False}, {65426: False}, {65427: False}, {65428: False},
            {65429: False}, {65430: False}, {65431: False}, {65432: False}, {65433: False}, {65434: False},
            {65434: False}, {65435: False}, {65435: False}, {65436: False}, {65437: False}, {65438: False},
            {65439: False}, {65469: False}, {65450: False}, {65451: False}, {65452: False}, {65453: False},
            {65454: False}, {65455: False}, {65456: False}, {65457: False}, {65458: False}, {65459: False},
            {65460: False}, {65461: False}, {65462: False}, {65463: False}, {65464: False}, {65465: False},
            {65470: False}, {65471: False}, {65472: False}, {65473: False}, {65474: False}, {65475: False},
            {65476: False}, {65477: False}, {65478: False}, {65479: False}, {65480: False}, {65481: False},
            {65482: False}, {65483: False}, {65484: False}, {65485: False}, {65505: False}, {65506: False},
            {65507: False}, {65508: False}, {65509: False}, {65511: False}, {65512: False}, {65513: False},
            {65514: False}, {65515: False}, {65516: False}, {65517: False}, {65518: False}, {65488: False},
            {65489: False}, {32: False}, {33: False}, {34: False}, {35: False}, {35: False}, {36: False}, {37: False},
            {38: False}, {39: False}, {40: False}, {41: False}, {42: False}, {43: False}, {44: False}, {45: False},
            {46: False}, {47: False}, {48: False}, {49: False}, {50: False}, {51: False}, {52: False}, {53: False},
            {54: False}, {55: False}, {56: False}, {57: False}, {58: False}, {59: False}, {60: False}, {61: False},
            {62: False}, {63: False}, {64: False}, {91: False}, {92: False}, {93: False}, {94: False}, {95: False},
            {96: False}, {96: False}, {97: False}, {98: False}, {99: False}, {100: False}, {101: False}, {102: False},
            {103: False}, {104: False}, {105: False}, {106: False}, {107: False}, {108: False}, {109: False},
            {110: False}, {111: False}, {112: False}, {113: False}, {114: False}, {115: False}, {116: False},
            {117: False}, {118: False}, {119: False}, {120: False}, {121: False}, {122: False}, {123: False},
            {124: False}, {125: False}, {126: False}
        ]

        self.keypress = 0    # Нажатая клавиша.
        self.keyrelease = 0  # Отпущенная клавиша.

    # Вызывайте эту функцию всегда в функции on_key_press():
    def press(self, key: int):
        self.keypress = key
        for k in self.keys:
            if list(k.keys())[0] == key:
                k[list(k.keys())[0]] = True

    # Вызывайте эту функцию всегда в функции on_key_release():
    def release(self, key: int):
        self.keyrelease = key
        for k in self.keys:
            if list(k.keys())[0] == key:
                k[list(k.keys())[0]] = False

    # Вернуть истину если клавиша зажата. Иначе ложь:
    def ispressed(self, key: int):
        for k in self.keys:
            if (list(k.keys())[0] == key) and (k[list(k.keys())[0]]):
                return True
        return False

    # Вернуть истину если клавиша нажата. Иначе ложь:
    def ispress(self, key: int):
        if key == self.keypress:
            return True
        return False

    # Вернуть истину если клавиша отпущена. Иначе ложь:
    def isrelease(self, key: int):
        if key == self.keyrelease:
            return True
        return False

    # Нажатая клавиша:
    def keypress(self):
        return self.keypress

    # Отпущенная клавиша:
    def keyrelease(self):
        return self.keyrelease
