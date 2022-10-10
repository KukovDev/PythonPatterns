# Класс мыши для библиотеки arcade:


class Mouse:
    def __init__(self):
        self.buttons = [{1: False}, {2: False}, {4: False}]  # Кнопки.
        self.keypress = 0                                    # Нажатая кнопка.
        self.keyrelease = 0                                  # Отпущенная кнопка.
        self.pos = 0, 0                                      # Позиция мыши.
        self.scroll = 0, 0                                   # Скролл мыши.

    # Вызывайте эту функцию всегда в функции on_key_press():
    def press(self, x: int, y: int, button: int):
        self.keypress = button
        self.pos = x, y
        for b in self.buttons:
            if list(b.keys())[0] == button:
                b[list(b.keys())[0]] = True

    # Вызывайте эту функцию всегда в функции on_key_release():
    def release(self, x: int, y: int, button: int):
        self.keyrelease = button
        self.pos = x, y
        for b in self.buttons:
            if list(b.keys())[0] == button:
                b[list(b.keys())[0]] = False

    # Вызывайте эту функцию всегда в функции on_mouse_motion():
    def motion(self, x: int, y: int):
        self.pos = x, y

    # Вызывайте эту функцию всегда в функции on_mouse_scroll():
    def scroll(self, x: int, y: int, scrollx: int, scrolly: int):
        self.pos = x, y
        self.scroll = scrollx, scrolly

    # Вернуть истину если кнопка зажата. Иначе ложь:
    def ispressed(self, button: int):
        for b in self.buttons:
            if (list(b.keys())[0] == button) and (b[list(b.keys())[0]]):
                return True
        return False

    # Вернуть истину если клавиша нажата. Иначе ложь:
    def ispress(self, button: int):
        if button == self.keypress:
            return True
        return False

    # Вернуть истину если кнопка отпущена. Иначе ложь:
    def isrelease(self, button: int):
        if button == self.keyrelease:
            return True
        return False

    # Нажатая кнопка:
    def keypress(self):
        return self.keypress

    # Отпущенная кнопка:
    def keyrelease(self):
        return self.keyrelease

    # Получить позицию мыши:
    def getpos(self):
        return self.pos

    # Получить скроллинг мыши:
    def getscroll(self):
        return self.scroll
