# Syntax
# class parent_class:
#     def __init__(self,p1,p2):
#         self.p1=p1
#         self.p2=p2
#     def method_name(self):
#         #implementation


# class child_class(parent_class):
#     def __init__(self,p3,p4):
#         self.p3=p3
#         self.p4=p4
#     def method_name(self):
#         #implementation
    

# child_object=child_class(p1,p2)
# child_object.method_name()

# Example 1: Father and Son (Single Inheritance + super())
# Code

class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is ", self.surname)

    def display_father_name(self):
        print("The fathername is ", self.father_name)


class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("name is ", self.name)


child_obj=son("john", "K","Rajesh")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()
