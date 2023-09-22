class Computer:
    def __init__(self,name,make,os):
        self.name = name
        self.CPU_Obj = self.CPU(make)
        self.OS_Obj = self.OS(os)

    def __str__(self):
        return "Name : " + self.name + "\nCPU : " + self.CPU_Obj.get_make() + "\nOS Name : " + self.OS_Obj.get_name()

    class CPU:
        def __init__(self,make):
            self.make = make

        def get_make(self):
            return self.make
        
    class OS:
        def __init__(self,os):
            self.os = os

        def get_name(self):
            return self.os
        
c = Computer('PC1','Intel','Linux')
print(c)