import random
from gui.iguicontroller import IGuiController as IGuiController


class Controller(IGuiController):
    def __init__(self):
        self.debugPrint = True
        self.id = str(random.randrange(0,1000))

    def runCommand(self, name, *args):
        command = self.commands.get(name)
        if command is not None:
            if self.debugPrint:
                print("GUIController " + self.id + ": Running command '" + name + "'")
            command(*args)
        else:
            print("GUIController " + self.id + ": No command with name: '" + name + "'")

    def bindCommand(self, name, command):
        if self.commands.get(name) is not None:
            print("GUIController " + self.id + ": Command named: '" + name + "' already bound.  Rebinding...")
        self.commands[name] = command

    def createVariable(self, name):
        if self.variables.get(name) is not None:
            print("GUIController " + self.id + ": Variable named: '" + name + "' already bound.  Rebinding...")
        self.variables[name] = ''
        if self.debugPrint:
            print("GUIController " + self.id + ": variable '" + name + "' created.")

    def set(self, name, variable):
        if self.variables.get(name) is None:
            print("GUIController " + self.id + ": set '" + name + "' variable not found.")
            return
        self.variables[name] = variable
        if self.debugPrint:
            print("GUIController " + self.id + ": set '" + name + "' updated.")

    def get(self, name):
        if self.variables.get(name) is None:
            print("GUIController " + self.id + ": get '" + name + "' variable not found.")
            return
        return self.variables[name]


