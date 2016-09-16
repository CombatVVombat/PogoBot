from gui.iguicontroller import IGuiController as IGuiController


class Controller(IGuiController):
    def runCommand(self, name):
        command = self.commands.get(name)
        if command is not None:
            command()
        else:
            print("No command with name: " + name)

    def assignCommand(self, name, command):
        if self.commands.get(name) is not None:
            print("Command named: " + name + " already bound.  Rebinding...")
        self.commands[name] = command

    #### FIX ME
    def assignVariable(self, name, variable):
        if self.variables.get(name) is not None:
            print("Variable named: " + name + "already bound.  Rebinding...")
        self.variables[name] = variable

