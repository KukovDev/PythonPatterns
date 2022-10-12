# Класс мыши для библиотеки arcade:


class Mouse:
    def __init__(self):
        self.buttons = [{1: False}, {2: False}, {4: False}]  # Кнопки.
        self.keypress = 0                                    # Нажатая кнопка.
        self.keyrelease = 0                                  # Отпущенная кнопка.
        self.pos = 0, 0                                      # Позиция мыши.
        self.mscroll = 0, 0                                  # Скролл мыши.
        self.ismscroll = False                               # Крутится ли колёсико мыши.

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
        self.mscroll = scrollx, scrolly
        self.ismscroll = True

    # Вернуть истину если кнопка зажата. Иначе ложь:
    def ispressed(self, button: int):
        for b in self.buttons:
            if (list(b.keys())[0] == button) and (b[list(b.keys())[0]]):
                return True
        return False

    # Вернуть истину если клавиша нажата. Иначе ложь:
    def ispress(self, button: int):
        if button == self.keypress:
            self.keypress = 0
            return True
        return False

    # Вернуть истину если кнопка отпущена. Иначе ложь:
    def isrelease(self, button: int):
        if button == self.keyrelease:
            self.keyrelease = 0
            return True
        return False
    
    # Вернуть истину если колёсико мыши крутится. Иначе ложь:
    def isscroll(self):
        if self.ismscroll:
            self.ismscroll = False
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
        return self.mscroll
