from Zoo.AllXmlDependencies import AllXml


class Animal(AllXml):
    instances = 0

    def __init__(self, kind, food):
        AllXml.__init__(self, kind)
        self.__food = food
        Animal.instances += 1
        self.code = Animal.instances

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

    def __del__(self):
        Animal.instances -= 1
