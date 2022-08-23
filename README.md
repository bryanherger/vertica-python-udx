# vertica-python-udx
Custom UDX including User-Defined Scalar Functions, UDLoader, UDParser, UDFilter extensions for Vertica developed in Python.
## Installation
Clone the repository and run ddl/install.sql or just run the SQL commands to install the UDX you need.

Remove by running ddl/uninstall.sql

## UDFilter example
PyJsonFilter shows how to flatten JSON with a filter.  This is similar to the built-in behavior of the JSON parser.

To run the example:

vsql -U user -w pass -f PythonUDFilter.sql
