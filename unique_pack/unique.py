#! python2.7

"""
Module for gathering unique values from an input.
Focused on ArcGIS specific inputs such as field values of a feature class.
"""

import collections

import arcpy


def get_unique_feature(input_feature, field):
    """
    Collect unique values from an input feature class
    :param input_feature: feature class, shp, layer
    :param field: text value of field name to process
    :return: regular dictionary of unique values and counts
    """

    counter = collections.Counter()
    with arcpy.da.SearchCursor(input_feature, field) as cursor:
        for row in cursor:
            counter[row[0]] += 1

    return dict(counter)
