# please see https://geopy.readthedocs.io/en/stable/#installation for how to use geopy package to implement.
import datetime
import vertica_sdk
import ssl
import geopy.geocoders
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
geopy.geocoders.options.default_ssl_context = ctx

class reverseGeocode(vertica_sdk.ScalarFunction):
    """
    UDSF calls OpenStreetMap API to reverse geocode a point
    """
    def processBlock(self, server_interface, arg_reader, res_writer):
        from geopy.geocoders import Nominatim
        server_interface.log("Hello! python_udxes_are_great")
        geolocator = Nominatim(user_agent="vertica12_python_udsf")
        while True:
            lat = arg_reader.getFloat(0)
            lon = arg_reader.getFloat(1)
            location = geolocator.reverse(str(lat)+","+str(lon))
            res_writer.setString(location.address)
            res_writer.next()
            if not arg_reader.next():
                break

class reverseGeocode_factory(vertica_sdk.ScalarFunctionFactory):
    volatility = vertica_sdk.Volatility.IMMUTABLE

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addFloat()
        arg_types.addFloat()
        return_type.addVarchar()
    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(256)
    def createScalarFunction(self, srv):
        return reverseGeocode()
