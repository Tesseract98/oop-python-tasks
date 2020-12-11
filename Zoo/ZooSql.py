import sqlite3 as db
from Zoo.impl.Cage import Cage
from Zoo.impl.Animal import Animal
from Zoo.impl.Employee import Employee
from Zoo.ZooString import ZooString

empty_db = """
PRAGMA foreign_keys = ON;

Create Table IF NOT EXISTS Cage(
    code Integer Primary Key Not Null
);

Create Table IF NOT EXISTS Animal(
    code Integer Primary Key Autoincrement Not Null,
    name Varchar Not Null,
    food Varchar Not Null,
    cage integer references Cage(code) on update cascade on delete cascade
);

Create Table IF NOT EXISTS Employee(
    code Integer Primary Key Autoincrement Not Null,
    name Varchar Not Null,
    profession Varchar Not Null
);

Create Table IF NOT EXISTS Zoo(
    cage integer references Cage(code) on update cascade on delete cascade,
    employee integer references Employee(code) on update cascade on delete cascade
);
"""


class DataSql:
    @staticmethod
    def write(out, object_zoo):
        conn = db.connect(out)
        curs = conn.cursor()
        curs.executescript(empty_db)
        codes_animal = []
        codes_employee = []
        for c in object_zoo.zoo_string:
            if not c.get_cage().added:
                curs.execute("Insert Into Cage(code) Values(?)", [c.get_cage().name])
                c.get_cage().added = True
            for i in c.get_animals():
                if not i.added:
                    codes_animal.append(i.code)
                    curs.execute("Insert Into Animal(code, name, food, cage) Values(?, ?, ?, ?)",
                                 [i.code, i.name, i.food, c.get_cage().name])
                    i.added = True
            for i in c.get_employees():
                if not i.added:
                    i.added = True
                    codes_employee.append(i.code)
                    curs.execute("Insert Into Employee(code, name, profession) Values(?, ?, ?)",
                                 [i.code, i.name, i.profession])
                curs.execute("Insert Into Zoo(cage, employee) Values(?, ?)", [c.get_cage().name, i.code])
        conn.commit()
        conn.close()

    @staticmethod
    def read(inp, object_zoo):
        Animal.instances, Employee.instances, Cage.instances = 0, 0, 0
        employee_instances = dict()
        conn = db.connect(inp)
        curs = conn.cursor()
        cage_dict = dict()
        curs.execute('select code from Cage')
        for i in curs.fetchall():
            cage_dict[i[0]] = Cage(i[0])
        for i, j in cage_dict.items():
            new_zoo_string = ZooString(j)
            curs.execute("Select code, name, food From Animal Where cage = ?", [i])
            anim_lst = curs.fetchall()
            for z in anim_lst:
                obj_animal = Animal(z[1], z[2])
                obj_animal.code = z[0]
                new_zoo_string.set_animals(obj_animal)
            curs.execute("Select employee From Zoo Where cage = ?", [i])
            cage_lst = curs.fetchall()
            for z in cage_lst:
                curs.execute("Select code, name, profession From Employee Where code = ?", z)
                empl_lst = curs.fetchall()
                if empl_lst[0][1] not in employee_instances:
                    obj_employee = Employee(empl_lst[0][1], empl_lst[0][2])
                    obj_employee.code = empl_lst[0][0]
                    employee_instances[empl_lst[0][1]] = obj_employee
                new_zoo_string.set_employees(employee_instances[empl_lst[0][1]])
            object_zoo.zoo_string = new_zoo_string

