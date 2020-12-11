from Zoo.AllXmlDependencies import AllXml


class Employee(AllXml):
    instances = 0

    def __init__(self, name, profession):
        AllXml.__init__(self, name)
        self.__profession = profession
        Employee.instances += 1
        self.code = Employee.instances

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        self.__profession = profession

    def __del__(self):
        Employee.instances -= 1
