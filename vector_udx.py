import math
import vertica_sdk

def cosine_similarity_function(vec1, vec2):
    # Pad the shorter vector with zeros
    if len(vec1) < len(vec2):
        vec1.extend([0] * (len(vec2) - len(vec1)))
    elif len(vec2) < len(vec1):
        vec2.extend([0] * (len(vec1) - len(vec2)))
    # Compute the dot product
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    # Compute the magnitudes of the vectors
    magnitude_vec1 = math.sqrt(sum(a * a for a in vec1))
    magnitude_vec2 = math.sqrt(sum(a * a for a in vec2))
    # Compute the cosine similarity
    cosine_sim = dot_product / (magnitude_vec1 * magnitude_vec2)
    return cosine_sim

class cosine_similarity(vertica_sdk.ScalarFunction):
    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            lmat = [float(cell.getNumeric(0)) for cell in arg_reader.getArrayReader(0)]
            rmat = [float(cell.getNumeric(0)) for cell in arg_reader.getArrayReader(1)]
            res_writer.setFloat(cosine_similarity_function(lmat,rmat))
            res_writer.next()
            if not arg_reader.next():
                break

class cosine_similarity_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return cosine_similarity()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addArrayType(vertica_sdk.ColumnTypes.makeNumeric())
        arg_types.addArrayType(vertica_sdk.ColumnTypes.makeNumeric())
        return_type.addFloat()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addFloat()

# Install:
# CREATE OR REPLACE LIBRARY PyVectorFunctions AS 'vector_udx.py' LANGUAGE 'Python';
# CREATE OR REPLACE FUNCTION cosine_similarity AS NAME 'cosine_similarity_factory' LIBRARY PyVectorFunctions;
# Example usage
# => select cosine_similarity(ARRAY[1,2,3],ARRAY[4,5,6]);
# cosine_similarity
#-------------------
# 0.974631846197076
