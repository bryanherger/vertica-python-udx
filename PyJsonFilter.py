import datetime
import json
import vertica_sdk

# Function for flattening 
# json
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
        # User process data here, and put into outputbuffer.
        inp = inputbuffer.read()
        jsonIn = json.loads(inp.decode())
        # inp = inp + ".json"
        # j['filter'] = 'true'
        jsonOut = flatten_json(jsonIn)
        outputbuffer.write(json.dumps(jsonOut).encode())
        return vertica_sdk.StreamState.DONE

class PyJsonFilterFactory(vertica_sdk.FilterFactory):
    def __init__(self):
        pass

    def plan(self, serverInterface, planContext):
        pass

    def prepare(self, serverInterface, planContext):
        #User implement the function to create PyUDSources.
        return PyJsonFilter()
