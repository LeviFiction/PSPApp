
class APP:
    TargetDocument = None
    ActiveDocument = None
    def __init__(self):
        self.Documents = []
        self.TargetDocument = self.PSPDocument()
        self.ActiveDocument = self.PSPDocument()
        self.__constList = [self.PSPEnumType("Execution mode defines how the command will run; e.g., interactive or silent.", "ExecutionMode", [(u'Default', 0, u'Defer to the parent execution mode.'), (u'Interactive', 1, u'Display dialog to edit parameters, then execute command.'), (u'Silent', 2, u'Execute command without displaying dialog.'), (u'EditOnce', 3, u'Display dialog on first execution, but subsequent executions are silent.'), (u'EditOnly', 4, u'Display the dialog, but do not execute the command.'), (u'SilentFix', 5, u'Execute command without displaying dialog.')] )]
        self.Constants = self.PSPConstantPool(self.__constList)
        pass
    def Do(self, Environment, command, d={}, doc = None):
        pass
    def __getitem__(self, key):
        pass
    def EndMemStats(self):
        pass
    def GetCommandParameters(self):
        pass
    def GetMemStats(self):
        pass
    def StartMemStats(self):
        pass
    
    class PSPDocument:
        def __init__(self):
            self.Width = 0
            self.Height = 0
            self.Name = ""
            self.Title = ""

    class PSPConstantPool():
        def __init__(self, constants):
            self.__constants = constants
            pass
        def All(self):
            pass
        def __getattr__(self, key):
            for x in self.__constants:
                if x.Name() == key:
                    return x

    class PSPEnumType:
        __Description = ""
        __Name = ""
        __Values = []
        def __init__(self, Description = "", Name = "", Values = []):
            self.__Description = Description
            self.__Name = Name
            self.__Values = Values
            pass
        def Description(self):
            return self.__Description
        def Name(self):
            return self.__Name
        def Values(self):
            return self.__Values
        def __getattr__(self, key):
            for x in self.__Values:
                if key == x[0]:
                    return x[1]

    # Constants = PSPConstantPool(__constList)
App = APP()