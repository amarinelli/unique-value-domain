# Unique Values Python toolbox

##### v0.0.1 (March 2016)

###### ArcGIS Python toolbox for gathering unique values from an input and assigning them to a new or existing coded value domain in the geodatabase.


#### Tools

###### [Unique Values to Coded Value Domain](https://github.com/amarinelli/unique-value-domain/blob/master/UniqueValues.pyt#L24)
> Inputs such as a tables and csv can be used along with an appropriate field to determine the unique values and assign them to a new or existing coded value domain in a geodatabase of the user's choice.
>> **Parameters:**
- `input_feature` feature class, table, shp, layer
- `in_field` text value of the field name to process values from
- `geodatabase` workspace where the domain will live
- `domain_name` name of the new domain


#### ArcGIS Desktop compatibility

- Python `2.7`
- Tested @ ArcGIS for Desktop `10.3.x`
- No client dependencies aside from *arcpy*


#### Development

See `tests` folder for [basic tests](tests/test_basic.py) and [sample data](tests/data)

- [pytest](https://github.com/pytest-dev/pytest/)
- [virtualenv](https://github.com/pypa/virtualenv)


#### Issues and Enhancements

- See [here](https://github.com/amarinelli/unique-value-domain/issues)
