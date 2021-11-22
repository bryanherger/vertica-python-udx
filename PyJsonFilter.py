import datetime
import json
import vertica_sdk

# Function for flattening json
def flatten_json(y):
    out = {}
  
    def flatten(x, name =''):
          
        # If the Nested key-value 
        # pair is of dict type
        if type(x) is dict:
              
            for a in x:
                flatten(x[a], name + a + '_')
                  
        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:
              
            i = 0
              
            for a in x:                
                # flatten(a, name + str(i) + '_')
                flatten(a, str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
  
    flatten(y)
    return out

class PyJsonFilter(vertica_sdk.UDFilter):
    def __init__(self):
        pass

    def setup(self, srvInterface):
        pass

    def process(self, srvInterface, inputbuffer, inputstate, outputbuffer):
        if inputstate == vertica_sdk.InputState.END_OF_FILE and inputbuffer.getSize() == 0:
            srvInterface.log("EOF / end of buffer")
            return vertica_sdk.StreamState.DONE
        # User process data here, and put into outputbuffer.
        buffer = str()
        jsons = []
        while inputbuffer.getOffset() < inputbuffer.getSize():
            thisbyte = inputbuffer.read(1)
            # srvInterface.log("thisbyte = "+str(thisbyte))
            if thisbyte == b'\n':
                # srvInterface.log("json = "+buffer)
                jsons.append(buffer)
                buffer = str()
                if inputstate == vertica_sdk.InputState.END_OF_FILE:
                    continue
                else:
                    break
            buffer = buffer + thisbyte.decode()
        # inp = inputbuffer.read()
        # jsons = inp.decode().split("\n")
        srvInterface.log("jsons="+str(len(jsons)))
        cc = 0
        for j in jsons:
            # srvInterface.log("j("+str(cc)+")="+j)
            cc = cc + 1  
            try:
                jsonIn = json.loads(j)
            except json.decoder.JSONDecodeError:
                srvInterface.log("Invalid JSON j="+j)
                continue
            # inp = inp + ".json"
            # j['filter'] = 'true'
            jsonOut = flatten_json(jsonIn)
            outputbuffer.write(json.dumps(jsonOut).encode())
        if inputstate == vertica_sdk.InputState.END_OF_FILE:
            srvInterface.log("EOF / size "+str(inputbuffer.getSize())+" / offset"+str(inputbuffer.getOffset()))
            return vertica_sdk.StreamState.DONE
        return vertica_sdk.StreamState.INPUT_NEEDED

class PyJsonFilterFactory(vertica_sdk.FilterFactory):
    def __init__(self):
        pass

    def plan(self, serverInterface, planContext):
        pass

    def prepare(self, serverInterface, planContext):
        #User implement the function to create PyUDSources.
        return PyJsonFilter()
