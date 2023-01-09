# vertica-python-udx
Custom UDX including User-Defined Scalar Functions, UDLoader, UDParser, UDFilter extensions for Vertica developed in Python.
## Installation
Clone the repository and run ddl/install.sql or just run the SQL commands to install the UDX you need.

Remove by running ddl/uninstall.sql

## UDSF example: PyEncryptUDSF (aes_decrypt)
PyEncryptUDSF installs aes_decrypt, which decrypts a base64-encoded string using AES and a fixed key.  "aes.py" is included to generate a base64-encoded, encrypted string to test.

In order to use this, you'll also need to create a virtualenv with pycryptodome and copy the site-packages as a dependency as shown in ddl/install.sql

Create the virtualenv under /tmp with "python3 -m venv crypto".  Activate the virtualenv and run the following to remove old crypto and install latest pycryptodome:
```
pip3 uninstall crypto 
pip3 uninstall pycrypto 
pip3 install pycryptodome
```
Then run ddl/install.sql

## UDSF example: reverseGeocode 
reverseGeocode uses OpenStreetMap Nominatim and Python geopy to convert a (latitude,longitude) pair into a human readable address string.  All needed files are in the `reversegeocode` folder.

In order to use this, you'll need to create a virtualenv with geopy and copy the site-packages as a dependency. It's best to run on a Vertica node so the venv will be the same version as Vertica's bundled Python distribution.
The script "mkgeopyvenv.sh" will create a virtual environment using Vertica's Python package under /tmp that will be loaded as a dependency by the SQL script.  If you create one elsewhere, you'll need to edit the SQL to point to the correct venv path.

Run the SQL with `vsql -U <user> -w <password> -e -f ST_ReverseGeocode.sql`  The sample query should return:
```
SELECT reverseGeocode(40.773408,-73.870676);
                                      reverseGeocode
-------------------------------------------------------------------------------------------
 LaGuardia Airport, Runway Drive, Queens, City of New York, New York, 11371, United States
(1 row)
```

Note that the sample SQL 

## UDFilter example: PyJsonFilter
PyJsonFilter shows how to flatten JSON with a filter.  This is similar to the built-in behavior of the JSON parser.

To run the example:

vsql -U user -w pass -f PythonUDFilter.sql
