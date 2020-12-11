class AllXml:
    instances = 0

    def __init__(self, name):
        self.added = False
        self.__name = name
        self.__code = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, obj: int):
        self.__code = obj
