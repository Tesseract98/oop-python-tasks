import xml.dom.minidom
import xml.etree.cElementTree as et
from Zoo.impl.Cage import Cage
from Zoo.impl.Animal import Animal
from Zoo.impl.Employee import Employee
from Zoo.ZooString import ZooString


class DataXml:
    @staticmethod
    def write(out, object_zoo):
        dom = xml.dom.minidom.Document()
        root = dom.createElement('Zoo')
        dom.appendChild(root)
        for c in object_zoo.zoo_string:
            if not c.get_cage().added:
                out_f = dom.createElement('Cage')
                out_f.setAttribute('code', str(c.get_cage().name))
                out_f.setAttribute('number', str(c.get_cage().name))
                root.appendChild(out_f)
                c.get_cage().added = True
            for i in c.get_animals():
                if not i.added:
                    out_f = dom.createElement('Animal')
                    out_f.setAttribute('code', str(i.code))
                    out_f.setAttribute('kind', i.name)
                    out_f.setAttribute('food', i.food)
                    root.appendChild(out_f)
                    i.added = True
            for i in c.get_employees():
                if not i.added:
                    out_f = dom.createElement('Employee')
                    out_f.setAttribute('code', str(i.code))
                    out_f.setAttribute('name', i.name)
                    out_f.setAttribute('profession', i.profession)
                    root.appendChild(out_f)
                    i.added = True
        for c in object_zoo.zoo_string:
            out_f_str = dom.createElement('ZooString')
            out_f = dom.createElement('Cage')
            out_f.setAttribute('code', str(c.get_cage().name))
            out_f_str.appendChild(out_f)
            for i in c.get_animals():
                out_f = dom.createElement('Animal')
                out_f.setAttribute('code', str(i.code))
                out_f_str.appendChild(out_f)
            for i in c.get_employees():
                out_f = dom.createElement('Employee')
                out_f.setAttribute('code', str(i.code))
                out_f_str.appendChild(out_f)
            root.appendChild(out_f_str)

        xml_str = dom.toprettyxml(indent="  ")
        with open(out, "w") as f:
            f.write(xml_str)

    @staticmethod
    def read(inp, object_zoo):
        Animal.instances = Employee.instances = Cage.instances = 0
        tree = et.ElementTree(file=inp)
        root = tree.getroot()
        child_anim, child_empl, child_cage = dict(), dict(), dict()
        for child in root:
            var = child.attrib
            if child.tag == 'Cage':
                child_cage[var['code']] = Cage(int(var['number']))
            elif child.tag == 'Animal':
                var_obj = Animal(var['kind'], var['food'])
                var_obj.code = int(var['code'])
                child_anim[var['code']] = var_obj
            elif child.tag == 'Employee':
                var_obj = Employee(var['name'], var['profession'])
                var_obj.code = int(var['code'])
                child_empl[var['code']] = var_obj
            if child.tag == 'ZooString':
                new_zoo_string = ZooString()
                for in_child in child:
                    if in_child.tag == 'Animal':
                        new_zoo_string.set_animals(child_anim[in_child.attrib['code']])
                    elif in_child.tag == 'Employee':
                        new_zoo_string.set_employees(child_empl[in_child.attrib['code']])
                    elif in_child.tag == 'Cage':
                        new_zoo_string.set_cage(child_cage[in_child.attrib['code']])
                object_zoo.zoo_string = new_zoo_string
