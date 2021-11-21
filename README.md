# vertica-python-udl
Custom UDLoader, UDParser, UDFilter extensions for Vertica developed in Python.
## UDFilter example
PyJsonFilter shows how to flatten JSON with a filter.  This is similar to the built-in behavior of the JSON parser.

To run the example:

vsql -U user -w pass -f PythonUDFilter.sql
