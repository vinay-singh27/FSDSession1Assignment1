from schema import Schema, And, Use, SchemaError, SchemaMissingKeyError
import re
import numpy as np

data1 = {'Sepal_Length': 'dasdsasa', 'Sepal_Width': '2', 'Petal_Length': '1', 'Petal_Width' : 'a'}

def exceptions(df):

    schema = Schema([{'Sepal_Length': Use(float),
                'Sepal_Width': Use(float),
                'Petal_Length': Use(float),
                'Petal_Width': Use(float)
                }])

    try : 
        output = schema.validate([df])

    except SchemaError as error:
        output = "Error : " + parse_error_message(error.code)

    # print(output)  
    return (output, True)


def parse_error_message(error_message) :

    value_error = 'ValueError'
    missing_values = 'Missing keys'

    if re.search(missing_values, error_message) :
        matches = re.search('Missing keys: (.*)', error_message)
        return 'Please enter values for : ' + matches.group(1)

    if re.search(value_error, error_message) :
        matches =  re.search('Key (.*)error', error_message)
        return 'Invalid value enter for ' + matches.group(1)

# print(exceptions(data1))
# # print(parse_error_message(data1))

print(exceptions(data1))

# print( np.array(list(exceptions(data1)[0][0].values()) ))