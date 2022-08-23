import vertica_sdk

def decryptData(data):
    import base64
    from Crypto.Cipher import AES
    import configparser
 
    try:
        if data !=  None:
            result = 'N/A'
            decodedata = base64.b64decode(data)
            secret_key = b'0123456789abcdef'
            iv = b'0123456789abcdef'
            rev_obj = AES.new(secret_key, AES.MODE_CBC, iv)
            plaintext = rev_obj.decrypt(decodedata)
            result = plaintext.decode()
        else:
            result='N/A (None)'
    except Exception as e:
        result = 'N/A (Exception) '+str(e)
        pass
    return result

class aes_decrypt(vertica_sdk.ScalarFunction):
    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, block_reader, block_writer):
        while(True):
            enc = block_reader.getString(0)
            block_writer.setString(str(decryptData(enc)))
            block_writer.next()
            if not block_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass

class aes_decrypt_factory(vertica_sdk.ScalarFunctionFactory):

    def createScalarFunction(self, srv):
        return aes_decrypt()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addVarchar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(4096)
