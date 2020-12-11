from Zoo.AllXmlDependencies import AllXml


class Cage(AllXml):
    instances = 0

    def __init__(self, number):
        AllXml.__init__(self, number)
        self.code = number
        Cage.instances += 1
