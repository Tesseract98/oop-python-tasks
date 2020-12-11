from Zoo.ZooString import ZooString


class Zoo:
    def __init__(self):
        self.__zoo_strings = []

    @property
    def zoo_string(self):
        return self.__zoo_strings

    @zoo_string.setter
    def zoo_string(self, obj):
        self.__zoo_strings.append(obj)

    def delete_animal(self, code: int):
        self.__delete_index(ZooString.get_animals, code)

    def delete_employee(self, code: int):
        self.__delete_index(ZooString.get_employees, code)

    def delete_string(self, code: int):
        del self.zoo_string[code]

    def __delete_index(self, obj_func, code):
        for i in self.zoo_string:
            size_lst = len(obj_func(i))
            for j in range(size_lst):
                if obj_func(i)[j].code == code:
                    del obj_func(i)[j]
                    break
        new_code = 1
        for i in self.zoo_string:
            for j in obj_func(i):
                j.code = new_code
                new_code += 1
