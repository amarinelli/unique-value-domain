import imp

import re

import arcpy

import unique.core as unique

# Used during development, force reload
imp.reload(unique)


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

        # First parameter
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPTableView",
            parameterType="Required",
            direction="Input")

        # Second parameter
        param1 = arcpy.Parameter(
            displayName="Values Field",
            name="values_field",
            datatype="Field",
            parameterType="Required",
            direction="Input")

        param1.enabled = False
        param1.filter.list = ["Short", "Long", "Float", "Double", "Text",
                              "Date"]
        param1.parameterDependencies = [param0.name]

        # Third parameter
        param2 = arcpy.Parameter(
            displayName="Geodatabase",
            name="geodatabase",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        param2.filter.list = ["Local Database", "Remote Database"]

        # Fourth parameter
        param3 = arcpy.Parameter(
            displayName="Domain name",
            name="domain_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        params = [param0, param1, param2, param3]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        if parameters[0].value:
            parameters[1].enabled = True
        else:
            parameters[1].enabled = False

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        if parameters[1].value:
            desc = arcpy.Describe(parameters[0].value)
            if desc.editorTrackingEnabled:
                editor_fields = [desc.creatorFieldName, desc.createdAtFieldName,
                                 desc.editorFieldName, desc.editedAtFieldName]
                if str(parameters[1].value) in editor_fields:
                    parameters[1].setErrorMessage(
                        "Editor Tracking fields don't need domains")

        if parameters[3].value:
            if re.match("^[a-zA-Z0-9_-]*$", parameters[3].valueAsText)
                parameters[3].setErrorMessage("Domain name should only " \
                                              "contain letters, numbers, " \
                                              "underscores, and hyphens")

        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        # Gather parameters
        input_values = parameters[0].valueAsText
        field = parameters[1].valueAsText
        geodatabase = parameters[2].valueAsText
        domain_name = parameters[3].valueAsText

        # Generate unique values from feature class > field
        values = unique.get_unique_feature(input_values, field)
        arcpy.AddMessage("Values: " + str(values))

        return
