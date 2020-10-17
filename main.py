# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def GetName(self):
        print(self.name)

    def GetAge(self):
        print(self.age)

class Citizn(People):  
    def SetNation(self, nation):
        self.nation = nation

    def GetNation(self):
        print(self.nation)

Me = Citizn('yujiro', 39)

Me.GetName()
Me.GetAge()
Me.SetNation('Japan')
Me.GetNation()


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
