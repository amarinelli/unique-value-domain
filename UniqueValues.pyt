import arcpy
import unique


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Unique Values"
        self.alias = "unique"

        # List of tool classes associated with this toolbox
        self.tools = [UniqueValuesDomain]


class UniqueValuesDomain(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Unique Values to Coded Value Domain"
        self.description = "Using an input that contains a list of values, " \
                           "this tool will create a set of all unique values " \
                           "and assign them to a new or existing coded " \
                           "values domain in the geodatabase"
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
