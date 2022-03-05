from contextlib import contextmanager


class Storage:

    def __init__(self, items):
        self.__items = items
        self.is_appendable = False

    def show(self):
        print(self.__items)

    def append(self, item):
        if self.is_appendable:
            self.__items.append(item)

    def __lock(self):
        self.is_appendable = False

    def __unlock(self):
        self.is_appendable = True

    @contextmanager
    def open_storage(self):
        if not self.is_appendable:
            self.__unlock()
        yield self
        self.__lock()


if __name__ == '__main__':
    storage = Storage([1, 2, 'abcde'])
    storage.show()
    with storage.open_storage() as opened_storage:
        opened_storage.append(999)
        opened_storage.append('gtr')
    storage.append('ooo')
    storage.append('qwerty')
    storage.show()
